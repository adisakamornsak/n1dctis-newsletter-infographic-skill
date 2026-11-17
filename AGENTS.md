# Repository workflow

Read `pea-newsletter-infographic/SKILL.md` before authoring newsletters. Read its
referenced content, mascot/background, layout, and QA rules as needed. The Thai
prompt at `prompts/newsletter-prompt.th.md` is a copy-and-paste entrypoint for
assistants that do not load skills. Do not claim native skill execution on a host
that only reads plain text.

Keep the canonical skill folder intact. Keep the version, short prompt and QA contract consistent with every authorized change. Do not treat the illustrative template dates,
percentages, scenes, logos, or people as event evidence.

Do not regenerate the logo or user photos. Use verified original Watt-D artwork or the explicitly user-approved transparent
cutout bundled with this skill; without it, omit in auto mode or report a missing asset in include mode.
Do not distribute fonts. Prefer verified Thai-capable Google Sans; use verified Thai-capable Google Prompt only when Google Sans is unavailable, and disclose this fallback. Never claim Prompt is Google Sans or silently use another font.

The Plugin contains instructions and assets, not a renderer. Use the version synced by the Plugin system; do not require per-request GitHub checks or a local runtime. Read `docs/validation-report.md` for tested behavior and gaps. Do not automatically upload inputs, publish assets,
create remote branches, or change repository visibility. Publishing requires an
explicit user request and an authenticated, authorized write channel.

For v2.4.0, accept any number of required news images without a template-defined cap and produce exactly one final JPG/JPEG at 1440x2560 px, portrait. Bento-grid photo layouts may crop-to-fill, scale, zoom and reposition images while preserving important subjects and avoiding distortion. Generate story-matched backgrounds and supporting visuals to avoid excessive plain white empty areas. Never solve overcrowding by pagination or omissions. Keep the explicit-only motto gate and both short-prompt copies synchronized. Never substitute an older local logo for the asset currently maintained by the repository owner.

For v3.0.0, maintain the canonical `pea-newsletter-infographic/` folder and rebuild the tracked portable Plugin copy with `npm run build:plugin` after every skill or asset change. Check it with `npm test` and `npm run check:plugin`. End users must not need Node.js, Git, a terminal or a local installer. Do not hand-edit the generated Plugin skill copy.
