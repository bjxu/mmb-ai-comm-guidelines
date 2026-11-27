"""Split the Helsana "Corporate language" PDFs into one folder per section.

Each section folder gets <lang>.png (the section stacked into one image) and
<lang>.pdf (the section cropped from the vector PDF).

The PDFs are Confluence exports whose text layer is unusable (fonts have no
Unicode mapping), so sections are found visually: every section starts with a
grey horizontal rule + "Last modified on" line, followed by a large heading.
Section titles are read from the heading with Tesseract OCR. Sections are matched
across languages by order, so all four PDFs must yield the same number.

Requirements: tesseract-ocr (+ deu/fra/ita data), pip install pymupdf pillow pytesseract numpy
Usage: python scripts/split_sections.py [output_dir]
"""
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pymupdf
import pytesseract
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "helsana-knowledge-base"
LANGS = {
    "en": ("Corporate language - English.pdf", "eng"),
    "de": ("Corporate language - German.pdf", "deu"),
    "fr": ("Corporate language - French.pdf", "fra"),
    "it": ("Corporate language - Italian.pdf", "ita"),
}
OCR_DPI = 100
OUT_DPI = 150
PX = 72 / OCR_DPI  # OCR pixels -> PDF points

MARGIN = 20  # px kept above a heading
CONTENT_X = (60, 790)  # content column at OCR_DPI
HEADING_LEFT = (65, 78)


def render_gray(page):
    return np.array(Image.open(io.BytesIO(page.get_pixmap(dpi=OCR_DPI).tobytes("png"))).convert("L"))


def next_line(g, y):
    """Next ink line at/after row y as (top, bottom, left, right), or None."""
    ink = (g[:, CONTENT_X[0]:CONTENT_X[1]] < 200).any(axis=1)
    while y < len(ink) and not ink[y]:
        y += 1
    if y >= len(ink):
        return None
    e = y
    while e < len(ink) and ink[e]:
        e += 1
    cols = np.where((g[y:e] < 200).any(axis=0))[0]
    return y, e, int(cols[0]), int(cols[-1])


def heading_line(g, y):
    """Like next_line, but skips tiny artefacts (icons, specks)."""
    b = next_line(g, y)
    while b and b[1] - b[0] < 8:
        b = next_line(g, b[1])
    return b


def separator_rules(g):
    """Thin, full-width light-grey rules with white space above and below."""
    band = g[:, CONTENT_X[0]:CONTENT_X[1]]
    frac = ((band < 245) & (band > 150)).mean(axis=1)
    runs = []
    for y, f in enumerate(frac):
        if f > 0.9:
            if runs and y - runs[-1][1] <= 1:
                runs[-1][1] = y
            else:
                runs.append([y, y])
    out = []
    for a, b in runs:
        above, below = band[max(0, a - 6):max(0, a - 3)], band[b + 3:b + 6]
        if b - a <= 3 and (above.size == 0 or (above > 250).mean() > 0.95) \
                and (below.size == 0 or (below > 250).mean() > 0.95):
            out.append(b)
    return out


def is_heading(g, line, rule):
    top, bottom, left, _ = line
    if not (30 <= bottom - top <= 50 and HEADING_LEFT[0] <= left <= HEADING_LEFT[1]):
        return False
    if rule is not None and not 90 <= top - rule <= 125:
        return False
    crop = Image.fromarray(g[max(0, top - 8):bottom + 8, 50:800])
    d = pytesseract.image_to_data(crop, config="--psm 7", output_type=pytesseract.Output.DICT)
    hs = sorted(h for h, t in zip(d["height"], d["text"]) if t.strip())
    return bool(hs) and hs[len(hs) // 2] >= 24  # body text is ~12px


def ocr_title(g, top, lang):
    """OCR the (possibly wrapped) heading starting at row `top`."""
    ink = (g[:, CONTENT_X[0]:CONTENT_X[1]] < 200).any(axis=1)
    e, gap = top, 0
    while e < len(ink) and gap < 30:
        gap = 0 if ink[e] else gap + 1
        e += 1
    crop = Image.fromarray(g[max(0, top - 5):e, 50:800])
    crop = crop.resize((crop.width * 2, crop.height * 2))
    return " ".join(pytesseract.image_to_string(crop, lang=lang, config="--psm 6").split())


def find_sections(doc, lang):
    """Section = separator rule, small "Last modified" line, then a large heading
    ~105px below the rule (or at the top of the next page)."""
    G = [render_gray(p) for p in doc]
    found = {(0, next_line(G[0], 0)[0])}
    for pn, g in enumerate(G):
        for r in separator_rules(g):
            cands = []
            lm = next_line(g, r + 3)
            if lm and lm[1] - lm[0] <= 14 and HEADING_LEFT[0] <= lm[2] <= HEADING_LEFT[1] \
                    and lm[3] < 360 and lm[0] - r < 40:
                h = heading_line(g, lm[1])
                if h:
                    cands.append((pn, h, r))
                elif pn + 1 < len(G) and (h := heading_line(G[pn + 1], 0)):
                    cands.append((pn + 1, h, None))
            # Fallback when other content overlaps the "Last modified" line.
            y0 = r + 95
            if y0 < g.shape[0]:
                col = (g[y0:r + 125, 66:80] < 90).any(axis=1)
                if col.any() and (h := heading_line(g, y0 + int(col.argmax()))):
                    cands.append((pn, h, r))
            for hp, h, rr in cands:
                if is_heading(G[hp], h, rr):
                    found.add((hp, h[0]))
                    break
    return [{"page": pn, "y": max(0, y - MARGIN), "title": ocr_title(G[pn], y, lang)} for pn, y in sorted(found)]


def segments(doc, starts, k):
    """(page, y0, y1) slices in OCR pixels covering section k."""
    s = starts[k]
    end = starts[k + 1] if k + 1 < len(starts) else {"page": len(doc) - 1, "y": None}
    segs = []
    for pn in range(s["page"], end["page"] + 1):
        h = round(doc[pn].rect.height / PX)
        y0 = s["y"] if pn == s["page"] else 0
        y1 = end["y"] if pn == end["page"] and end["y"] is not None else h
        if y1 - y0 > 5:
            segs.append((pn, y0, y1))
    return segs


def trim_blank(img, keep=10):
    a = np.array(img.convert("L"))
    rows = np.where((a < 250).any(axis=1))[0]
    if not len(rows):
        return None
    return img.crop((0, max(0, rows[0] - keep), img.width, min(img.height, rows[-1] + keep)))


def export(doc, segs, png_path, pdf_path):
    parts, out_pdf = [], pymupdf.open()
    for pn, y0, y1 in segs:
        page = doc[pn]
        clip = pymupdf.Rect(0, y0 * PX, page.rect.width, y1 * PX) & page.rect
        im = Image.open(io.BytesIO(page.get_pixmap(dpi=OUT_DPI, clip=clip).tobytes("png"))).convert("RGB")
        im = trim_blank(im)
        if im is not None:
            parts.append(im)
            new = out_pdf.new_page(width=clip.width, height=clip.height)
            new.show_pdf_page(new.rect, doc, pn, clip=clip)
    stacked = Image.new("RGB", (max(p.width for p in parts), sum(p.height for p in parts)), "white")
    y = 0
    for p in parts:
        stacked.paste(p, (0, y))
        y += p.height
    stacked.save(png_path, optimize=True)
    out_pdf.save(pdf_path, garbage=4, deflate=True)


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "sections"
    docs, found = {}, {}
    for code, (fname, tess) in LANGS.items():
        docs[code] = pymupdf.open(SRC / fname)
        found[code] = find_sections(docs[code], tess)
        print(f"{code}: {len(found[code])} sections")

    counts = {c: len(s) for c, s in found.items()}
    if len(set(counts.values())) != 1:
        for c, s in found.items():
            print(c, [x["title"] for x in s])
        sys.exit(f"Section counts differ between languages: {counts}")

    index = []
    for k, en in enumerate(found["en"]):
        folder = out / f"{k + 1:02d}-{slug(en['title'])}"
        folder.mkdir(parents=True, exist_ok=True)
        entry = {"folder": folder.name, "titles": {}, "pages": {}}
        for code, doc in docs.items():
            segs = segments(doc, found[code], k)
            export(doc, segs, folder / f"{code}.png", folder / f"{code}.pdf")
            entry["titles"][code] = found[code][k]["title"]
            entry["pages"][code] = [segs[0][0] + 1, segs[-1][0] + 1]
        index.append(entry)
        print(folder.name, entry["titles"])
    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
