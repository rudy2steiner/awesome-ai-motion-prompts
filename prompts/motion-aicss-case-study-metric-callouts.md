# Customer Case Study Metrics

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/case-study-metric-callouts](https://www.aicssanimations.com/directory/Motion-Prompts/case-study-metric-callouts)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second customer case study promo in an editorial magazine style on deep green: a finance lead's quote sets line by line in large serif italics beside an illustrated portrait, then three metric callouts count up, each with the baseline that makes it believable.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Brindle, accounts payable automation (fictional). Wordmark: "brindle". Line: "Accounts payable on autopilot".
- Customer: Halden Freight, a regional logistics company (fictional). Wordmark "HALDEN FREIGHT".
- Person: Priya Natarajan, VP Finance, Halden Freight (fictional).
- Quote, with these line breaks: "We used to close the books in nine days." / "Now it's three and a half, and nobody" / "stays late to do it." Underline "three and a half".
- Context line: "Halden Freight moved accounts payable to Brindle in March 2026."
- Metrics (number · label · baseline):
  "61%" · "faster month-end close" · "9 days → 3.5 days"
  "1,240" · "invoices matched automatically each week" · "88% of the 1,410 received"
  "$412K" · "in duplicate payments caught in year one" · "37 duplicates stopped before payment"
- Label: "CUSTOMER STORY". Link: "Read Halden's story →".
- Length: 10 seconds.
</inputs>

<direction>
- Look: a feature spread from a good business magazine, set on deep green: a large italic pull quote, a confident flat portrait, a row of metrics with thin rules and generous air. The customer is the hero and the vendor signs off small at the bottom. Calm, slow and assured: things set into place like type on a page, never fly.
- Palette: background #0F2620 with a faint seeded paper grain at 3% (#163329 specks) and a soft 6% lighter pool behind the quote; cream #F3EBDC (main text, numbers); sage #9DB3A6 (secondary text, hairlines at 40%); saffron #E9A93B (the quote mark, underline, label, rule accents, link); rust #C9603A (one earring, the brindle mark's dot). Portrait: saffron disc #E9A93B with halftone dots #D18F27; blazer olive #4E5B3A with lapel shadows #3E492E; top cream #F3EBDC; skin #6B4430 with a cheek facet #7E5238 and a nose facet #5C3A29; hair #17120F; lips #A9472E; glasses cream #F3EBDC.
- Type: Newsreader for the editorial voice: the quote in 400 italic 58px with a 72px line height, the quote mark in 500 180px, the name in 500 26px, the metrics in 500 128px; Schibsted Grotesk 400, 500, 600 and 700 for labels (15px tracked 0.2em for "CUSTOMER STORY", 20px 500 for metric labels, 16–18px 400 for baselines and context, 17px 600 for the link, the Halden wordmark 700 18px tracked 0.18em). Set every count-up number in fixed-width digit slots so nothing shifts while it counts.
- Layout:
  - Top: "CUSTOMER STORY" in saffron at x 120, baseline y 112; a 1px sage rule from x 336 to 1500 at y 107; at the right, the Halden mark (three rounded bars 30 × 8 stacked like containers, each offset 6px right of the one below, cream) and "HALDEN FREIGHT", right-aligned to x 1800 at baseline y 114.
  - Portrait: a 380px saffron disc centered at (330, 400). Inside, a flat editorial bust: a sleek black bob with a side part, a softly angled face with the cheek and nose facets, relaxed almond eyes drawn as short dark arcs behind thin round cream glasses (2.5px), calm lips with a slight smile, a small rust stud earring, a cream top and an olive blazer with lapels. The shoulders break out of the bottom of the disc by 30px, which is the only thing that crosses its edge. The halftone dots (a 10px grid) fade from 60% at the disc's top-left to 0 at its bottom-right.
  - Under the portrait, centered on x 330: "Priya Natarajan" in cream at baseline y 664; "VP Finance, Halden Freight" Schibsted 400 17px sage at y 692.
  - Quote: the saffron mark at x 600, baseline y 330, hanging left of the text; the three lines at x 680, baselines y 300, 372 and 444, cream; the underline under "three and a half" is a 4px saffron bar 12px under the baseline. The context line Schibsted 400 18px sage at x 680, baseline y 512.
  - Metrics: three columns starting at x 120, 700 and 1280, each 480 wide. Each has a rule at y 750 (a 48px 2px saffron segment, then a 1px sage line to the column's end), the number at baseline y 886, the label in cream at y 928 and the baseline line in sage at y 956.
  - Sign-off: the brindle mark (a 22px saffron square rotated 45° with a rust dot at its center) and "brindle" in Newsreader 500 italic 30px cream at x 120, baseline y 1036, then "Accounts payable on autopilot" Schibsted 400 17px sage after it; the link in saffron right-aligned to x 1800 on the same baseline.
- Motion: text sets line by line: each line sits in a mask and rises from 100% below to 0 on easeOutQuart over 0.8 s. Rules draw left to right on easeInOutCubic. The portrait assembles in layers (disc scales from 0.92 and fades, then blazer, face, hair, glasses, each rising 12px and fading on easeOutCubic, 0.12 s apart). Numbers count with easeOutExpo over 1.2 s; "$412K" counts in whole thousands; "1,240" keeps its comma from 1,000 up.
- Camera: a 1.5% push-in toward the quote from 0 to 8.8 s on easeInOutSine, then still.
- Premium: a quote that sounds like a person; numbers with units, time frames and baselines; quiet, exact typography with real hierarchy; one disciplined accent. Cheap: stock-photo headshots, five-star rating rows, logo walls, bouncing numbers, gradient text, a quote in a speech bubble, a photo-realistic face.
- Banned: photos, real people, real company names, logos and UI copied from existing products, star ratings, speech bubbles, gradient text, glows, confetti, purple, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: the green page; "CUSTOMER STORY" rises (0.1 s) and its rule draws (0.2–0.6 s); the Halden wordmark fades in (0.35–0.6 s).
- 0.4–1.4s: the portrait assembles: disc (0.4 s), blazer and top (0.6 s), face (0.72 s), hair (0.84 s), glasses and earring (0.96 s); the halftone fades in last (1.0–1.4 s).
- 0.9–2.2s: the quote mark fades and drops 10px into place (0.9 s); the quote's three lines rise in at 1.0, 1.25 and 1.5 s.
- 2.2–2.9s: the underline draws under "three and a half" (2.2–2.7 s); the name and title rise in (2.4–2.9 s); the context line fades in (2.6–2.9 s).
- 3.0–5.2s: the three metric rules draw (3.0–3.5 s, 0.1 s apart); the numbers count up from 3.2, 3.5 and 3.8 s, each over 1.2 s; each label rises 0.2 s after its count starts; the baselines fade in 4.6–5.2 s, 0.15 s apart.
- 5.3–5.9s: the sign-off rises in: the brindle mark and wordmark, the line, then the link.
- 6.0s: the hero frame: label, Halden wordmark, the full portrait with name and title, the complete quote with its underline and context line, all three metrics at their final values with labels and baselines, and the sign-off.
- 6.0–7.4s: hold while the push-in continues.
- 7.4–7.8s: the link's arrow nudges 6px right and back once (easeInOutSine).
- 7.8–10.0s: hold on the final frame; the push-in stops at 8.8 s.
For other lengths, stretch the gap between the quote and the metrics and the final hold; keep each line's 0.8 s rise, the 1.2 s counts and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: the portrait and both wordmarks are inline SVG, the grain is generated once at load from a seeded PRNG, and the halftone is a CSS radial-gradient pattern under a mask.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face (Newsreader 400 italic, 500 and 500 italic; Schibsted Grotesk 400, 500, 600 and 700) before defining window.seek.
- Engine: HTML/CSS. Absolutely positioned DOM elements on the stage with inline SVG for the portrait and marks; seek(t) writes every transform, opacity, width, clip-path and text content as inline styles computed from t. No CSS transitions, CSS animations or Web Animations API. Line masks are overflow-hidden wrappers whose child's translateY comes from t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the quote keeps its three line breaks and none of its lines runs past x 1800; the underline sits exactly under "three and a half"; the portrait reads as a person in glasses and a blazer, only the shoulders cross the disc's edge, and it looks illustrated, not photographic; the counts end on exactly 61%, 1,240 and $412K without their widths jumping; 61% matches 9 days to 3.5 days and 1,240 is 88% of 1,410; the 6.0 s frame shows every element listed above; and the final frame matches it at rest. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
