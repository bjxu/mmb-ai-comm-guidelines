---
title: "Dates and times – rules for all languages"
appliesWhen: >-
  Text in any language (de-CH, fr-CH, it-CH, en-GB) containing a date, time or time range, including opening hours, deadlines and appointments; load together with the language file, even if the formatting looks correct.
version: "2"
isGlobal: false
document_id: "date-time-format-general"
description: "Language-independent rules for generating and reviewing dates and times, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002"
    title: "Corporate language - English.pdf / German.pdf / French.pdf / Italian.pdf"
    sections: "Date and times; Subject line; Thousands and years"
review_notes:
  - "general-003: the source requires four-digit years but says nothing about completing two-digit years. Rule chosen: flag, never complete."
  - "general-004: weekday + date, date ranges and time ranges spanning am/pm are not covered by the source. Confirm with Helsana whether rules are needed."
---
## Scope

These rules define formatting only. Preserve every date and time exactly as given: never infer, complete, calculate or change the value. Leave dates and times unchanged when they are part of an identifier, a quotation, a reference number or a system extract.

Apply these rules together with the language file for the text's language. The language file defines the formats; this file defines when each format applies.

**Severity** in each rule means:

- **mandatory**: always apply when generating; report every deviation when reviewing.
- **preferred**: use this form when generating; when reviewing, accept the listed alternatives and do not report them.

## Context: running text or short form (`cpm-kbs-datetime-general-002`)

- **Applies to:** all dates and times
- **Severity:** mandatory
- **Source:** Corporate language, section "Date and times" (EN p. 9, DE p. 10, FR p. 10, IT p. 9) and section "Subject line" (EN p. 30, DE p. 32, FR p. 33, IT p. 31)
- **Instruction:** Before applying a format, decide which context the date or time is in:
  - **Running text:** the body of the message, including the salutation, closing and lists in the body. A portal message body is running text.
  - **Short form:** subject lines and tables.

  Each language file has separate rules for the two contexts. A format that is correct in one context is incorrect in the other.

## Keep dates and times on one line (`cpm-kbs-datetime-general-001`)

- **Applies to:** all dates and times
- **Severity:** mandatory when generating; never reported when reviewing
- **Source:** Corporate language, section "Date and times" (EN p. 10, DE p. 10, FR p. 10, IT p. 9)
- **Instruction:** When you write or rewrite a date or time, join its parts with non-breaking spaces (U+00A0) so that no line break can separate them. This covers the spaces between day, month and year, between a time and `Uhr`, `am`/`pm` or `h`, and between `ore` and a time. When reviewing, never report ordinary versus non-breaking spaces, and do not change a date or time that is correct apart from the type of space.

## Four-digit years (`cpm-kbs-datetime-general-003`)

- **Applies to:** all dates, in every context
- **Severity:** mandatory
- **Source:** Corporate language, section "Thousands and years" (EN p. 13, DE p. 14, FR p. 16, IT p. 13)
- **Instruction:** Always write the year with four digits. When you generate text, take the full year from the input. When you review a two-digit year (`26`, `'26`), report it, but do not complete it yourself. Ask for the full year, because the century cannot be known for certain (for example in birth dates).
- **Examples:**

  | Input | When reviewing |
  |---|---|
  | `4. April 26` | report: two-digit year, full year needed |
  | `3 September '26` | report: two-digit year, full year needed |

## Cases these rules do not cover (`cpm-kbs-datetime-general-004`)

- **Applies to:** dates and times in constructions that no rule describes
- **Severity:** mandatory
- **Instruction:** For a construction no rule covers, apply only the rules for its parts and leave the construction itself unchanged. Do not report it as an error. This includes a weekday before a date, date ranges, and time ranges that the language file does not mention. Example: in `Montag, 03. September 2026`, correct the day to `3.` but keep `Montag,` as written.
