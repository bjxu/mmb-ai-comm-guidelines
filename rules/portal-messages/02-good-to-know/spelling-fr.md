---
title: "Spelling in French"
appliesWhen: >-
  Any customer-facing French text (fr-CH), generated or reviewed; always load.
version: "1"
isGlobal: true
document_id: "spelling-fr"
description: "French spelling and punctuation references and variant choice for generating and reviewing customer messages, based on the Helsana corporate correspondence guidelines."
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
  - "punctuation"
  - "corporate-language"
sources:
  - source_id: "CPM-KB-SRC-002-fr"
    title: "Corporate language - French.pdf"
    sections: "Bon à savoir (p. 7–8)"
review_notes:
  - "The source names 'Le bon usage' by Maurice Grevisse and 'André Goose'. The co-author's name is André Goosse; corrected here."
  - "fr-003: the source only names the 'Guide du typographe romand'. The concrete punctuation rules (spaces before : ; ! ?, guillemets) are not given and are left to the specific sections, e.g. 04 Quotation marks."
  - "The review instructions in fr-001 and fr-002 (report only clear errors; report a variant only when certain) are not in the source. A model cannot look up the Larousse recommendation, so it must not guess."
---
## Follow official French spelling (`cpm-kbs-spelling-fr-001`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language FR, "Bon à savoir", p. 7
- **Instruction:** Use the official French spelling rules. The reference work is *Le bon usage* by Maurice Grevisse and André Goosse. When reviewing, report only clear spelling errors. Do not report a spelling that is also correct; for variants, see fr-002.

## Choose the variant Larousse recommends (`cpm-kbs-spelling-fr-002`)

- **Applies to:** words with more than one correct spelling
- **Severity:** preferred
- **Source:** Corporate language FR, "Bon à savoir", p. 7
- **Instruction:** When several spellings are possible, use the one the Larousse recommends. When reviewing, report a variant only if you are certain which form the Larousse recommends; otherwise leave it unchanged.

## Punctuation: Guide du typographe romand (`cpm-kbs-spelling-fr-003`)

- **Applies to:** punctuation and typography
- **Severity:** mandatory
- **Source:** Corporate language FR, "Bon à savoir", p. 7
- **Instruction:** Follow the Swiss French conventions of the *Guide du typographe romand* for punctuation. Where a Helsana rule file covers a punctuation case (for example quotation marks), follow that file.

## Helsana rules come first (`cpm-kbs-spelling-fr-004`)

- **Applies to:** every text
- **Severity:** mandatory
- **Source:** Corporate language FR, "Bon à savoir", p. 7
- **Instruction:** Helsana sets its own rules in some areas, for example product names and document layout. Where a Helsana rule file covers a case, follow it, even if the reference works say otherwise.
