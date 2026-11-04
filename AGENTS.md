# Repository workflow

Read `pea-newsletter-infographic/SKILL.md` before authoring newsletters. Read its
referenced content, mascot/background, layout, and QA rules as needed. The Thai
prompt at `prompts/newsletter-prompt.th.md` is a copy-and-paste entrypoint for
assistants that do not load skills. Do not claim native skill execution on a host
that only reads plain text.

Keep the canonical skill folder intact. Keep the version, short prompt and QA contract consistent with every authorized change. Do not treat the illustrative template dates,
percentages, scenes, logos, or people as event evidence.

Do not regenerate the logo or user photos. Use only verified original Watt-D
artwork; without it, omit in auto mode or report a missing asset in include mode.
Do not distribute fonts or silently use a fallback. Never call an unverified
font or generative rendering Google Sans-compliant.

The helper scripts are not a complete renderer. Read `docs/validation-report.md`
for tested behavior and gaps. Do not automatically upload inputs, publish assets,
create remote branches, or change repository visibility. Publishing requires an
explicit user request and an authenticated, authorized write channel.

For v2.3.0, accept any number of required news images without a template-defined
cap and produce exactly one final static PNG at 1440x2560 px (width x height), portrait 9:16. Do not enlarge the canvas or swap dimensions. Real tool limits and fixed-size readability still apply.
Never solve overcrowding by pagination or omissions. Keep the explicit-only
motto gate and both short-prompt copies synchronized. Run instruction-contract
checks and report what they do not verify. Never substitute an older local logo
for the asset currently maintained by the repository owner.
