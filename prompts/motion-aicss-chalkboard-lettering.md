# Chalkboard Lettering

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/chalkboard-lettering](https://www.aicssanimations.com/directory/Motion-Prompts/chalkboard-lettering)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second film of a café chalkboard menu lettered by hand in dusty chalk, with ornaments, a doodle and one line wiped away and rewritten.

<inputs>
If I don't give you something, use the default and don't ask.
- Café: Fennel & Fig (fictional)
- Subhead: Today's Board
- Coffee: Flat white 3.40 · Oat latte 3.80 · Spiced chai 3.20
- Kitchen: Soup of the day, Tomato & basil 5.50 (wiped and rewritten as Leek & potato 5.50) · Cardamom bun 2.80
- Footer: Open 7–4, every day
- Length: 10 seconds.
</inputs>

<direction>
- Board: slate green #23332D with soft mottling (±5% seeded fBm), a ghost layer of old erased chalk (pale swirls at 6–10%: the board has been used before), and a fine tooth, a high-frequency noise texture made once at load that the chalk catches on. An oak frame 48px wide (#8A5E3A, generated grain, mitred corners) runs around x 120–1800, y 70–1010, with a chalk tray along the bottom holding two chalk stubs and a felt eraser. Soft warm window light from the upper left lifts the board 6% on that side.
- Chalk: white #F1EFE6, butter #F2DD8C, rose #F0A9B6, sky #A3CDE8. Every mark is a mask multiplied by the board's tooth: where the tooth is low, the chalk skips, so strokes break up at their edges and thin out under light pressure. Fresh strokes shed a few specks of dust that drift down 20–60px and fade.
- Lettering, a café mix of styles, each line written letter by letter. Render each letter's shape to a mask, then reveal it with a soft-edged front that follows the letter's own strokes (down the stems from the top, around bowls from the top), while a chalk stick (a 14px white cylinder with a worn, rounded tip and a soft shadow) rides the front. The name takes about 80ms per letter; smaller lines run as a gentle time-lapse at 22–30ms per letter.
  - Café name: "Playfair Display" 900 italic, 150px, white, centered on baseline y 282, with an inline (a 4px board-colored line just inside each stroke) and a butter drop shade of 45° hatching offset 10px down and right.
  - Subhead: "Satisfy" 400, 64px, rose, centered on y 370, between two small hand-drawn laurel sprigs.
  - A double rule with a diamond at its center, x 520 to 1400 at y 408, drawn from the center outward.
  - Columns: COFFEE from x 300 and KITCHEN from x 1020 on baseline y 470, in "Bebas Neue" 400, 58px, white, each with a hand-drawn underline that overshoots and curls. Left column items in Bebas Neue 46px, white, on baselines y 540, 616 and 692, prices in Bebas Neue 46px, butter, right-aligned at x 880, joined by dotted leaders. Right column: "Soup of the day" on y 540; its variety in "Caveat" 500, 40px, sky, on y 600 with its price right-aligned at x 1600; "Cardamom bun" on y 692 with its price.
  - A doodle: a steaming cup (outline, saucer, handle and three steam curls), about 160px tall, centered at (1480, 820), drawn as centerline paths with the same chalk texture.
  - Footer: Caveat 600, 40px, white, centered on baseline y 912.
- The wipe: the felt eraser (a 150×56 block, wooden back #6B4A2E, grey felt #9A9A98) lifts from the tray and rubs out the variety line in three short zig-zag passes; chalk vanishes where the felt passes but leaves a pale smear (the strokes blurred, at 30% and fading to 15%), then the new variety is written over the ghost, with a small rose star doodled beside it.
- Motion is steady and handmade: one thing written at a time, the chalk stick moving at a hand's pace, no bounces or springs. Everything stays at least 48px inside the frame's inner edge.
- Premium: chalk that breaks up on the board's tooth, a mix of lettering styles with shading and ornaments, the haze of old erasures. Cheap: a chalk-texture font fading in, perfectly clean white strokes, a uniform noise overlay.
Banned: chalk-style display fonts that fake the texture, letters fading in, clean vector strokes without tooth, glow, neon, a pure black board, emoji or clip-art icons, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.5s: the used board in window light, chalk stubs in the tray, a few dust specks settling.
- 0.5–1.8s: the café name is written letter by letter, then its inline and butter hatch shade.
- 1.8–2.4s: the rose subhead, the laurels and the double rule.
- 2.4–4.0s: COFFEE and its curling underline, then its three items, each followed by its leader and price.
- 4.0–5.5s: KITCHEN, Soup of the day, Tomato & basil and its price, then Cardamom bun and its price.
- 5.5–6.3s: stillness: the name, subhead and both columns read as a finished board while the dust settles.
- 6.3–6.9s: the eraser rubs out Tomato & basil in three passes, leaving a pale smear, and goes back to the tray.
- 6.9–7.7s: Leek & potato is written over the smear in sky chalk; the rose star appears beside it.
- 7.7–8.4s: the steaming cup doodle, then the footer.
- 8.4–8.7s: the chalk stick returns to the tray.
- 8.7–10.0s: hold, still.
For other lengths, scale the lettering speed and the stillness together; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before building the letter masks and defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. No libraries.
- At load, build the board, the frame, the tooth texture and every letter's mask with a per-pixel reveal-time map (when the writing front reaches it); seek(t) shows each mask where its reveal time has passed, multiplied by the tooth, and computes the eraser, smear and dust from t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the chalk breaks up on the tooth at 1280×720, every line sits at least 48px inside the frame, leaders run cleanly to their prices, the smear stays faintly visible under the new line, and the 6 s frame shows the name, subhead and both columns complete. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
