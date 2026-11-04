# One image, all supplied news images

Apply this guide to every layout. This is a production contract, not an automatic rendering engine.

## 1. Inventory before layout

Accept any number of news images, including zero, without a template-defined image-count cap. Do not impose the three/four-photo slots visible in mockups. Keep an internal ordered manifest with `image_id`, `filename`, `role`, `required`, `exclusion_reason`, source dimensions and `placement`. Use a distinct ID for each supplied occurrence even when filenames or bytes repeat. Only explicit user selection can exclude or deduplicate news images. Identify logo, mascot and style references separately; never use that classification to hide an omission. Report unavailable or unreadable inputs.

Do not add the manifest's counts, IDs or filenames to the published news copy unless requested. They are verification data, not new story facts.

## 2. Plan a single canvas

Use one continuous infographic with a single protected header/sub-header and footer. A4-like portrait is only a starting preference. Set width and height from real copy and source-image dimensions, legibility needs and renderer capacity; there is no fixed maximum photo count in the template.

For small sets, use a prominent hero and supporting cards. For large sets, use an adaptive grid, gallery, filmstrip or collage across continuous sections. No fixed numeric thresholds are required. Do not create artificial duplicate image slots when no photos were supplied. Do not make a long strip of miniature independent pages with repeated headers.

If crowded: remove unused panels and nonessential decoration, condense repetitive prose without losing meaning/locked data, reflow the gallery, then increase canvas dimensions. Never crop a source photo, remove a required fact, invent a motto, hide an image under another, or make screenshots illegible just to fit a fixed rectangle. Keep meaningful details readable at native size; explain that a long export may need scrolling or zooming on a phone.

## 3. Preserve originals during composition

Place source photographs and screenshots directly from the original files with proportional contain fitting and padding. Keep the entire rectangle visible; frame rounding must not clip its corners. Do not recolor, retouch, remove backgrounds, upscale with AI, add overlays or regenerate news images. Decorative layers and Watt-D remain separate.

Keep the protected logo at native pixel dimensions unless the user supplies a different authorized asset. Reserve adequate space based on the actual file dimensions. The current `lock_logo.py` accepts only a 1086x1536 canvas; it is not an arbitrary-size renderer. Use a verified compositing path for other sizes instead of forcing the whole design into the helper's fixed dimensions. Never truncate a logo to fit it.

## 4. Capacity is not infinite

A rule with no image-count cap does not remove upload, attachment-access, memory, pixel, font or export limits. Check these before rendering and account for source aspect ratios. Internal batch processing or temporary tiles may be used only if all results are composed into one final image. Do not deliver those tiles separately.

If the current environment cannot produce the complete readable single image, report the exact blocker and do not claim success. Do not silently choose a subset, split pages, crop content, or bypass tool safety/resource limits. Any changed scope requires a later explicit instruction, not an automatic fallback.

## 5. Export and verify

Deliver exactly one final static PNG file, with one frame. APNG animations, GIFs, slide decks, multiple pages, ZIPs of image parts and PDFs are not substitutes for that result. Preview assets are working material, not extra final deliverables.

Check each required manifest ID against the actual layout, all placements against canvas bounds, and every source corner for clipping. Counts alone cannot catch a duplicate replacing a missing image. Inspect text at native resolution and the whole canvas for hierarchy and overlaps. Verify protected copy, source numerals, true Google Sans, logo integrity, original photos and the motto gate independently. Report included/required image counts and final dimensions only after these checks.

## 6. Acceptance scenarios

| Input | Expected result |
| --- | --- |
| No news photos | One source-grounded image; no invented event photography |
| One photo | One image containing the full original photo |
| Several photos with mixed aspect ratios | All required IDs in one contain-fit layout |
| Many photos, including batches | One expanded coherent image; no silent cap or pagination |
| Same filename/duplicate occurrence | Preserve occurrences unless exclusion is authorized |
| Explicit user selection | Include that selection and document exclusions internally |
| Source screenshot contains small labels | Size for readability; do not turn it into an unreadable thumbnail |
| A reference contains sample KPIs/motto | Do not copy them as real copy or authorization |
| Capacity or asset/font blocker | Report the blocker; never label a partial/split result complete |
