---
title: "Dates and times in Italian"
appliesWhen: >-
  Italian text (it-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "2"
isGlobal: false
document_id: "date-time-format-it"
requires:
  - "date-time-format-general"
description: "Italian rules for generating and reviewing dates and times, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-it"
    title: "Corporate language - Italian.pdf"
    sections: "Data e ora (p. 9–10); Oggetto (p. 31–33)"
review_notes:
  - "it-004: the source table writes 'ore 08.30' in running text but only '08.30' in subject lines and tables. Rule limited to running text."
  - "it-005: version 1 called minutes optional but listed 'ore 12.00' as incorrect. Both forms are now accepted."
---
Apply together with `date-time-format-general`, which defines running text versus short form, non-breaking spaces and four-digit years. The source names letters, e-mails and portal messages explicitly as running text.

## Date in running text (`cpm-kbs-datetime-it-001`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language IT, "Data e ora", p. 9
- **Instruction:** Write the day without a leading zero, then the full month name in lowercase, then the four-digit year.
- **Format:** `d MMMM yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `03 settembre 2026` | `3 settembre 2026` |
  | `3 Settembre 2026` | `3 settembre 2026` |
  | `3 sett. 2026` | `3 settembre 2026` |
  | `03.09.2026` | `3 settembre 2026` |

## First day of the month (`cpm-kbs-datetime-it-002`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language IT, "Data e ora", p. 9
- **Instruction:** Write the first day of a month with the ordinal sign: `1°`. Write all other days as plain numbers.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `1 dicembre 2026` | `1° dicembre 2026` |
  | `1o dicembre 2026` | `1° dicembre 2026` |
  | `2° dicembre 2026` | `2 dicembre 2026` |

## Times (`cpm-kbs-datetime-it-003`)

- **Applies to:** running text and short form
- **Severity:** mandatory
- **Source:** Corporate language IT, "Data e ora", p. 9
- **Instruction:** Use the 24-hour clock with four digits: a leading zero for hours below 10 and a full stop between hours and minutes.
- **Format:** `hh.mm`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `9.30` | `09.30` |
  | `09:30` | `09.30` |
  | `9h30` | `09.30` |

## `ore` before the time (`cpm-kbs-datetime-it-004`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language IT, "Data e ora", p. 9
- **Instruction:** In running text, write `ore` before the time. Do not add `ore` in subject lines or tables.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `alle 09.30` | `alle ore 09.30` |
  | `09.30 ore` | `ore 09.30` |

## Full hours in running text (`cpm-kbs-datetime-it-005`)

- **Applies to:** running text, times on the full hour
- **Severity:** preferred
- **Source:** Corporate language IT, "Data e ora", p. 9
- **Instruction:** When generating, write full hours without minutes. When reviewing, accept both forms.
- **Preferred:** `Siamo aperti per lei fino alle ore 12.`
- **Also accepted:** `Siamo aperti per lei fino alle ore 12.00.`

## Date in subject lines and tables (`cpm-kbs-datetime-it-006`)

- **Applies to:** short form (subject lines, tables)
- **Severity:** mandatory
- **Source:** Corporate language IT, "Data e ora", p. 9; "Oggetto", p. 31
- **Instruction:** Write the date in numbers with leading zeros, separated by full stops.
- **Format:** `dd.mm.yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `3.9.2026` | `03.09.2026` |
  | `3 settembre 2026` | `03.09.2026` |
