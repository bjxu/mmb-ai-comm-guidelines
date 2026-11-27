---
title: "Dates and times in English"
appliesWhen: >-
  English text (en-GB) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "2"
isGlobal: false
document_id: "date-time-format-en"
requires:
  - "date-time-format-general"
description: "English rules for generating and reviewing dates and times, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-en"
    title: "Corporate language - English.pdf"
    sections: "Date and times (p. 9–10); Form of address, overview table (p. 17); Subject line (p. 30)"
review_notes:
  - "en-002: the source says ordinals 'can' be left out, then gives 'Write: 1 January 2020'. Treated as mandatory; confirm."
  - "en-004: the earlier example 'from 8 am to 1 pm' was not in the source and has been removed. Ranges spanning am and pm are not covered."
---
Apply together with `date-time-format-general`, which defines running text versus short form, non-breaking spaces and four-digit years.

## Date in running text (`cpm-kbs-datetime-en-001`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 9
- **Instruction:** Write the day without a leading zero and without a full stop, then the full month name with an initial capital, then the four-digit year.
- **Format:** `d MMMM yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `03 September 2026` | `3 September 2026` |
  | `3 Sept 2026` | `3 September 2026` |
  | `September 3, 2026` | `3 September 2026` |
  | `3 september 2026` | `3 September 2026` |
  | `03.09.2026` | `3 September 2026` |

## No ordinals in dates (`cpm-kbs-datetime-en-002`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 9; "Form of address" overview table, p. 17
- **Instruction:** Write the day as a plain number, without `st`, `nd`, `rd` or `th`, and without `the … of`.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `1st January 2026` | `1 January 2026` |
  | `the 1st of January 2026` | `1 January 2026` |

## Times (`cpm-kbs-datetime-en-003`)

- **Applies to:** running text and short form
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 9–10
- **Instruction:** Use the 12-hour clock. Write the hour without a leading zero, separate hours and minutes with a full stop, and add lowercase `am` or `pm`. Midnight is `12 am`, noon is `12 pm`. The same format applies in subject lines and tables.
- **Format:** `h.mm am` / `h.mm pm`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `09.30 am` | `9.30 am` |
  | `9:30 am` | `9.30 am` |
  | `9.30` | do not guess; report: am or pm missing |
  | `21.30` | `9.30 pm` |
  | `21.30 pm` | `9.30 pm` |
  | `9.30 AM` | `9.30 am` |

## Time ranges (`cpm-kbs-datetime-en-004`)

- **Applies to:** running text and short form, ranges within the same half of the day
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 9
- **Instruction:** Join the two times with an en dash (–) without spaces, and write `am` or `pm` once, after the second time.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `3.30 pm–4.00 pm` | `3.30–4.00 pm` |
  | `3.30 - 4.00 pm` | `3.30–4.00 pm` |

## Full hours (`cpm-kbs-datetime-en-005`)

- **Applies to:** running text, times on the full hour
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 10
- **Instruction:** Leave out the minutes for full hours.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `We are open till 5.00 pm.` | `We are open till 5 pm.` |

## Date in subject lines and tables (`cpm-kbs-datetime-en-006`)

- **Applies to:** short form (subject lines, tables)
- **Severity:** mandatory
- **Source:** Corporate language EN, "Date and times", p. 9–10; "Subject line", p. 30
- **Instruction:** Write the date in numbers with leading zeros, separated by full stops.
- **Format:** `dd.mm.yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `7.1.2026` | `07.01.2026` |
  | `7 January 2026` | `07.01.2026` |
  | `01/07/2026` | do not convert; report: day/month order unclear |
