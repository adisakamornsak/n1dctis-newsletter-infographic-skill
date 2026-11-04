# Changelog

## v2.1.1 - 2026-11-04

- Prohibit newly invented mottos, slogans, taglines, catchphrases, and inspirational sign-offs unless explicitly requested by the user for the current newsletter.
- Preserve supplied motto wording verbatim; omit empty motto panels rather than filling them from reference layouts.
- Apply the rule to mascot speech, decorative backgrounds, headers, captions, banners, and footers as well as body copy.
- Shorten the Thai prompt to a quick-fill form with automatic design defaults and a compact set of protected brand/content rules.
- Bundle the same short prompt with the skill, and add instruction-contract regression tests. These tests check documentation consistency, not model behavior.


## v2.1 - 2026-11-03

- Added support for optional use of the PEA Watt-D mascot as a decorative brand character in newsletters.
- Added rules allowing decorative backgrounds to change according to the character of each news story while remaining non-factual and readable.
- Added `mascot_usage` and `background_direction` input controls.
- Added a dedicated reference for mascot/background behavior and extended routing, workflow, and QA guidance.
- Clarified that mascot/background layers must stay separate from protected logo, locked copy, and unchanged user-supplied images.

## v2.0 - 2026-11-03

- Retained the original PEA Newsletter Infographic skill, its exact source-logo asset, and text/photo/numeric audit scripts.
- Added four distinct art-direction mockups and five-variant routing, including Digital Operations, Cyber Shield, Enterprise Systems & Analytics, and Cyber Ops & Infrastructure.
- Clarified that sample percentages, example dates, sample photos, and AI-generated logo representations in mockups are not verified content and must never be propagated to real newsletters.
- Clarified selectable layout names, automatic content-based layout selection, and variation rules for recurring departmental newsletters.
- Added instructions to generate tech/cyber-themed decorative backgrounds/icons as separate visual layers, not as edits to user photos.
- Extended the verification checklist and updated font, logo, and source data gates.

## v1.0 - 2026-11-03

- Initial Chiang Mai-style newsletter skill with protected logo, locked organization copy, Google Sans requirement, image integrity, numeric audit, and one approved layout reference.
