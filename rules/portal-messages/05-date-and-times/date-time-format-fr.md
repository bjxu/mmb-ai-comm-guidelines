---
title: "Dates and times in French"
appliesWhen: >-
  French text (fr-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "2"
isGlobal: false
document_id: "date-time-format-fr"
requires:
  - "date-time-format-general"
description: "French rules for generating and reviewing dates and times, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-fr"
    title: "Corporate language - French.pdf"
    sections: "Date et heure (p. 10–11); Objets (p. 33–35)"
review_notes:
  - "fr-002: version 1 required a leading zero (09 h 30). The source allows dropping it in correspondence ('tu peux laisser de côté le zéro') and its table uses 8 h 30. Changed to: generate without zero, accept both."
  - "fr-003: the source says full hours *may* be written without minutes ('tu peux'). Changed from mandatory to preferred."
  - "fr-005: '1er' is not mentioned in 'Date et heure'; it comes from the example 'née le 1er janvier 2020' in 'Objets'. Confirm."
---
Apply together with `date-time-format-general`, which defines running text versus short form, non-breaking spaces and four-digit years.

## Date in running text (`cpm-kbs-datetime-fr-001`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language FR, "Date et heure", p. 10
- **Instruction:** Write the day without a leading zero, then the full month name in lowercase, then the four-digit year.
- **Format:** `d MMMM yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `03 septembre 2026` | `3 septembre 2026` |
  | `3 Septembre 2026` | `3 septembre 2026` |
  | `3 sept. 2026` | `3 septembre 2026` |
  | `03.09.2026` | `3 septembre 2026` |

## Times (`cpm-kbs-datetime-fr-002`)

- **Applies to:** running text and short form
- **Severity:** preferred
- **Source:** Corporate language FR, "Date et heure", p. 10
- **Instruction:** Use the 24-hour clock. Separate hours and minutes with `h`, with a space on each side. When generating, write the hour without a leading zero. When reviewing, also accept the hour with a leading zero.
- **Format:** `<hour> h <minutes>`
- **Preferred:** `9 h 30`, `14 h 45`
- **Also accepted:** `09 h 30`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `9h30` | `9 h 30` |
  | `09h 30` | `9 h 30` |
  | `9:30` | `9 h 30` |

## Full hours in running text (`cpm-kbs-datetime-fr-003`)

- **Applies to:** running text, times on the full hour
- **Severity:** preferred
- **Source:** Corporate language FR, "Date et heure", p. 10
- **Instruction:** When generating, write full hours without minutes, followed by `heures`. When reviewing, accept both forms.
- **Preferred:** `Vous trouverez porte ouverte jusqu’à 12 heures.`
- **Also accepted:** `Vous trouverez porte ouverte jusqu’à 12 h 00.`

## Date in subject lines and tables (`cpm-kbs-datetime-fr-004`)

- **Applies to:** short form (subject lines, tables)
- **Severity:** mandatory in subject lines; preferred in tables
- **Source:** Corporate language FR, "Objets", p. 33 (subject lines: `jj.mm.AAAA`); "Date et heure", p. 10 (tables: "il est possible")
- **Instruction:** Write the date in numbers with leading zeros, separated by full stops. In tables, also accept the running-text form.
- **Format:** `dd.mm.yyyy`
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `7.1.2026` (subject line) | `07.01.2026` |
  | `7 janvier 2026` (subject line) | `07.01.2026` |

## First day of the month (`cpm-kbs-datetime-fr-005`)

- **Applies to:** running text
- **Severity:** mandatory
- **Source:** Corporate language FR, "Objets", p. 35 (example `née le 1er janvier 2020`)
- **Instruction:** Write the first day of a month as `1er`. Write all other days as plain numbers.
- **Examples:**

  | Incorrect | Correct |
  |---|---|
  | `1 janvier 2026` | `1er janvier 2026` |
  | `1° janvier 2026` | `1er janvier 2026` |
  | `2e janvier 2026` | `2 janvier 2026` |
