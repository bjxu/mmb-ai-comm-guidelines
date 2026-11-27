---
title: "Tone of voice in French"
appliesWhen: >-
  Any customer-facing French text (fr-CH), generated or reviewed; always load.
version: "1"
isGlobal: true
document_id: "tone-of-voice-fr"
description: "French tone-of-voice rules for generating and reviewing customer messages, based on the Helsana corporate correspondence guidelines."
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
  - source_id: "CPM-KB-SRC-002-fr"
    title: "Corporate language - French.pdf"
    sections: "C'est le ton qui fait la musique (p. 1–7)"
review_notes:
  - "There is no fr-006: the French 'Être crédible' only says 'Se relire permet d'éviter les lourdeurs stylistiques'. Merged into fr-002, together with its example."
  - "fr-010: the source also lists the subjunctive as relativising. Left out, because French grammar often requires it; confirm."
  - "Not in the source, added to prevent false reports and content changes: the exceptions for greetings and closings (001, 009), for the name Helsana (008) and for real uncertainty (010), the instruction for input without concrete information (001), the fallback for vague time words (003) and the restriction on writing definitions (007)."
  - "fr-012 (vous) comes from one sentence in the source; the full rules are in section 10 Form of address. Severity set to mandatory, because 'tu' towards a customer is an error, not a matter of style."
---
## Pertinence : nous donnons des réponses

### Write punchy messages (`cpm-kbs-tone-fr-001`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Rédiger clairement", p. 2
- **Instruction:** Avoid filler words that say little or are self-evident. Replace general adjectives with concrete information, but only with information from the input. If the input has none, remove the empty adjective or leave the sentence unchanged.
- **Avoid:** `conseillers compétents` (competence is a basic requirement for every adviser), `sympa`, `gentil`, `prévenant`, `efficace`
- **Not affected:** fixed greetings, closings and wishes, for example `Bonjour`, `Meilleures salutations`, `Prompt rétablissement`.

### Stay simple (`cpm-kbs-tone-fr-002`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Rester simple", p. 2; "Être crédible", p. 4
- **Instruction:** Concentrate on the essentials. Avoid redundancy and heavy, roundabout phrasing; prefer the plain expression.
- **Replace:** `des détails plus précis` → `des informations détaillées`, `procéder à l’envoi` → `envoyer`, `un examen réalisé pour la première fois` → `le premier examen`

### Take the customer's perspective (`cpm-kbs-tone-fr-003`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Adopter le point de vue du client", p. 3
- **Instruction:** Avoid company-centred wording and marketing or business jargon. Drop qualifiers the reader does not need.
- **Avoid:** `valeur ajoutée`, `plage horaire`, `proactif`, `ciblé`, `asap`
- **Vague time words** such as `asap`: replace only with a concrete time from the input; otherwise leave them unchanged and report them.
- **Replace:** `conseil en assurance` → `conseil`, `couverture d’assurance` → `couverture`, `prestation d’assurance` → `prestation`, `vendre` → `proposer`, `offrir`

## Intelligibilité : formuler de manière claire

### Keep sentences short (`cpm-kbs-tone-fr-004`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Rester bref", p. 3–4
- **Instruction:** Avoid long sentences, too many insertions, strings of nouns and additions after an article. Use at most one relative clause per sentence. In longer sentences, put the main verb as early as possible.

### Use verbs, not nominalisations (`cpm-kbs-tone-fr-005`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Être clair", p. 4
- **Instruction:** Leave nominalisations to legal texts. Use the verb instead, because it shows more clearly who does what.

### Explain foreign words and technical terms (`cpm-kbs-tone-fr-007`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Si nécessaire, clarifier", p. 5; "Pertinence", p. 2
- **Instruction:** Use foreign words, especially anglicisms, sparingly. A foreign word is fine when it has entered everyday language (`e-mail`, not `courrier électronique`). Use foreign or classical technical terms only when there is no French alternative, and explain them if their meaning is not obvious. Use only an explanation from the input or an approved glossary; when reviewing, report an unexplained term instead of writing a definition. For abbreviations, see section 03, Abbreviations.
- **Replace:** `underwriting` → `examen du risque`, `meeting` → `réunion`, `médicaments OTC` → `médicaments en vente libre, sans ordonnance`, `deadline` → `délai`

### Address the reader directly (`cpm-kbs-tone-fr-008`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Formulation directe", p. 5
- **Instruction:** Put the reader at the centre. As a rule, do not refer to Helsana by name; use `nous` instead (see also section 12, Helsana the brand).
- **Not affected:** the signature, product and service names (for example `Helsana+`, l’app Helsana) and the names of legal entities.

## Transparence : nous écrivons comme nous sommes

### Be realistic: no superlatives (`cpm-kbs-tone-fr-009`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Rester réaliste", p. 5–6
- **Instruction:** Avoid meaningless superlatives. Convince through service and commitment, not exaggeration.
- **Avoid:** `extraordinaire`, `excellent`, `fantastique`, `les meilleurs`, `le plus grand nombre`
- **Not affected:** fixed greetings and closings, for example `Meilleures salutations`, `Avec nos meilleurs messages`.

### Be accessible: no relativising words (`cpm-kbs-tone-fr-010`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Être accessible", p. 6
- **Instruction:** Avoid modal verbs and adverbs that weaken a statement or create doubt.
- **Report:** `certainement` used as filler, and `pouvoir`, `devoir` when the sentence stays true without them.
- **Not affected:** modal verbs that state a real option, permission or obligation (`Vous pouvez résilier jusqu’au 30 novembre`, `Vous devez remettre le formulaire`), and words such as `probablement` or `éventuellement` that express real uncertainty about a fact. Removing them would turn an uncertain statement into a promise.

### Write in the active voice (`cpm-kbs-tone-fr-011`)

- **Severity:** guideline
- **Source:** Corporate language FR, "Privilégier les tournures actives", p. 6–7
- **Instruction:** Write in the active voice. Passive sentences are heavy and hide the action. Name the actor only if the input makes it clear; otherwise keep the passive.

### Formal address (`cpm-kbs-tone-fr-012`)

- **Severity:** mandatory
- **Source:** Corporate language FR, "Pertinence", p. 2
- **Instruction:** Address the reader as `vous`. The detailed rules are in section 10, Form of address.

