---
title: "Dates and times in French"
appliesWhen: >-
  French text (fr-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "1"
isGlobal: false
document_id: "date-time-format-fr"
description: "French rules for generating and reviewing dates and times based on the corporate Helsana correspondence guidelines."
content_type: "knowledge-base-source"
updated: "2026-10-15"
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
    title: "Corporate language - Brand Portal_F.pdf"
---
These rules define formatting only. Preserve the factual date and time from the source; never infer, complete, calculate or change a missing or ambiguous value, and do not alter dates or times that are part of an identifier or other immutable value.

Where a rule below conflicts with another guideline, the more specific rule wins.

#### ruleId: `cpm-kbs-datetime-general-001`

**Instruction:** Keep every complete date and time expression on one line.

#### ruleId: `cpm-kbs-datetime-general-002`

**Instruction:** When you write or rewrite a date or time expression, join its components with non-breaking spaces (U+00A0) so that a line break cannot separate them. This applies only to text you generate. When reviewing, never report a suggestion or issue for ordinary versus non-breaking spaces, and never flag a date or time that is already correct apart from the type of space; leave such text unchanged.

#### ruleId: `cpm-kbs-datetime-fr-001`

**Instruction:** Write the date in the order day, month, year.

Apply the following formatting rules:

- Write the day without a leading zero.
- Write the month name in full and in lowercase.
- Write the year after the month.

**Format:** `d MMMM yyyy`

**Correct:**

- `3 septembre 2016`

**Incorrect:**

- `03 septembre 2016`
- `3 Septembre 2016`
- `9 sept 2026`
- `septembre 3 2016`


#### ruleId: `cpm-kbs-datetime-fr-002`

**Instruction:** Use the 24-hour clock.

Apply the following formatting rules:

- Write the hour with two digits.
- Separate the hour and minutes with `h`.
- Use non-breaking spaces around `h`.

**Format:** `hh h mm`

**Correct:**

- `09 h 30`
- `11 h 45`

**Incorrect:**

- `09h 30`
- `09:30`

#### ruleId: `cpm-kbs-datetime-fr-003`

**Applies to:** Full hours in running text.

**Instruction:** Omit the minutes when expressing a full hour in running text and write `heures` after the hour.

**Correct:**

- `Vous trouverez porte ouverte jusqu’à 12 heures.`

**Incorrect:**

- `Vous trouverez porte ouverte jusqu’à 12 h 00.`
