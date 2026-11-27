---
title: "Tone of voice – rules for all languages"
appliesWhen: >-
  Any customer-facing text in any language (de-CH, fr-CH, it-CH, en-GB), generated or reviewed; always load together with the language file.
version: "1"
isGlobal: true
document_id: "tone-of-voice-general"
description: "Language-independent guidance for applying the Helsana tone of voice when generating and reviewing customer messages."
content_type: "knowledge-base-source"
updated: "2026-11-27"
author: "Marina Soblis"
status: "draft"
approval_status: "pending"
approved_by: null
approved_at: null
tags:
  - "tone-of-voice"
  - "style"
  - "corporate-language"
sources:
  - source_id: "CPM-KB-SRC-002"
    title: "Corporate language - English.pdf / German.pdf / French.pdf / Italian.pdf"
    sections: "Tone of voice (EN p. 1–6, DE p. 1–7, FR p. 1–7, IT p. 1–7)"
review_notes:
  - "The source is written for the website ('visitors'). Only the French version names correspondence explicitly ('Notre site web et notre correspondance'). Applying it to portal messages is an interpretation; confirm."
  - "The SEO exception in the source (rules do not apply to keywords) is left out, because it does not apply to portal messages."
  - "Rule 001 examples: the source writes the support-team example from the reader's view ('our individual needs'). Changed to the message's view ('your needs') in all four languages."
  - "general-001 to general-004 are not in the source. general-001 to -003 protect facts and legal meaning when the model rewrites style; general-004 resolves conflicts with other rule files. general-001 also restricts source rule 001, which tells writers to add concrete information: an LLM does not know the facts and would have to invent them. Confirm."
---
## Purpose

Helsana's tone of voice follows three brand principles: *add value with every contact*, *make things simple for our customers*, *be like a good friend*. In writing, this means three qualities, each described by the rules in the language file:

| Quality | Meaning | Rules in the language file |
|---|---|---|
| **Relevant**: we provide answers | active, open, clear-cut wording | 001–003 |
| **Easy to understand**: we get to the point | clear, simple, structured language | 004–008 |
| **Transparent**: we write the way we are | close, warm, accessible | 009–011 |

The same rule number means the same principle in every language. The language files give the word lists and examples for each language.

**Severity** in these files means:

- **guideline**: apply when generating. When reviewing, report only clear cases, as a suggestion with a concrete rewrite, never as an error.

## Preserve content (`cpm-kbs-tone-general-001`)

- **Applies to:** every rewrite made for tone
- **Source:** none (added safeguard for LLM use, not in the corporate language guide)
- **Severity:** mandatory
- **Instruction:** Tone rules change wording, never content. Keep every fact, amount, date, deadline, condition, obligation, refusal and legal statement exactly as it is. Never add information to make a sentence more concrete. The source examples use facts such as "125 years" or "certified by the Swiss Financial Market Supervisory Authority". Only use facts like these when they are in the input.

## Keep real possibility and obligation (`cpm-kbs-tone-general-002`)

- **Applies to:** rules 010 (modal verbs) and 011 (active voice) in the language files
- **Source:** none (added safeguard for LLM use, not in the corporate language guide)
- **Severity:** mandatory
- **Instruction:** Remove a modal verb only when it weakens a statement that is true without it. Keep it when it expresses a real option, permission or obligation, for example `You can cancel by 30 November` or `You must submit the form`. When you turn a passive sentence into an active one, name only an actor that the input makes clear. If the actor is unknown, keep the passive.

## Minimal rewrites (`cpm-kbs-tone-general-003`)

- **Applies to:** reviewing
- **Source:** none (added safeguard for LLM use, not in the corporate language guide)
- **Severity:** mandatory
- **Instruction:** When reviewing, report a tone issue only when a sentence clearly breaks a rule. Propose the smallest rewrite that fixes it. Do not rewrite sentences that are already acceptable, and do not restyle the whole message.

## Precedence (`cpm-kbs-tone-general-004`)

- **Applies to:** every text
- **Source:** none (added safeguard for LLM use, not in the corporate language guide)
- **Severity:** mandatory
- **Instruction:** The examples in the tone files illustrate only the principle they belong to. For everything else, follow the specific rule files, for example form of address, linguistic equality, product names, dates and amounts. Example: when a tone example uses the generic masculine (`Als Kunde …`), follow the linguistic-equality rules instead.
