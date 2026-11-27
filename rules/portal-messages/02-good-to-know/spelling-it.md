---
title: "Spelling in Italian"
appliesWhen: >-
  Any customer-facing Italian text (it-CH), generated or reviewed; always load.
version: "1"
isGlobal: true
document_id: "spelling-it"
description: "Italian spelling reference for generating and reviewing customer messages, based on the Helsana corporate correspondence guidelines."
content_type: "knowledge-base-source"
updated: "2026-11-27"
author: "Marina Soblis"
status: "draft"
approval_status: "pending"
approved_by: null
approved_at: null
tags:
  - "spelling"
  - "orthography"
  - "corporate-language"
sources:
  - source_id: "CPM-KB-SRC-002-it"
    title: "Corporate language - Italian.pdf"
    sections: "Buono a sapersi (p. 7)"
review_notes:
  - "Rule numbers match across languages: 001 spelling reference, 002 choice between variants, 003 language-specific rule, 004 Helsana rules first, 005 Swiss usage. Italian has no 002 or 003, because the source gives no variant rule."
  - "The Italian source only says the Treccani dictionary can be consulted ('puoi consultare'). Unlike DE, EN and FR, it does not say how to choose between variants. it-001 treats Treccani as the reference; confirm."
  - "The review instruction in it-001 (report only clear errors) is not in the source."
  - "Added, not in the source: it-005 (Swiss usage is correct) and the exemption of proper names and quoted text (001). Confirm."
---
## Follow Treccani spelling (`cpm-kbs-spelling-it-001`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language IT, "Buono a sapersi", p. 7
- **Instruction:** Use standard Italian spelling as recorded in the Treccani dictionary. When reviewing, report only clear spelling errors. Do not report a spelling that Treccani also accepts.
- **Not affected:** proper names of people, companies and places, official names and titles, and text quoted from the customer's message. Never change their spelling.

## Helsana rules come first (`cpm-kbs-spelling-it-004`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language IT, "Buono a sapersi", p. 7
- **Instruction:** Helsana sets its own rules in some areas, for example product names and document layout. Where a Helsana rule file covers a case, follow it, even if the dictionary says otherwise.

## Swiss usage is correct (`cpm-kbs-spelling-it-005`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** none (Swiss Italian; see review_notes)
- **Instruction:** Words and expressions used in Swiss Italian, including Swiss official terms, are correct. Do not replace them with the form used in Italy, and do not report them.
- **Examples:** `medicamento`, not `farmaco`; `cassa malati`; `AVS`
