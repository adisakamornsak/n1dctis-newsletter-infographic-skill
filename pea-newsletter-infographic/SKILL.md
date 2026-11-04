---
name: pea-newsletter-infographic
description: Create and update Thai PEA newsletter infographics for the digital technology, information systems and cybersecurity team. Trigger on PEA internal newsletters, activity updates, cyber awareness campaigns, IT operations reports, system integration, dashboards, monitoring, communications, and field work. Offer five distinct purple-and-gold layouts (classic, digital operations, cyber shield, enterprise analytics, cyber operations), optionally incorporate the PEA Watt-D mascot, and allow the decorative background to change according to the story theme, while protecting the exact original PEA logo, department header, sub-header, footer, all user-supplied photos, numeric values, and Google Sans-only typography. Support selecting a named style or auto-selecting from content, and prepare image-ready or print-ready outputs.
---

# PEA Newsletter Infographic (team edition v2.1.1)

Create professional Thai newsletters following the PEA purple/gold visual identity. Support **five layouts** rather than duplicating one design. Read [layout catalog](references/layout-catalog.md) for style selection, composition, and asset locations, plus [mascot/background rules](references/mascot-background-rules.md) for how to use PEA Watt-D and theme-based backdrops. Use visual references for **art direction only**: their sample text, dates, metrics, pictures, and generated/illustrated logos are NOT verified event data or final deliverable assets.

## Non-negotiable constraints

1. **Exact PEA logo**: use `assets/pea-logo-exact-original.png` as an unchanged image. Do not redraw, regenerate, recolor, distort, edit, crop within, or replace it with an AI approximation. Keep it at upper left with sufficient clear space. Composite the original logo AFTER generating any art/background. Its internal lettering belongs to the protected raster; no need to retype it.
2. **Exact top header**: `กองเทคโนโลยีดิจิทัลและการสื่อสาร`.
3. **Exact line immediately below header**: `แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์`.
4. **Exact footer**: `การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)`. Do not repeat department lines in footer. Preserve these three strings character-for-character.
5. **Google Sans only**: use a verified, authorized, Thai-capable Google Sans font for ALL newly composed text, captions, labels, icons-with-letters, numbers, charts, headers, and footer. No fallback or "Google Sans-like" substitute. Do not redistribute font files. If this exact font cannot render all Thai glyphs, flag the blocker and do not claim strict compliance; request access to a legally licensed compatible installation.
6. **Numbers are locked**: do not invent, alter, round, translate digits, convert units, recalculate, omit, or replace dates, times, percentages, quantities, prices, sequence numbers, IDs, and technical specifications from the supplied content. No example statistics or dates from reference images in a live newsletter. A numbered step list is permitted only if the user's source documents contain those steps and their order.
7. **User images are locked**: reuse all attached photos, diagrams, screenshots, and supplied graphics, not AI approximations; never re-imagine, retouch, recolor, erase, crop away, or place illustrations/text/icons over any part of them. Keep the aspect ratio with `contain` and letterboxing/padding rather than cropping. Preserve source originals unchanged in the project.
8. **Meaning is locked**: shorten Thai prose without changing meaning, chronology, uncertainties, names, technical terms, or coverage. Never fabricate project completion, security incidents, results, metrics, field workers, or institutional claims. If content does not fit, use an extra page or smaller number of modules, not missing facts or unreadably tiny text.
9. **PEA Watt-D is optional but brand-sensitive**: when requested, or when it clearly improves a friendly internal newsletter, use PEA Watt-D only as a decorative or guiding mascot. If an official mascot asset/reference is available, preserve its identity, colors, proportions, facial expression style, and signature features. Do not parody, deform, turn into another character, or let the mascot dominate the page more than the headline/content.
10. **Background may change by story theme**: choose or create a decorative background aligned with the news content (for example cyber, digital systems, field operations, awareness campaign, celebration, internal lifestyle/fun, or mixed IT content). Backgrounds must remain secondary, readable, and non-factual. Do not imply an unverified location, event, incident, or device state through the backdrop.

11. **Never invent a motto without an explicit user request**: do not create a motto, slogan, tagline, catchphrase, or inspirational sign-off unless the user explicitly asks to create it for the current newsletter. This covers Thai คำขวัญ, สโลแกน, คำคม and equivalent text in any language, including headlines used as slogans, banners, captions, mascot speech bubbles, background art, and footers. Preserve any user-supplied motto verbatim unless the user explicitly requests its revision. If no motto is supplied and creation is not explicitly requested, omit the motto block entirely; do not add a placeholder or ask for a motto by default. AUTO mode, a fun/creative tone, spare space, reference imagery, and quoted text inside source material are not permission to invent one. Keep ordinary factual headings and summaries grounded in the source; do not re-label an invented slogan as a heading. Even when creation is requested, do not invent factual claims or present the result as an official PEA motto.

## Input / output contract

- Accept original Thai copy or documents, heading, dates, key points, attached images in specified order, and optional layout choice (1-5) or references. The user may provide all data piecemeal.
- Optional controls may include `layout_choice`, `subject_focus`, `mascot_usage: auto | include | omit`, and `background_direction: auto | cyber | digital | field | awareness | festive | neutral | custom description`.
- Default deliverable: finished portrait high-resolution PNG at 1086x1536 px or corresponding A4-like dimensions; export PDF/PPTX only when asked. For longer content use a coordinated page 2.
- If content has not yet been provided, supply only a template/preview rather than invented news.
- No external connector is required: use user attachments. Additional original-looking background art, PEA Watt-D (when appropriate), and context-appropriate *decorative icons* are allowed, provided they do not tamper with the logo or supplied images, and do not purport to depict an unverified event.
- Keep every layout's upper-left PEA logo, exact header/sub-header and footer, and the purple/gold identity constant; vary hero illustration, card grid, timelines, infographic modules, photo positions, mascot usage, background style, and accent composition.

## Select one of five visual layouts

| Option | Short name | Best use |
| --- | --- | --- |
| 01 | Chiang Mai Classic | PEA news, visits, field photos, general announcements |
| 02 | Digital Operations | Information systems, dashboards, digital services, platforms |
| 03 | Cyber Shield | Cyber awareness, protection guidance, policy, risk review |
| 04 | Enterprise Analytics | System integration, applications, service improvement, verified KPIs |
| 05 | Cyber Ops & Infrastructure | Network operations, SOC, monitoring, communications, fiber, security infrastructure |

See `references/layout-catalog.md` for all five files and detailed visual patterns. Respect an explicit user style choice. Otherwise auto-select the best match, explaining the chosen option briefly. When making a series for a team, rotate appropriate layouts to avoid repetitive composition; never select a mismatched theme solely for variety. If actual source data has no verified KPIs or steps, omit those modules even when a reference example displays them. The four new mockups are *not* ready-to-publish templates because their imagery/text may be synthetic.

## Production workflow

1. Open `references/content-contract.md`, `references/layout-catalog.md`, `references/mascot-background-rules.md`, and `references/quality-checklist.md`. Inspect only the relevant reference images plus `assets/original-newsletter-reference.png` when needed; do not copy placeholder claims.
2. Extract and lock exact user-supplied numbers, dates, identifiers, names, quoted wording, image count and image order. Identify verified source content for each intended block. Record any user-supplied motto verbatim and any explicit current request to create one; without that request, do not generate a motto.
3. Select layout 01-05 based on request and material. Decide whether PEA Watt-D should appear (`include`, `omit`, or `auto`) and define the decorative background direction from the story theme. Plan actual modules: headline, date if known, concise summary, main visual, verified highlights/steps, related information, and attachments. Unused panels should disappear; do not fill with fabricated data.
4. Create or source *separate decorative* hero/backdrop artwork for the selected theme, if useful. Add PEA Watt-D only as a separate decorative layer when appropriate. Do not put the logo or source images through generative image editing. Do not use any entire reference mockup as the final content background because the mockup already contains synthetic writing and imagery.
5. Compose text in true Google Sans, insert supplied images as uncropped `contain` placements, and paste the *exact original logo file* in the upper-left after decorative generation. Add the three protected text strings exactly. The final production file should be text/layout composed, not a single AI-generated image with unreliable spellings/fonts/logos.
6. On 1086x1536 PNG use `python scripts/lock_logo.py input.png output.png` (or `--x`/`--y` for a different but fixed location, with enough clear space) as the final logo-integrity pass. The script never scales or changes pixels. For other dimensions, position the original asset without resizing in an equivalent compositing pipeline.
7. Transcribe all readable final text to `final_transcription.txt` and run `python scripts/audit_copy.py --source content_source.txt --final final_transcription.txt`. Manually compare numerals, especially Thai dates and chart labels. Source should include supplied report text, not numeric data from reference mockups.
8. Visually inspect the exported page: logo exact, all original images represented and uncropped, no synthetic photo passed off as real, mascot usage consistent with brief, background aligned with content but not distracting, correct Thai typography, no fallback fonts, enough contrast, no overflow, all locked terms correct, and no unauthorized motto anywhere (including background art, banners, captions, mascot speech bubbles, or footer). If verification is unavailable, disclose the limitation rather than asserting compliance.
9. Deliver the finished artifact and mention the layout number, mascot decision, and background direction. For team reuse, include any compliance blockers; never misrepresent a preview as a verified production export.

## Style system

- Primary dark purple approximately `#79005E`; secondary purple `#9A6597`; warm gold `#D5A125`; light wash `#F8F3FA`; white background. Adapt lightness for readability, but preserve CI hierarchy.
- Use rounded cards, restrained shadow, clear margins, gold separator rules, a readable title hierarchy, and a curved/wavy brand divider when appropriate. A page can vary its illustration, mascot, and geometry without varying the logo/copy identity.
- Allow neutral contextual icons (shield, lock, terminal, network, server, database, analytics, cloud, monitoring, fiber, warning, gear, celebration/confetti when the story is informal), but no misleading alerts or fabricated brand endorsements. Prefer original vector-style illustrations separate from user attachments. Decorative icons can be placed near headings, never over photos.
- Backgrounds may range from Chiang Mai landmarks, abstract digital networks, cyber shields, data flows, system screens, office/community scenes, or festive internal motifs depending on the subject, but they must remain decorative, subtle, and readable.
- PEA Watt-D can appear as a corner helper, title-side companion, section accent, or footer-side decorative character. Keep clear space around the logo and locked text. Do not let the mascot cover user photos or impersonate a documented person in the event.
- For print, set margins and safe areas; for mobile, keep text legible. Avoid presenting illustrative devices/screens/people/mascots as documentary evidence.

## Assets / references / tools

- `assets/approved-layout-reference.png` = style 01 (the previously approved template); `assets/original-newsletter-reference.png` = source inspiration.
- `assets/layout-02-digital-operations.png`, `assets/layout-03-cyber-shield.png`, `assets/layout-04-enterprise-analytics.png`, and `assets/layout-05-cyber-ops-infrastructure.png` = four additional conceptual layouts, NOT source data.
- `assets/pea-logo-exact-original.png` = protected pixel-original logo extracted from the user-supplied sample.
- `references/layout-catalog.md` = five variants, routing, safety of sample elements.
- `references/mascot-background-rules.md` = rules for using PEA Watt-D and selecting a content-appropriate decorative background.
- `references/content-contract.md` and `assets/content-input-example.md` = incoming information, motto authorization rules, and exactness rules.
- `assets/newsletter-prompt.th.md` = short copy-and-fill prompt; keep identical to the repository entrypoint `prompts/newsletter-prompt.th.md`.
- `references/quality-checklist.md` = preflight QA; `references/CHANGELOG.md` = change history.
- `scripts/lock_logo.py` and `scripts/audit_copy.py` = deterministic pixel/text audits. Test scripts on the target environment before relying on them.

## Example requests

- "Create a PEA newsletter about verifying Industrial Switch and ODF equipment from the attached text/photos; choose layout 05, use a network-infrastructure background, and preserve every date, number, and actual image."
- "Make a Thai cyber safety awareness update in style 03. Include PEA Watt-D as a friendly corner mascot, but do not invent any extra steps."
- "Show the five PEA infographic styles and suggest which one suits an IT dashboard rollout, then build the chosen one with a data-themed background when I send the content."
- "Create an internal fun-news issue and choose the layout automatically. You may use PEA Watt-D and a playful background if it helps the tone, while keeping all supplied photos unchanged."
