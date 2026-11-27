---
title: "Dates and times in German"
appliesWhen: >-
  German text (de-CH) containing a date, time or time range, including opening hours, deadlines and appointments; load even if the formatting looks correct.
version: "1"
isGlobal: false
document_id: "date-time-format-de"
description: "German rules for generating and reviewing dates and times based on the corporate Helsana correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-de"
    title: "Corporate language - Brand Portal.pdf"
---
These rules define formatting only. Preserve the factual date and time from the source; never infer, complete, calculate or change a missing or ambiguous value, and do not alter dates or times that are part of an identifier or other immutable value.

Where a rule below conflicts with another guideline, the more specific rule wins.

#### ruleId: `cpm-kbs-datetime-general-001`

**Instruction:** Keep every complete date and time expression on one line.

#### ruleId: `cpm-kbs-datetime-general-002`

**Instruction:** When you write or rewrite a date or time expression, join its components with non-breaking spaces (U+00A0) so that a line break cannot separate them. This applies only to text you generate. When reviewing, never report a suggestion or issue for ordinary versus non-breaking spaces, and never flag a date or time that is already correct apart from the type of space; leave such text unchanged.

#### ruleId: `cpm-kbs-datetime-de-001`

**Instruction:** Write the date in the order day, month, year.

Apply the following formatting rules:

- Write the day without a leading zero.
- Add a full stop after the day.
- Write the month name in full with an initial capital letter.
- Write the year after the month.
- Write the year with four digits. Expand a two-digit year to the current century (`26` becomes `2026`).

**Format:** `d. MMMM yyyy`

**Correct:**

- `3. September 2026`

**Incorrect:**

- `03. September 2026`
- `4. April 26`
- `4 April 26`
- `3 September 2026`
- `3.september 2026`
- `September 3 2026`


#### ruleId: `cpm-kbs-datetime-de-002`

**Instruction:** Use the 24-hour clock.

Apply the following formatting rules:

- Write the hour without a leading zero.
- Separate hours and minutes with a full stop.
- Add `Uhr` after the time.
- Use a non-breaking space between the time and `Uhr`.

**Format:** `h.mm Uhr`

**Correct:**

- `9.30 Uhr`
- `11.45 Uhr`
- `13.30 Uhr`

**Incorrect:**

- `09.30 Uhr`
- `9.30`
- `9:45 Uhr`

#### ruleId: `cpm-kbs-datetime-de-003`

**Applies to:** Full hours in running text.

**Instruction:** Omit the minutes when expressing a full hour in running text.

**Correct:**

- `Wir haben von 8 bis 12 Uhr für Sie geöffnet.`
