# Layout 01 design reference

- Final asset: `pea-newsletter-infographic/assets/layout-01-chiang-mai-classic.jpg`, RGB JPEG, 1440 × 2560 px.
- Generated the decorative background with the built-in image generation tool; composed the original repository logo, text and photo placeholders separately. No user photos were regenerated. No mascot is used.
- Used installed Google Prompt Regular/SemiBold after checking Thai cmap coverage; Google Sans was unavailable. Font files are not bundled. Browser rendering preserves Thai shaping.
- This is an illustrative layout, not news evidence. The six example image slots do not limit input image count. Replace sample copy and slots with each story's supplied facts and images; resolve the department through `sub_header`.
- Backgrounds should vary with the story. Chiang Mai Classic names the composition style and does not require a temple, mountain, Doi Suthep or other landmark.
- Visually checked Thai text, branding, placeholder labels and footer. `validate_output.py`, the 53-test suite and ZIP packaging passed.

## Final background prompt

Create a premium editorial decorative background for a Thai corporate newsletter reference, tall portrait 9:16. NO TEXT, NO LETTERS, NO NUMBERS, NO LOGO, NO MASCOT, NO PEOPLE. Topic-neutral elegant purple and gold design, adaptable to general activity news. Soft pale lavender background #F8F3FA, translucent flowing silk ribbon arcs in lavender and plum, fine warm gold contour lines, tiny subtle geometric dots. NO mountains, NO temples, NO recognizable geographic landmarks, NO cityscape, NO specific technology icons. Upper right from 15 to 38 percent has a beautiful layered sculptural abstract lavender paper-ribbon flourish with warm gold edges, with depth and soft shadow. Top 12 percent and upper left pale and quiet for official header and headline to be added separately. Center 40 to 91 percent predominantly very light lavender with fine curved contour patterns along edges; intentionally light for separate photo-grid composition. Bottom 8 percent deep plum #79005E gracefully curved footer ribbon with thin gold edge. No frames, no cards, no writing. Polished rich yet restrained print editorial visual, no empty white zones.
