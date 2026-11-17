---
name: pea-newsletter-infographic
description: Create Thai PEA newsletter infographics for PEA departments, defaulting to the information systems and cybersecurity team. Use when producing or updating internal PEA newsletter graphics from Thai source text and user-supplied images. Enforce the exact PEA logo placement, exact header/footer and a configurable department sub-header, Google Sans typography with Google Prompt as the fallback, unchanged user photos, unchanged numeric data, optional PEA Watt-D mascot, and five reusable purple/gold layouts. Accept any number of supplied news images, keep everything in one final portrait image, and deliver exactly one compressed JPG at 1440x2560 pixels rather than PNG. Also generate story-matched backgrounds or supporting artwork so the page does not feel plain or excessively empty, and support bento-grid style image layouts with intelligent crop-and-fill behavior.
---

# PEA Newsletter Infographic (team edition v3.0.0)

Create professional Thai newsletters following the PEA purple/gold visual identity. Support **five layouts** rather than duplicating one design. Read [layout catalog](references/layout-catalog.md) for style selection, composition, and art-direction patterns, [mascot/background rules](references/mascot-background-rules.md) for PEA Watt-D and backdrops, and [single-image layout rules](references/single-image-layout.md) before planning the page.

## Plugin runtime and synced version

Use the skill, references and assets bundled with the version currently synced by the Plugin system. Do not fetch GitHub, install software, run a local updater, require a terminal, or modify the installed Plugin before making a newsletter. A working synced copy is sufficient; no per-request online version check is required. Do not claim it is the newest GitHub commit. Report the bundled version when asked.

The workflow is designed for supported web, desktop and mobile Plugin hosts, without a local runtime dependency. Use the host's available image-generation, composition and export tools. Before production, confirm access to the bundled assets and tools that can preserve the original logo and every required user image, verify Thai typography, and export a real RGB JPG/JPEG at 1440x2560. Plugin installation alone does not supply these tools or fonts. If a required capability is missing or cannot be verified, report the specific limitation and offer a clearly labelled draft only; do not call it a compliant final deliverable. Do not regenerate protected assets to work around missing composition tools.

## Approved visual direction

For layout 01, inspect `assets/layout-01-chiang-mai-classic.jpg` as a flexible composition guide. Its photo slots, sample text, and abstract purple/gold background are illustrative. Vary the background with each story; Chiang Mai Classic does not require Doi Suthep, mountains, temples, or any fixed landmark.

For general activity and field-news stories, prefer the user-approved Chiang Mai Classic photo-grid treatment. Read [approved composition and Thai typography](references/approved-photo-grid.md) and inspect `assets/approved-photo-grid-reference.jpg` before designing a similar story. Apply its pale purple background, prominent headline, chronological activity strips, dense mixed-size photo grid, and integrated transparent Watt-D when appropriate. Adapt image count and sections to the current story; the example is not a source of facts. Explicit user layout choices and the other four layouts remain supported.

## Non-negotiable constraints

1. **Exact PEA logo**: if the bundled original logo asset is available, use that original asset. You may reduce its displayed size proportionally to suit the infographic dimensions and header composition: apply one uniform scale factor to both width and height (0 < scale <= 1), allowing only pixel-rounding differences. Preserve the complete logo, its original colors, proportions, and details; never crop, stretch, rotate, redraw, regenerate, recolor, otherwise edit, or replace it with an AI approximation. Keep it at upper left with adequate clear space and recognizable details at final viewing size. Keep the source asset file unchanged. The crop-to-fill permission for news images does not apply to the logo.
2. **Exact top header**: `กองเทคโนโลยีดิจิทัลและการสื่อสาร`.
3. **Configurable line immediately below header**: use the optional `sub_header` parameter for the department name. If omitted, empty, or whitespace-only, default to `แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์`. Trim surrounding whitespace from a supplied value, then preserve its wording exactly; do not infer a different department from the news or reference artwork. Keep this line immediately below the unchanged top header.
4. **Exact footer**: `การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)`.
5. **Typography**: use verified Thai-capable Google Sans for all newly composed text when available. If it cannot be used, use verified Thai-capable Google Prompt (Prompt) consistently instead and disclose the fallback in the final response. Do not silently substitute any other font; if neither font is available, report the blocker rather than claim compliance. Recheck Thai shaping, line breaks, and fit after switching fonts.
6. **Numbers are locked**: never invent, alter, round, or omit user-supplied dates, percentages, quantities, IDs, or technical specifications.
7. **User images are locked and unlimited in count**: accept any number of supplied news images, including zero. Reuse all required photos, screenshots, diagrams, and graphics exactly; do not retouch, recolor, or regenerate them. For layout purposes, you may scale, crop, zoom, and reposition supplied news images and supporting illustrations to focus on the key subject and create attractive collage or bento-grid compositions. Choose the focal point of each image deliberately, balance mixed tile sizes, and crop-to-fill frames without aspect-ratio gaps. Preserve essential people, objects, text, and context; never crop in a way that changes the meaning or factual evidence, and never distort the image. If a crop would remove essential content, adjust the frame or use contain placement instead. This permission applies to displayed image framing, not editing source files, and does not permit cropping the protected logo.
8. **Meaning is locked**: shorten Thai prose only when meaning, chronology, names, uncertainties, and technical terms remain unchanged.
9. **PEA Watt-D is optional but brand-sensitive**: use only as a secondary decorative helper when requested or clearly appropriate. Prefer a transparent cutout integrated into the page, placed beside the headline when space allows; follow `references/mascot-background-rules.md`.
10. **Background and supporting graphics should match the story**: actively create or select decorative backgrounds, hero illustrations, icons, graphic motifs, and filler visuals that match the news content so the page feels rich and intentional rather than blank. Backgrounds must remain non-factual, secondary to the content, and readable. Avoid leaving large plain white empty areas unless the content density truly requires negative space for readability. Empty sections may be filled with generated illustrations, icons, diagrams, decorative patterns, or thematic panels.
11. **Never invent a motto without an explicit user request**: do not create any motto, slogan, tagline, catchphrase, banner phrase, or inspirational sign-off unless the user explicitly asks for it in the current newsletter. Preserve a supplied motto verbatim unless revision is explicitly requested.
12. **Exactly one final static JPG/JPEG**: deliver exactly one final static image at **1440 × 2560 pixels** in **portrait orientation**. Do not paginate, split into multiple images, animate, or rotate. Do not substitute PNG, PDF, or PPTX as the final deliverable.
13. **JPEG output discipline**: export as a high-quality JPG/JPEG with an opaque background (no transparency). Keep compression high enough for readable Thai text and screenshots, then verify that readability survives the compression.
14. **No silent task changes**: if all required content cannot fit readably within 1440 × 2560 without violating the locked rules, report the conflict. Do not resize the canvas, split pages, omit required images, or claim completion.

## Input / output contract

- Accept Thai source copy, dates, headings, key points, and any number of supplied news images in the user’s order.
- Optional controls: `sub_header` (department line; blank/omitted uses the default above), `layout_choice`, `subject_focus`, `mascot_usage: auto | include | omit`, `background_direction: auto | cyber | digital | field | awareness | festive | neutral | custom description`.
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

1. Check the Plugin runtime capabilities above, then open `references/content-contract.md`, `references/layout-catalog.md`, `references/mascot-background-rules.md`, `references/single-image-layout.md`, and `references/quality-checklist.md`.
2. Resolve `sub_header` from the user’s value or the default and lock its wording. Extract and lock all user-supplied facts, dates, names, numbers, and image order. Record any user-supplied motto and any explicit authorization to create one.
3. Select layout 01–05, mascot usage, and background direction. Plan one fixed-size portrait composition at 1440 × 2560. Map every required news image to a visible placement on that single canvas. Use collage or bento-grid image grouping when it improves density, balance, or readability. Plan each image focal point and crop to emphasize it while retaining essential content.
4. Build decorative background/illustration layers separately from source images. Generate or compose backgrounds, hero visuals, icon sets, decorative motifs, and supporting filler graphics that are clearly related to the story theme (for example cyber, digital systems, infrastructure, awareness, internal fun, food/activity, etc.). Use PEA Watt-D only as a secondary decorative layer.
5. Compose all text in verified Thai-capable Google Sans, or Google Prompt when Google Sans is unavailable. Let Thai paragraphs flow to the available width with word-aware line breaks; remove premature hard breaks and inspect the rendered lines as described in `references/approved-photo-grid.md`. Insert every required supplied image. Use contain placement where appropriate, or use crop-to-fill placement when a bento-grid or photo-tile layout needs full-bleed image cells with no empty aspect-ratio gaps. Preserve important subjects and avoid distortion. Place the exact logo and protected header/sub-header/footer text.
6. With the host's composition tools, place the bundled original logo at upper left using proportional reduction only. Preserve its source bytes, complete visibility, colors, proportions and clear space. Keep decorative generation separate from logo and news-image composition. Do not regenerate the logo or user images.
7. Read the rendered text and compare it against the supplied source. Check names, dates, numeric values and their associations, technical terms and the resolved department line. Confirm the header, resolved sub-header and footer each appear exactly once. Do not invent extra facts or numbers; text recognition alone is not a full factual check.
8. Inspect the exported file with the host's available file/image tools: actual RGB JPG/JPEG, exact 1440x2560 geometry, one static image, opaque background and no orientation metadata that rotates it. Verify Thai shaping, readable text after compression, complete required-image coverage and a story-matched background. If file properties or font identity cannot be verified, state what is unverified and label the output as a draft instead of claiming full compliance.
9. Deliver only the single final JPG/JPEG. Report the selected layout, mascot decision, background direction, image count used, and any compliance blockers.

## Style system

- Primary dark purple approximately `#79005E`; secondary purple `#9A6597`; warm gold `#D5A125`; light wash `#F8F3FA`; white or very light background base.
- Use rounded cards, restrained shadow, clear margins, gold separators, and a clear visual hierarchy.
- Use contextual icons, illustrated hero elements, soft pattern overlays, gradient panels, and section graphics when helpful.
- Use background fills, color blocks, subtle patterns, generated mini-illustrations, or thematic icons to reduce large plain-white empty zones while preserving readability.
- Image galleries may use bento-grid structures with mixed tile sizes, rounded cards, and full-bleed crop-to-fill photos so the layout stays dense and polished without awkward gaps.
- Keep Watt-D, if used, away from the protected logo and text.

## Bundled resources

- `references/approved-photo-grid.md` = user-approved activity-news composition and Thai line-breaking guidance.
- `assets/approved-photo-grid-reference.jpg` = latest user-approved visual reference, not reusable news content.
- `references/layout-catalog.md` = five layout patterns and routing guidance.
- `references/mascot-background-rules.md` = PEA Watt-D and background usage rules.
- `references/content-contract.md` = content exactness and image-handling rules.
- `references/single-image-layout.md` = fixed-size one-image planning rules.
- `references/quality-checklist.md` = preflight QA checklist.
- `assets/content-input-example.md` = optional intake form.
- `assets/newsletter-prompt.th.md` = short fill-in prompt; keep identical to `../prompts/newsletter-prompt.th.md` when maintained in a repo.
