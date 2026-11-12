---
name: pea-newsletter-infographic
description: Create Thai PEA newsletter infographics for the digital technology, information systems, and cybersecurity team. Use when producing or updating internal PEA newsletter graphics from Thai source text and user-supplied images. Enforce the exact PEA logo placement, exact department header/sub-header/footer, Google Sans-only typography, unchanged user photos, unchanged numeric data, optional PEA Watt-D mascot, and five reusable purple/gold layouts. Accept any number of supplied news images, keep everything in one final portrait image, and deliver exactly one compressed JPG at 1440x2560 pixels rather than PNG. Also generate story-matched backgrounds or supporting artwork so the page does not feel plain or excessively empty.
---

# PEA Newsletter Infographic (team edition v2.3.2)

Create professional Thai newsletters following the PEA purple/gold visual identity. Support **five layouts** rather than duplicating one design. Read [layout catalog](references/layout-catalog.md) for style selection, composition, and art-direction patterns, [mascot/background rules](references/mascot-background-rules.md) for PEA Watt-D and backdrops, and [single-image layout rules](references/single-image-layout.md) before planning the page.

## Non-negotiable constraints

1. **Exact PEA logo**: if the bundled original logo asset is available, use it unchanged. Never redraw, regenerate, recolor, distort, edit, or replace the logo with an AI approximation. Keep it at upper left with adequate clear space.
2. **Exact top header**: `กองเทคโนโลยีดิจิทัลและการสื่อสาร`.
3. **Exact line immediately below header**: `แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์`.
4. **Exact footer**: `การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)`.
5. **Google Sans only**: use a verified Thai-capable Google Sans installation for all newly composed text. Do not claim compliance if a fallback font is used.
6. **Numbers are locked**: never invent, alter, round, or omit user-supplied dates, percentages, quantities, IDs, or technical specifications.
7. **User images are locked and unlimited in count**: accept any number of supplied news images, including zero. Reuse all required photos, screenshots, diagrams, and graphics exactly; do not crop, retouch, recolor, regenerate, or cover them with decorative elements. Use proportional contain placement only.
8. **Meaning is locked**: shorten Thai prose only when meaning, chronology, names, uncertainties, and technical terms remain unchanged.
9. **PEA Watt-D is optional but brand-sensitive**: use only as a secondary decorative helper when requested or clearly appropriate.
10. **Background and supporting graphics should match the story**: actively create or select decorative backgrounds, hero illustrations, icons, and graphic motifs that match the news content so the page feels rich and intentional rather than blank. Backgrounds must remain non-factual, secondary to the content, and readable. Avoid leaving large plain white empty areas unless the content density truly requires negative space for readability.
11. **Never invent a motto without an explicit user request**: do not create any motto, slogan, tagline, catchphrase, banner phrase, or inspirational sign-off unless the user explicitly asks for it in the current newsletter. Preserve a supplied motto verbatim unless revision is explicitly requested.
12. **Exactly one final static JPG/JPEG**: deliver exactly one final static image at **1440 × 2560 pixels** in **portrait orientation**. Do not paginate, split into multiple images, animate, or rotate. Do not substitute PNG, PDF, or PPTX as the final deliverable.
13. **JPEG output discipline**: export as a high-quality JPG/JPEG with an opaque background (no transparency). Keep compression high enough for readable Thai text and screenshots, then verify that readability survives the compression.
14. **No silent task changes**: if all required content cannot fit readably within 1440 × 2560 without violating the locked rules, report the conflict. Do not resize the canvas, split pages, omit required images, or claim completion.

## Input / output contract

- Accept Thai source copy, dates, headings, key points, and any number of supplied news images in the user’s order.
- Optional controls: `layout_choice`, `subject_focus`, `mascot_usage: auto | include | omit`, `background_direction: auto | cyber | digital | field | awareness | festive | neutral | custom description`.
- Default deliverable: **one final JPG/JPEG only**, 1440 × 2560 px, portrait, RGB, opaque background.
- Treat layout references, logos, and mascot assets as supporting assets, not as report images.
- If content has not yet been provided, supply only a template/preview rather than invented news.

## Five layout options

| Option | Short name | Best use |
| --- | --- | --- |
| 01 | Chiang Mai Classic | PEA news, visits, field photos, general announcements |
| 02 | Digital Operations | Information systems, dashboards, digital services, platforms |
| 03 | Cyber Shield | Cyber awareness, protection guidance, policy, risk review |
| 04 | Enterprise Analytics | System integration, applications, service improvement, verified KPIs |
| 05 | Cyber Ops & Infrastructure | Network operations, SOC, monitoring, communications, fiber, security infrastructure |

Respect an explicit style choice. Otherwise auto-select the best match from the story.

## Production workflow

1. Open `references/content-contract.md`, `references/layout-catalog.md`, `references/mascot-background-rules.md`, `references/single-image-layout.md`, and `references/quality-checklist.md`.
2. Extract and lock all user-supplied facts, dates, names, numbers, and image order. Record any user-supplied motto and any explicit authorization to create one.
3. Select layout 01–05, mascot usage, and background direction. Plan one fixed-size portrait composition at 1440 × 2560. Map every required news image to a visible placement on that single canvas.
4. Build decorative background/illustration layers separately from source images. Generate or compose backgrounds, hero visuals, icon sets, and decorative motifs that are clearly related to the story theme (for example cyber, digital systems, infrastructure, awareness, internal fun, food/activity, etc.). Use PEA Watt-D only as a secondary decorative layer.
5. Compose all text in verified Google Sans. Insert every required supplied image with contain placement. Place the exact logo and protected header/sub-header/footer text.
6. If a logo file is available, use `python scripts/lock_logo.py input.jpg output.jpg --logo assets/pea-logo-exact-original.png` to apply or verify the exact logo at the required fixed canvas size without scaling the logo itself.
7. Transcribe readable final text and compare it against the source using `python scripts/audit_copy.py --source content_source.txt --final final_transcription.txt`.
8. Validate the exported image with `python scripts/validate_output.py final.jpg`. The validator checks JPEG format, exact dimensions, single-frame output, and safe orientation metadata. Also visually confirm that the page is not dominated by large plain white unused areas and that the generated/decorative background meaningfully supports the story.
9. Deliver only the single final JPG/JPEG. Report the selected layout, mascot decision, background direction, image count used, and any compliance blockers.

## Style system

- Primary dark purple approximately `#79005E`; secondary purple `#9A6597`; warm gold `#D5A125`; light wash `#F8F3FA`; white or very light background base.
- Use rounded cards, restrained shadow, clear margins, gold separators, and a clear visual hierarchy.
- Use contextual icons, illustrated hero elements, soft pattern overlays, gradient panels, and section graphics when helpful, but never place them over user photos.
- Use background fills, color blocks, subtle patterns, or thematic illustrations to reduce large plain-white empty zones while preserving readability.
- Keep Watt-D, if used, away from the protected logo and text.

## Bundled resources

- `references/layout-catalog.md` = five layout patterns and routing guidance.
- `references/mascot-background-rules.md` = PEA Watt-D and background usage rules.
- `references/content-contract.md` = content exactness and image-handling rules.
- `references/single-image-layout.md` = fixed-size one-image planning rules.
- `references/quality-checklist.md` = preflight QA checklist.
- `assets/content-input-example.md` = optional intake form.
- `assets/newsletter-prompt.th.md` = short fill-in prompt; keep identical to `../prompts/newsletter-prompt.th.md` when maintained in a repo.
- `scripts/audit_copy.py`, `scripts/lock_logo.py`, and `scripts/validate_output.py` = deterministic helper scripts.
