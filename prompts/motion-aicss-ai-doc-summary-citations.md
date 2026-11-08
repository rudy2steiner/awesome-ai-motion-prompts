# AI Summary With Citations

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/ai-doc-summary-citations](https://www.aicssanimations.com/directory/Motion-Prompts/ai-doc-summary-citations)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second AI summary demo for a contract reader: an ivory document sits on the left of a dark app, the summary streams into the right panel, and then each numbered citation chip lights up in coral and draws a line across the gutter to the exact passage it came from, which highlights in the document; a follow-up question gets a cited answer.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Parsewell (fictional), an AI reader for contracts. File: "Halden–Corvo MSA.pdf · 12 pages".
- Document: "MASTER SERVICES AGREEMENT" between Halden Freight Ltd. and Corvo Logistics, Inc. (both fictional), dated February 12, 2026. Passages, word for word:
  [p. 3] "4. Term and Renewal. 4.1 This Agreement begins on March 1, 2026 and continues for an initial term of twenty-four (24) months. 4.2 It renews automatically for successive twelve (12) month terms unless either party gives written notice of non-renewal at least ninety (90) days before the end of the then-current term."
  [p. 5] "7. Fees and Payment. 7.2 Invoices are payable within forty-five (45) days of receipt. Undisputed amounts not paid when due accrue interest at one percent (1.0%) per month."
  [p. 6] "9. Limitation of Liability. 9.1 Except for breaches of Section 11 (Confidentiality), each party's total liability under this Agreement is capped at the fees paid in the twelve (12) months before the claim."
  [p. 8] "12. Termination. 12.3 Either party may terminate this Agreement for convenience on sixty (60) days' written notice, subject to payment for services already performed."
- Summary ("4 key terms · from 12 pages"), each with its chip:
  [1] "Runs 24 months from March 1, 2026, then renews yearly unless cancelled 90 days ahead."
  [2] "Invoices are due in 45 days; late balances accrue 1% a month."
  [3] "Liability is capped at 12 months of fees, except confidentiality breaches."
  [4] "Either side can exit on 60 days' notice, paying for work done."
- Deadline card: "Renewal notice deadline" · "Dec 1, 2027" · chip [1] · ghost button "Add to calendar" (the first term ends Feb 29, 2028; 90 days earlier is Dec 1, 2027).
- Follow-up: "Does the cap cover data breaches?" Answer: "No. Confidentiality breaches are excluded from the cap." with chip [3].
- Length: 10 seconds.
</inputs>

<direction>
- Look: a reading room at night. A warm sheet of paper on a deep teal-ink desk, and next to it a calm dark panel where the summary arrives. The only saturated color is coral, and it means exactly one thing: "this claim comes from here". Every connection is visible, precise and quiet.
- Palette. Desk and app background #0F1E1F; panel #152A2B with a 1px #234143 border; panel text #EEF3F0, body #DCE6E3, secondary #8FA9A6, tertiary #5E7A77. Paper #F5F0E6 with ink #22201C, secondary #6D665A and rules #CFC6B5; paper shadow 0 30px 60px rgba(0,0,0,0.45). Coral #FF7A59 for chips, connector lines and highlights (highlight fill: coral at 26% while active, 14% at rest), coral deep #E35F3F for the active chip's ring. One quiet mint #7FD3C4 for the "Summarize" button's done check. No other hues.
- Top bar y 0–72: an original Parsewell mark at (40, 22), a 28px coral rounded square with two short horizontal notches cut into its right side, "Parsewell" in Figtree 600 20px #EEF3F0, the file name in 15px secondary centered on the document (x 492), and a "Summarize" button at (1000, 16), 160×40, #234143 fill, which shows a mint check once pressed.
- Document: a paper sheet at x 72–912, y 104–1040 (840×936), radius 6. Inside, 64px margins: the title "MASTER SERVICES AGREEMENT" in Source Serif 4 600 22px tracked 0.06em at y 168; the parties line "Halden Freight Ltd. and Corvo Logistics, Inc. · February 12, 2026" in Source Serif 4 italic 15px secondary at y 200; then the four passages as an excerpt view: each starts with its section heading in Source Serif 4 600 17px followed by the text in Source Serif 4 400 17px with 28px line height, set ragged-right to 712px wide. Between passages, a fold marker: a dashed #CFC6B5 rule with "· · ·" centered on it, 40px tall. A page marker ("p. 3", "p. 5", "p. 6", "p. 8") sits in the right margin at each passage's first line in Figtree 500 12px #6D665A. Lay the passages out from y 240 so the last ends by y 1000.
- Summary panel x 1000–1848, y 104–1040, radius 18. Header "Summary" in Figtree 600 26px at (1040, 160); "4 key terms · from 12 pages" in 15px secondary under it. Four rows from y 236, 104px apart: a chip at x 1040 (the row's left edge, vertically centered on the first line), the sentence in Figtree 400 21px with 32px line height from x 1088, wrapped to 700px. Deadline card at y 676: 768×132, #1A3334 fill, radius 14: "Renewal notice deadline" in 14px secondary caps tracked 0.08em, "Dec 1, 2027" in Figtree 600 34px #EEF3F0, its chip [1] at the card's left, "Add to calendar" ghost button (1px #234143, 15px) at the right. Follow-up area at y 836–1016: the question as a small right-aligned bubble at y 836 (#234143, 17px, 40px tall), the answer on one line at y 904 in 19px body with its chip at x 1040, and a composer line "Ask about this contract…" at y 996 in 16px tertiary above a 1px #234143 rule.
- Chips: 30×26, radius 7, the number in Figtree 600 14px. Unlit: 1.5px coral outline, coral number. Lit: coral fill, #0F1E1F number, plus a 3px coral-deep ring for its active moment.
- Connectors: a cubic curve from the chip's left edge (x 1040) to the right end of the passage's last highlighted line in the document, leaving and arriving horizontally (control points 120px out on each side), crossing the gutter between paper and panel. 2px coral while active, with a 4px dot at each end; it draws along its length in 0.35 s on easeInOutCubic. At rest it relaxes to 1.5px at 50% opacity. When several rest at once they never cross: route them in order, top to bottom.
- Highlights: the cited words sit on a coral tint drawn as one rounded rect per line (padding 2px × 4px, radius 3), sweeping left to right across each line in 0.1 s, lines in order. Cite only the exact clause that backs the claim (4.1 and 4.2 for [1], 7.2 for [2], 9.1 for [3], 12.3 for [4]). A 3px coral bar appears in the paper's left margin beside each cited passage.
- Streaming: the summary arrives word by word at 24 words per second, each word fading in over 0.12 s with a 3px rise; no cursor. A sentence's chip appears unlit (scale 0.8→1, 0.15 s) as its last word lands. The header's count and the deadline card follow the last sentence.
- Type: Source Serif 4 400 / 400 italic / 600 for the document; Figtree 400 / 500 / 600 for all UI. Tabular figures for dates and amounts.
- Premium: a believable contract set like a real legal document, a summary genuinely shorter than its source, citations that land on the exact clause, connectors that are thin, ordered and never tangled, one accent color with one meaning, a derived fact (the notice deadline) that proves the reading. Cheap: glowing laser beams, highlights that cover whole paragraphs, a summary that just repeats the text, chips that bounce, a typing cursor racing, neon on black, gradients.
- Banned: real company names, logos and UI copied from existing products; law firm or court names; glow, bloom or neon; any second accent hue for citations; animated gradient borders; sparkles or magic icons; crossing connectors; lorem ipsum; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: the app fades up from #0F1E1F (0.0–0.4 s); the document is already laid out on its sheet; the summary panel shows only its header area and "Summarize" waiting. The button presses at 0.6 s (dips to 0.95, 0.08 s) and shows its mint check.
- 0.85–3.35s: the four summary sentences stream in, one after another (each about 0.55 s, with a 0.08 s gap), each chip appearing unlit as its sentence finishes; "4 key terms · from 12 pages" fades in at 0.85 s.
- 3.25–3.6s: the deadline card rises 10px and fades in with its unlit chip.
- 3.7–5.8s: the chips light in turn: [1] at 3.7 s (its connector draws to 4.2, its highlight sweeps, and the deadline card's chip lights with it), [2] at 4.25 s, [3] at 4.8 s, [4] at 5.35 s. As each new chip lights, the previous connection settles to its rest state over 0.25 s.
- 5.8–6.3s: the 6.0 s frame is the hero: the whole document with all four passages highlighted and margin bars, all four summary rows with lit chips, four ordered connectors across the gutter (the [4] connector still at full strength), and the deadline card.
- 6.4–7.25s: the follow-up question types into the composer at 40 characters per second, then rises into a bubble (7.2 s).
- 7.3–8.2s: the answer streams in (7.35–7.8 s); its chip [3] lights at 7.9 s, the [3] connector and highlight brighten back to full while the others stay at rest.
- 8.2–10.0s: hold on the full page: document, summary, deadline card, question and cited answer.
For other lengths, keep the streaming speed and one lit chip at a time, and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: everything is drawn in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no SMIL, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face, weight and style before defining window.seek.
- Engine: one inline SVG with a 1920×1080 viewBox. Lay out the document and summary text once at load (wrap lines by measuring words with getComputedTextLength on hidden text elements), record each cited span's per-line boxes and each chip's position, and build the connector paths from those measurements; seek then only sets opacity, transforms, stroke-dashoffset and highlight widths from t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that every passage is word for word as given and fits the sheet, each highlight covers exactly its clause and nothing more, each connector starts at its chip and ends at its own passage, connectors never cross, the summary's numbers match the document (24, 90, 45, 1%, 12, 60), the deadline reads Dec 1, 2027, and coral is the only accent. At 2.0 s two summary sentences are in; at 4.5 s chip [2] is lit with its connector; the 6.0 s frame shows all four connections and the deadline card; the final frame shows the cited answer with [3] lit. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
