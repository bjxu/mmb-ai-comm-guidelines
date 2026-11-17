---
title: "Currency Format Rules"
document_id: "cpm-kbs-currency-format"
description: "Language-specific rules for generating and reviewing currency amounts based on the corporate Helsana correspondence guidelines."
content_type: "knowledge-base-source"
version: "1.0"
updated: "2026-10-16"
author: "Marina Soblis"
status: "draft"
approval_status: "pending"
approved_by: null
approved_at: null
tags:
- "currency"
- "money"
- "formatting"
- "corporate-language"
sources:
- source_id: "CPM-KB-SRC-002-de"
  title: "Corporate Language - Brand Portal (1).pdf"
- source_id: "CPM-KB-SRC-002-fr"
  title: "Corporate language - Brand Portal_F.pdf"
- source_id: "CPM-KB-SRC-002-it"
  title: "Corporate language - Brand Portal_I.pdf"
- source_id: "CPM-KB-SRC-002-en"
  title: "Corporate language - Brand Portal_E.pdf"
is_global: false
---

## Corporate Currency Formatting Guidelines

### Purpose

Use these rules when generating or reviewing currency amounts in text.  
Apply the rules from the section corresponding to the output language.  
The rules define formatting only. They must not be used to infer, calculate, convert, round, or change the factual monetary value or currency.

### Rule application

Apply the following principles:
- Preserve the factual monetary value and currency from the source content.
- Apply the rules corresponding to the requested output language.
- Apply shared rules together with the applicable language-specific rules.
- If a language-specific rule conflicts with a shared rule, apply the language-specific rule.
- Do not infer a missing, incomplete, or ambiguous amount or currency.
- Do not convert one currency into another unless explicitly requested.
- Do not change currency amounts that form part of an identifier or other immutable source value.

## Shared rules

#### cpm-kbs-currency-general-001

**Requirement level:** MUST  
**Instruction:** Use the international currency code before a currency amount when the amount is written in figures.  
**Correct:**
- CHF 2.50
- EUR 2.50
- USD 2.50

#### cpm-kbs-currency-general-002

**Requirement level:** MUST  
**Applies to:** Currency amounts with minor units (Rappen/cents).  
**Instruction:** Separate the major and minor currency units with a full stop and write two digits for the minor units.  
**Correct:**
- CHF 2.50
- EUR 2.50
- USD 2.50

#### cpm-kbs-currency-general-003

**Requirement level:** MUST  
**Applies to:** Currency amounts without minor units in running text.  
**Instruction:** Write the currency code and whole amount followed by the approved dash notation for zero minor units.  
**Format:** CCC n.—  
**Correct:**
- CHF 200.—
- EUR 200.—
- USD 200.—

#### cpm-kbs-currency-general-004

**Requirement level:** MUST  
**Applies to:** Currency amounts in tables.  
**Instruction:** Always show two digits after the decimal point, including `.00` when there are no minor units.  
**Correct:**
- CHF 6.00
- EUR 6.00
- USD 6.00  
**Incorrect:**
- CHF 6
- EUR 6
- USD 6

## German (de-CH)

#### cpm-kbs-currency-de-001

**Requirement level:** MUST  
**Instruction:** Use CHF as the international currency code for amounts in Swiss francs.  
**Correct:**
- CHF 2.50
- CHF 200.—

#### cpm-kbs-currency-de-002

**Requirement level:** MUST  
**Instruction:** For monetary amounts, use a full stop to separate francs and rappen. This rule also applies to other currencies.  
**Correct:**
- CHF 46.60  
**Incorrect:**
- CHF 45,60

#### cpm-kbs-currency-de-003

**Requirement level:** MUST  
**Applies to:** Decimal numbers that are not currency amounts.  
**Instruction:** Use a comma as the decimal separator. Do not extend the currency decimal-point rule to non-monetary decimal numbers.  
**Correct:**
- 45,2 Liter
- CHF 45,2 Mio.  
**Incorrect:**
- 45.2 Liter
- CHF 45.2 Mio.

#### cpm-kbs-currency-de-004

**Requirement level:** MUST  
**Applies to:** Large numbers in currency amounts.  
**Instruction:** Group numbers of five or more digits in groups of three from the right using a protected space; do not use an apostrophe as a thousands separator.  
**Correct:**
- CHF 3 000 000.—  
**Incorrect:**
- CHF 3'000'000.—

#### cpm-kbs-currency-de-005

**Requirement level:** MUST  
**Applies to:** Published/editorial texts.  
**Instruction:** Write Swiss-franc amounts either as a number word or as a figure followed by `Franken`, according to the approved publication style.  
**Correct:**
- mehrere zehntausend Franken
- 100 Franken

## English (en-GB)

#### cpm-kbs-currency-en-001

**Requirement level:** MUST  
**Instruction:** Use CHF as the international currency code for Swiss francs. In most contexts, state monetary amounts using the ISO currency code.  
**Correct:**
- CHF 2.50
- CHF 200.—

#### cpm-kbs-currency-en-002

**Requirement level:** MUST  
**Applies to:** Currency names written out in running text.  
**Instruction:** Where the approved publication style permits a currency name to be written out, write the currency name out when no figure is given. Do not write out the currency name when the amount contains a decimal point.

#### cpm-kbs-currency-en-003

**Requirement level:** MUST NOT  
**Instruction:** Do not write out a currency name for an amount containing a decimal point. Use the currency code.  
**Correct:**
- CHF 2.50  
**Incorrect:**
- 2.50 Swiss francs

#### cpm-kbs-currency-en-004

**Requirement level:** MUST  
**Applies to:** Tables.  
**Instruction:** Write currency amounts with a decimal point and always show two decimal digits.  
**Correct:**
- CHF 6.00
- EUR 6.00
- USD 6.00

## French (fr-CH)

#### cpm-kbs-currency-fr-001

**Requirement level:** MUST  
**Instruction:** Use CHF as the international currency code for Swiss francs.  
**Correct:**
- CHF 2.50
- CHF 200.—

#### cpm-kbs-currency-fr-002

**Requirement level:** MUST  
**Applies to:** Running text.  
**Instruction:** Write amounts with cents using two decimal digits. For amounts without cents, use the approved dash notation.  
**Correct:**
- CHF 2.50
- CHF 200.—
- EUR 2.50
- EUR 200.—
- USD 2.50
- USD 200.—

#### cpm-kbs-currency-fr-003

**Requirement level:** MUST  
**Applies to:** Tables.  
**Instruction:** Always show two decimal digits, including `.00` when there are no cents.  
**Correct:**
- CHF 6.00
- EUR 6.50
- EUR 6.00
- USD 6.50
- USD 6.00

## Italian (it-CH)

#### cpm-kbs-currency-it-001

**Requirement level:** MUST  
**Instruction:** Use CHF as the international currency code for Swiss francs.  
**Correct:**
- CHF 2.50
- CHF 200.—

#### cpm-kbs-currency-it-002

**Requirement level:** MUST  
**Applies to:** Running text.  
**Instruction:** Write amounts with cents using two decimal digits. For amounts without cents, use the approved dash notation.  
**Correct:**
- CHF 2.50
- CHF 200.—
- EUR 2.50
- EUR 200.—
- USD 2.50
- USD 200.—

#### cpm-kbs-currency-it-003

**Requirement level:** MUST  
**Applies to:** Tables.  
**Instruction:** Always show two decimal digits, including `.00` when there are no cents.  
**Correct:**
- CHF 2.00
- EUR 2.50
- EUR 2.00
- USD 2.50
- USD 2.00
