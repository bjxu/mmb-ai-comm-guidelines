---
title: "Dates and times in Italian"
appliesWhen: >-
  Italian text (it-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "1"
isGlobal: false
document_id: "date-time-format-it"
description: "Italian rules for generating and reviewing dates and times based on the corporate Helsana correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-it"
    title: "Corporate language - Brand Portal_I.pdf"
---
These rules define formatting only. Preserve the factual date and time from the source; never infer, complete, calculate or change a missing or ambiguous value, and do not alter dates or times that are part of an identifier or other immutable value.

Where a rule below conflicts with another guideline, the more specific rule wins.

#### ruleId: `cpm-kbs-datetime-general-001`

**Instruction:** Keep every complete date and time expression on one line.

#### ruleId: `cpm-kbs-datetime-general-002`

**Instruction:** When you write or rewrite a date or time expression, join its components with non-breaking spaces (U+00A0) so that a line break cannot separate them. This applies only to text you generate. When reviewing, never report a suggestion or issue for ordinary versus non-breaking spaces, and never flag a date or time that is already correct apart from the type of space; leave such text unchanged.

#### ruleId: `cpm-kbs-datetime-it-001`

**Instruction:** Write the date in the order day, month, year.

Apply the following formatting rules:

- Write the day without a leading zero.
- Write the month name in full and in lowercase.
- Write the year after the month.

**Format:** `d MMMM yyyy`

**Correct:**

- `3 settembre 2026`

**Incorrect:**

- `03 settembre 2026`
- `3 Settembre 2026`
- `settembre 3 2026`
- `03 sett 2026`

#### ruleId: `cpm-kbs-datetime-it-002`

**Instruction:** Write the first day of a month using the ordinal symbol `°`. Use cardinal numbers for all subsequent days of the month.

**Correct:**

- `1° dicembre 2026`
- `2 dicembre 2026`

**Incorrect:**

- `1 dicembre 2026`
- `2° dicembre 2026`


#### ruleId: `cpm-kbs-datetime-it-003`

**Instruction:** Use the 24-hour clock.

Apply the following formatting rules:

- Write the hour with two digits.
- Separate hours and minutes with a full stop.

**Format:** `hh.mm`

**Correct:**

- `09.30`
- `15.45`

**Incorrect:**

- `9.30`
- `09:30`

#### ruleId: `cpm-kbs-datetime-it-004`

**Instruction:** Write `ore` before the time and use a non-breaking space between `ore` and the time.

**Correct:**

- `ore 09.30`

**Incorrect:**

- `09.30 ore`

#### ruleId: `cpm-kbs-datetime-it-005`

**Applies to:** Full hours in running text.

**Instruction:** Minutes may optionally be omitted when expressing a full hour in running text.

**Correct:**

- `Siamo aperti per lei fino alle ore 12.`

**Incorrect:**

- `Siamo aperti per lei fino alle ore 12.00.`
