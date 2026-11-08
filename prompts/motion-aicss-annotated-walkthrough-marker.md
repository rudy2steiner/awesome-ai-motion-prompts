# Annotated Product Walkthrough

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/annotated-walkthrough-marker](https://www.aicssanimations.com/directory/Motion-Prompts/annotated-walkthrough-marker)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second product walkthrough in the marked-up screenshot style: a field-service dispatch app sits on a slate desk while a red marker circles a new job, the job drags onto a technician's day, and arrows, a double underline, a highlighter swipe and handwritten notes in the margins explain what just happened.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Wrenfield (fictional), a dispatch board for heating and plumbing crews. Date on the board: "Tue, Oct 21". Header stats: "23 jobs · 4 techs".
- Unassigned jobs (title · address · type · length · note): "Leaking water heater" · 412 Birch Ln · Repair · 1.5 h · "Called 7:42"; "AC tune-up" · 88 Orchard Ct · Maintenance · 1 h; "Thermostat install" · 1290 Lake Rd · Install · 2 h.
- Technicians (jobs before → after): Tomás Reyes 5 → 6, Aiko Brennan 5, Sam Whitlock 5, Priya Nair 5. Tomás has a free gap from 10:30 to 12:00.
- Summary cards (before → after): Drive time 4 h 12 m → 3 h 51 m; Miles 142 → 131 (pill "−11 mi"); On-time arrivals 96%; Jobs scheduled 20 / 23 → 21 / 23.
- Chip on the dropped job: "ETA 10:36 sent".
- Handwritten notes: "urgent one, / called 7:42" · "re-routed the whole day" · "customer gets a live ETA" · tagline "One drag. / Whole day / planned."
- Sign-off: Wrenfield wordmark and "Dispatch for field-service teams".
- Length: 10 seconds.
</inputs>

<direction>
- Look: a clean product screenshot laid on a desk and marked up by someone who knows it well, with a single red marker and one yellow highlighter. The UI is crisp and untouched; the marks are confident, slightly imperfect and few. Notes live in the margins around the screenshot, where they can be read, and reach in with arrows.
- Palette. Desk: #E3E7EB with a dot grid of 2px #C9D0D7 dots every 28px. Screenshot: app white #FFFFFF, panels #F7F8FA, hairlines #E3E6EA, ink #18202B (text, the app's buttons and logo), secondary #5D6774, tertiary #98A1AC. Job types: Install fill #D5ECEE with text #0B6A73, Repair fill #FCE3CB with text #96500F, Maintenance fill #E0E9D3 with text #47672A. Marker red #E0402A (every stroke and note), highlighter #FFD84A at 65% with multiply blending. Shadow under the screenshot: rgba(24,32,43,0.18), 30px blur, 14px down. Nothing else: no gradients, no glow.
- Layout: the screenshot is 1400×790 at x 260–1660, y 150–940, radius 12, leaving margins of 260px left and right, 150px above and 140px below for the notes.
- The app, in frame pixels. Top bar y 150–206 with a hairline below: at x 284 a 28px rounded ink square holding a white bold "W", "Wrenfield" in 20px 600 beside it, the date "Tue, Oct 21" with two 16px chevrons centered at x 960, and "23 jobs · 4 techs" in 15px secondary at the right edge (x 1636, right-aligned).
- Left panel x 260–540 (#F7F8FA, hairline right edge): heading "Unassigned · 3" in 14px 600 at (276, 236); three cards 248×84 at x 276, y 250 / 346 / 442, white with a 1px hairline and radius 8, each with the title in 15px 600, the address in 13px secondary, a type chip (12px, in its type colors) and the length at the right, and "Called 7:42" in 12px #96500F on the first. At the bottom of the panel, a legend of the three type chips at y 900.
- Board x 556–1644: technician column x 556–696 (each row: a 28px initials circle and the name in 14px 500 with "5 jobs" in 12px tertiary under it); time grid x 696–1644 for 8 a.m. to 5 p.m. (9 hours, 105.3px per hour), hour labels "8a 9a 10a 11a 12p 1p 2p 3p 4p 5p" in 12px tertiary at y 236, dashed hairlines at each hour. Four rows of 104px from y 256 to 672. Job blocks inset 10px top and bottom, radius 6, type fill with the job's short name in 13px 600 and its time in 12px. Give every technician five plausible blocks with gaps for driving; Tomás's row is empty from 10:30 to 12:00 (x 959–1117).
- Summary row y 704–824: four cards 260×120 from x 556, 16px apart, each with a 13px secondary label and a 30px 600 value; the Miles card is the second (x 832–1092).
- Type: IBM Plex Sans 400 / 500 / 600 for the UI, with tabular figures for numbers. Caveat 700 for every handwritten note, 44px, and the tagline at 56px. Wordmark in IBM Plex Sans 700, 28px; its line in IBM Plex Sans 400, 20px, #5D6774.
- How marks are drawn: every mark is a path built from its ideal shape (ellipse, arc, line) sampled every 4px and pushed off course by seeded low-frequency noise of 1.5–3px, so no two are alike and none is geometric. Marker strokes are 6px with round caps and a pressure profile (4px at the start, 6px through the middle, 5px at the end) built as a filled outline, and an SVG turbulence and displacement filter (scale 1.2) roughens their edges very slightly. Each stroke reveals along its length like a pen moving: easeInOutSine within the stroke, at 900–1400px per second, with a 0.06 s lift between strokes. Once drawn, a mark never moves or boils.
- The shapes. Circles are loose ellipses that start at about 200°, travel 380° so the end overshoots the start, and shrink 5% toward the end so the loop doesn't close. Arrows are a curved shaft then two head strokes 22px long at ±28°, drawn after the shaft in 0.08 s each. Underlines are two strokes, the second 7px lower, a little shorter and tilted 1°. The highlighter is one 30px band with flat, slightly angled ends, drawn left to right in 0.35 s, sitting behind the text it marks.
- Handwritten notes: Caveat glyphs appear in writing order at 16 characters per second, each fading in over 0.05 s with a 2px rise, as the pen reaches it. Each note is rotated −2° to −5°, with a fixed seeded baseline wobble of ±2px per word. Notes sit only in the margins or in clear space, never over UI text.
- The drag: the "Leaking water heater" card lifts (shadow deepens to 0 12px 24px, rotates 2°), travels on a smooth arc to Tomás's gap in 0.8 s on easeInOutCubic, drops with a 0.15 s settle (scale 1.03→1) and becomes a Repair block reading "Water heater · 10:30–12:00". Its slot in the list becomes a dashed outline with "Assigned · Tomás R." in 13px tertiary, and the heading changes to "Unassigned · 2". A small original grabbing-hand cursor (drawn as one SVG path, white with an ink outline) carries the card and leaves when it drops.
- The UI's own changes are quick and plain: numbers count in 0.5 s on easeOutCubic, the "−11 mi" pill fades in, Tomás's count changes to "6 jobs", the "ETA 10:36 sent" chip (11px, ink on white, with a small check) pops in hanging from the block's top-right corner, centered at (1092, 258), with a 0.2 s scale 0.9→1.
- Premium: a real-looking app with real numbers, few marks each with a job, notes that read like a person (lowercase, short), marker strokes with pressure and overshoot, unhurried handwriting, a balanced page where the margins carry the notes. Cheap: perfect circles and straight vector arrows, clip-art arrows, wobbling "sketchy" lines that boil, notes stamped in all at once, marks covering the UI's text, a comic font, more than one marker color.
- Banned: real company names, logos and UI copied from existing products; a second marker color; emoji; a pen or hand drawing the marks on screen; boiling or jittering lines; sketch filters applied to the UI; perfectly geometric shapes for marks; drop shadows on the marks; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.5s: the desk and the screenshot rise 16px into place and fade in (easeOutCubic); the UI is complete in its "before" state.
- 0.5–1.5s: the marker circles the "Leaking water heater" card (ellipse center (400, 292), rx 150, ry 56) in 0.5 s, then writes "urgent one," and "called 7:42" on two lines in the left margin at x 34, y 268, rotated −4°.
- 1.55–2.55s: the grabbing hand picks up the card; it lifts, arcs over the hour labels and drops into Tomás's gap; the list leaves the dashed "Assigned · Tomás R." slot and the counts update.
- 2.6–3.25s: the marker draws an arc arrow from the circle's upper right (548, 262) up through (760, 172) and down between the 10a and 11a labels to the new block's top-left corner (966, 262), shaft then head.
- 3.3–4.35s: the Miles card counts 142 to 131 and the "−11 mi" pill appears (3.3–3.8 s), Drive time changes to 3 h 51 m and Jobs scheduled to 21 / 23; the marker double-underlines "131" (3.75–4.0 s), then writes "re-routed the whole day" in the bottom margin at x 760, y 1010, rotated −2°, with a short arrow up to the underline.
- 4.4–5.3s: the "ETA 10:36 sent" chip pops onto the block (4.4 s); the highlighter swipes across it (4.55–4.9 s); the marker writes "customer gets a live ETA" in the top margin at x 870, y 92, rotated −3°, and draws an arrow from (1120, 114) down to the chip's top edge (1100, 246), clear of the date and the hour labels.
- 5.3–5.9s: in the right margin the marker writes the tagline "One drag." / "Whole day" / "planned." at x 1686, y 420, 56px, rotated −4°, line height 64px, every line inside x 1680–1890.
- 5.9–6.3s: the 6.0 s frame is the hero: the finished "after" screenshot with every mark and every note drawn, the tagline in the right margin, nothing overlapping.
- 6.4–7.0s: the marker draws a swoosh underline beneath the tagline (a single stroke that kicks up at its right end).
- 7.2–8.0s: below the tagline, the Wrenfield mark (the ink square with "W") and wordmark fade in with an 8px rise at (1690, 700) (7.2 s); "Dispatch for field-service teams" types on beneath it at 30 characters per second in IBM Plex Sans (7.5 s), wrapped to two lines.
- 8.0–10.0s: hold on the complete page.
For other lengths, keep the stroke and writing speeds, add or drop one annotated change, and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no SMIL, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face and weight before defining window.seek, and lay out the handwritten glyphs only after the fonts are loaded.
- Engine: one inline SVG with a 1920×1080 viewBox, the UI drawn as SVG rects, paths and text. Generate every mark's outline once at load from the seeded noise and its pressure profile; each frame, seek reveals the right length of each stroke (stroke-dasharray and stroke-dashoffset on a centerline used as a mask over the filled outline) and sets each glyph's opacity and offset. The turbulence filter's seed is fixed, so frames are identical on every seek.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that every note sits in a margin or clear space and is fully readable, no mark covers UI text except the highlighter behind the chip, the circles don't close, the arrows' heads point at their targets, the marks never move once drawn, the numbers add up (21 scheduled plus 2 unassigned is 23, Tomás shows 6 jobs), and only one red and one yellow are used for marks. At 1.5 s the circle and the first note are drawn; at 2.6 s the card sits in Tomás's row; the 6.0 s frame shows the "after" UI with all marks, all four notes and the tagline; the final frame adds the swoosh, the wordmark and its line. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
