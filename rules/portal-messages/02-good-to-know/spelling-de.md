---
title: "Spelling in German"
appliesWhen: >-
  Any customer-facing German text (de-CH), generated or reviewed; always load.
version: "1"
isGlobal: true
document_id: "spelling-de"
description: "German spelling reference and variant choice for generating and reviewing customer messages, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-de"
    title: "Corporate language - German.pdf"
    sections: "Gut zu wissen (p. 7)"
review_notes:
  - "de-003 (ss instead of ß) is not stated in this section. It follows from the Swiss context and from the source's own spelling ('ausserordentlich', 'schliesslich', 'gesundheitsmässig'). Without it, 'follow Duden' could lead the model to write ß. Confirm, or point to the section that states it."
  - "The review instructions in de-001 and de-002 (report only clear errors; report a variant only when certain) are not in the source. A model cannot look up the Duden's yellow markings, so it must not guess."
  - "Added, not in the source: de-005 (Swiss usage is correct), the exemption of proper names and quoted text (001, 003), and consistent variants within a message (002). Confirm."
---
## Follow Duden spelling (`cpm-kbs-spelling-de-001`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language DE, "Gut zu wissen", p. 7
- **Instruction:** Use the current official German spelling as recorded in the Duden. When reviewing, report only clear spelling errors. Do not report a spelling that the Duden also allows; for variants, see de-002.
- **Not affected:** proper names of people, companies and places, official names and titles, and text quoted from the customer's message. Never change their spelling.

## Choose the variant the Duden recommends (`cpm-kbs-spelling-de-002`)

- **Applies to:** words with more than one correct spelling
- **Severity:** preferred
- **Source:** Corporate language DE, "Gut zu wissen", p. 7
- **Instruction:** When the Duden allows several spellings, use the one it recommends. Use the same variant throughout a message. When reviewing, report a variant only if you are certain which form the Duden recommends; otherwise leave it unchanged.

## Swiss spelling: ss, never ß (`cpm-kbs-spelling-de-003`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** none in this section (Swiss Standard German; see review_notes)
- **Instruction:** Write `ss`, never `ß`. This applies in every word, also where the Duden for Germany writes `ß`.
- **Examples:** `Grüsse`, `schliesslich`, `ausserdem`, `gemäss`, `Strasse`
- **Not affected:** proper names and foreign addresses, for example a surname `Weiß` or an address `Hauptstraße 5, München`.

## Helsana rules come first (`cpm-kbs-spelling-de-004`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language DE, "Gut zu wissen", p. 7
- **Instruction:** Helsana sets its own rules in some areas, for example product names and document layout. Where a Helsana rule file covers a case, follow it, even if the Duden says otherwise.

## Swiss usage is correct (`cpm-kbs-spelling-de-005`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** none (Swiss Standard German; see review_notes)
- **Instruction:** Words and expressions used in Swiss Standard German are correct. Do not replace them with the form used in Germany, and do not report them.
- **Examples:** `Spital`, not `Krankenhaus`; `allfällig`, not `etwaig`; `parkieren`, not `parken`
