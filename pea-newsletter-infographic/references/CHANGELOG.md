# Changelog

## v2.5.1 - 2026-11-17
- Add `layout-01-chiang-mai-classic.jpg`, a 1440x2560 illustrative composition guide with sample copy, flexible image slots, the original logo and a generated abstract purple/gold background. Compose text with verified Thai-capable Prompt because Google Sans is unavailable.
- Vary backgrounds by story; no fixed Doi Suthep, mountain, temple or landmark requirement. Synchronize both prompts and QA.

## v2.5.0 - 2026-11-17
- Update packaging to the current JPG/JPEG layout references and remove the retired original newsletter reference from required assets.
- Add optional `sub_header` for the department line immediately below the unchanged top header. Omitted or blank values retain the original information systems and cybersecurity department name.
- Preserve the resolved wording exactly; synchronize both Thai prompts, intake form, content contract and QA.
- Add `--sub-header` to copy auditing, preserving default behavior for existing callers.

## v2.4.5 - 2026-11-17
- Prefer Thai-capable Google Sans and permit verified Thai-capable Google Prompt as a disclosed fallback when Google Sans is unavailable.
- Recheck typography and line breaks after fallback; report a blocker if neither font is available.

## v2.4.4 - 2026-11-17
- Repair helper APIs and current JPEG contract tests; replace obsolete PNG, no-crop and version-pinned assertions.
- Reject corrupt/truncated, non-RGB, misnamed and rotated output; preserve input files during logo export.
- Check required copy appears exactly once; keep CLI and callable audits aligned.
- Update validation evidence to the repaired suite and document remaining visual/factual QA limits.

## v2.4.3 - 2026-11-16
- Add the user-approved activity-news photo-grid direction and latest reference image.
- Bundle the approved transparent running Watt-D derivative with its original, preserving provenance and white character details.
- Improve Thai paragraph flow and word-aware line breaks; synchronize prompts and QA.

## v2.4.2 - 2026-11-16
- Explicitly allow cropping news images and supporting illustrations to emphasize focal subjects and compose attractive collages or bento grids. Preserve essential subjects, text, context, and aspect ratio; use another frame or contain placement when necessary.
- Keep logo cropping prohibited and source image files unchanged. Synchronize prompts, layout guidance, and QA.

## v2.4.1 - 2026-11-16
- Allow proportional logo downscaling to suit the infographic dimensions and composition while preserving original colors, details, clear space, and complete visibility.
- Add optional `--scale` to the logo helper; reject enlargement, invalid scales, and placements that crop the logo. Keep the source asset unchanged.
- Synchronize the skill, Thai prompts, content contract, and QA checklist.

## v2.4.0 - 2026-11-12
- Add support for bento-grid image layouts with mixed tile sizes for attached photos.
- Allow crop-to-fill, scaling, zooming, and repositioning of attached images inside layout frames so photos can fully fill their grid cells without aspect-ratio gaps, while preserving important subjects and avoiding distortion.
- Allow generated supporting illustrations, icons, and background filler graphics in empty areas so the infographic does not feel overly blank.
- Keep one final JPG/JPEG at 1440x2560 portrait, all-image inclusion, and the explicit-only motto rule.

## v2.3.2 - 2026-11-11
- Strengthen the art-direction rule so the skill actively creates story-matched backgrounds, hero graphics, and decorative elements instead of leaving large plain white empty areas.
- Add guidance for thematic background generation, richer page filling, and QA checks against overly blank layouts.
- Keep the final deliverable as one JPG/JPEG at 1440x2560 portrait.

## v2.3.1 - 2026-11-11
- Change the required final output format from PNG to JPG/JPEG to reduce file size.
- Keep the fixed portrait size at 1440x2560 and the single-image rule.
- Add JPEG-specific output guidance: opaque background, readability check after compression, and JPEG validation.

## v2.3.0 - 2026-11-04
- Fix the newsletter deliverable to exactly one static PNG at 1440x2560 pixels in portrait orientation.

## v2.2.0 - 2026-11-04
- Accept any number of supplied news images.
- Require a single combined output image rather than multiple pages.

## v2.1.1 - 2026-11-04
- Prohibit newly invented mottos, slogans, and taglines unless explicitly requested.

## v2.1 - 2026-11-03
- Add optional PEA Watt-D mascot usage and theme-based background rules.
