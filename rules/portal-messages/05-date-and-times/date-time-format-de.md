---
title: "Dates and times in German"
appliesWhen: >-
  German text (de-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "2"
isGlobal: false
document_id: "date-time-format-de"
description: "German rules for generating and reviewing dates and times, based on the Helsana corporate correspondence guidelines."
content_type: "knowledge-base-source"
updated: "2026-11-27"
author: "Marina Soblis"
status: "draft"
approval_status: "pending"
approved_by: null
approved_at: null
tags:
  - "date"
  - "time"
  - "formatting"
  - "corporate-language"
sources:
  - source_id: "CPM-KB-SRC-002-de"
    title: "Corporate language - German.pdf"
    sections: "Datum und Zeit (p. 10–11); Betreffzeilen (p. 32–34)"
review_notes:
  - "de-003: the source says full hours *may* be written without minutes ('darfst'). Changed from mandatory to preferred."
  - "The source refers to Duden and DIN 5008 for everything not listed here."
---
## Date in running text (`cpm-kbs-datetime-de-001`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language DE, "Datum und Zeit", p. 10
- **Instruction:** Write the day without a leading zero, followed by a full stop, then the full month name, then the four-digit year.
- **Format:** `d. MMMM yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `03. September 2026` | `3. September 2026` |
  | `3 September 2026` | `3. September 2026` |
  | `3.september 2026` | `3. September 2026` |
  | `3. Sept. 2026` | `3. September 2026` |
  | `03.09.2026` | `3. September 2026` |

## Time in running text (`cpm-kbs-datetime-de-002`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language DE, "Datum und Zeit", p. 10
- **Instruction:** Use the 24-hour clock. Write the hour without a leading zero, separate hours and minutes with a full stop, and add `Uhr`.
- **Format:** `h.mm Uhr`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `09.30 Uhr` | `9.30 Uhr` |
  | `9:45 Uhr` | `9.45 Uhr` |
  | `9.30` | `9.30 Uhr` |
  | `13:30` | `13.30 Uhr` |

## Full hours in running text (`cpm-kbs-datetime-de-003`)

- **Applies to:** running text, times on the full hour
- **Severity:** preferred
- **Source:** Corporate language DE, "Datum und Zeit", p. 10
- **Instruction:** When generating, write full hours without minutes. When reviewing, accept both forms.
- **Preferred:** `Wir haben von 8 bis 12 Uhr für Sie geöffnet.`
- **Also accepted:** `Wir haben von 8.00 bis 12.00 Uhr für Sie geöffnet.`

## Date in subject lines and tables (`cpm-kbs-datetime-de-004`)

- **Applies to:** short form (subject lines, tables)
- **Severity:** mandatory
- **Source:** Corporate language DE, "Datum und Zeit", p. 10; "Betreffzeilen", p. 32
- **Instruction:** Write the date in numbers with leading zeros, separated by full stops.
- **Format:** `dd.mm.yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `3.9.2026` | `03.09.2026` |
  | `3. September 2026` | `03.09.2026` |
  | `03/09/2026` | `03.09.2026` |

## Time in subject lines and tables (`cpm-kbs-datetime-de-005`)

- **Applies to:** short form (subject lines, tables)
- **Severity:** mandatory
- **Source:** Corporate language DE, "Datum und Zeit", p. 10
- **Instruction:** Use the 24-hour clock with a leading zero, a full stop between hours and minutes, and `Uhr`.
- **Format:** `hh.mm Uhr`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `8.30 Uhr` | `08.30 Uhr` |
  | `08:30` | `08.30 Uhr` |
