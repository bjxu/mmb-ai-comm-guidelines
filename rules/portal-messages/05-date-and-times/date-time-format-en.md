---
title: "Dates and times in English"
appliesWhen: >-
  English text (en-GB) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "1"
isGlobal: false
document_id: "date-time-format-en"
description: "English rules for generating and reviewing dates and times based on the corporate Helsana correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-en"
    title: "Corporate language - Brand Portal_E.pdf"
---
These rules define formatting only. Preserve the factual date and time from the source; never infer, complete, calculate or change a missing or ambiguous value, and do not alter dates or times that are part of an identifier or other immutable value.

Where a rule below conflicts with another guideline, the more specific rule wins.

#### ruleId: `cpm-kbs-datetime-general-001`

**Instruction:** Keep every complete date and time expression on one line.

#### ruleId: `cpm-kbs-datetime-general-002`

**Instruction:** When you write or rewrite a date or time expression, join its components with non-breaking spaces (U+00A0) so that a line break cannot separate them. This applies only to text you generate. When reviewing, never report a suggestion or issue for ordinary versus non-breaking spaces, and never flag a date or time that is already correct apart from the type of space; leave such text unchanged.

#### ruleId: `cpm-kbs-datetime-en-001`

**Instruction:** Write the date in the order day, month, year.

Apply the following formatting rules:

- Write the day without a leading zero.
- Do not add a full stop after the day.
- Write the month name in full with an initial capital letter.
- Write the year after the month.

**Format:** `d MMMM yyyy`

**Correct:**

- `3 September 2020`

**Incorrect:**

- `03 September 2020`
- `3 Sept 2020`
- `September 3 2020`

#### ruleId: `cpm-kbs-datetime-en-002`

**Instruction:** Never use ordinal suffixes in English dates. Use a cardinal number.

**Correct:**

- `1 January 2020`

**Incorrect:**

- `1st January 2020`


#### ruleId: `cpm-kbs-datetime-en-003`

**Instruction:** Use the 12-hour clock.

Apply the following formatting rules:

- Write the hour without a leading zero.
- Separate hours and minutes with a full stop.
- Use lowercase `am` or `pm`.
- Use a non-breaking space between the time and `am` or `pm`.

**Format:** `h.mm am/pm`

**Correct:**

- `12 am` for midnight
- `12 pm` for noon
- `The meeting starts at 9.30 am.`

**Incorrect:**

- `09.30 am`
- `9.30`
- `21.30`
- `21:30`
- `21.30 pm`

#### ruleId: `cpm-kbs-datetime-en-004`

**Instruction:** For time ranges, place the period marker after the time as shown in the approved source format.

**Correct:**

- `3.30–4.00 pm`
- `We are open from 8 am to 1 pm.`

#### ruleId: `cpm-kbs-datetime-en-005`

**Applies to:** Full hours in running text.

**Instruction:** Omit the minutes when expressing a full hour in running text.

**Correct:**

- `We are open till 5 pm.`

**Incorrect:**

- `We are open till 5.00 pm.`
