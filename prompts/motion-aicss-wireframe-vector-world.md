# Wireframe Vector World

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/wireframe-vector-world](https://www.aicssanimations.com/directory/Motion-Prompts/wireframe-vector-world)
- **Collected:** 2026-11-08

## Prompt

```
<inputs>
- TITLE. Default: "VANTAGE 9".
- SUBLINE. Default: "SYSTEM ONLINE — PRESS START".
- PHOSPHOR: "green" (default) or "amber".
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Recreate a 1980s vector monitor: a beam drawing pure lines of light on a black tube. Brightness, never fill, does the work.
- Palette: background #020604. Green: glow #2BFF88, core #D9FFE9. Amber: glow #FFB000, core #FFF0C8. One hue only.
- Lines: stroke each path three times with 'lighter' compositing: 12px at 6% alpha, 4px at 22%, a 1.4px core at 90%. Crossings brighten on their own: that's the signature. Endpoints get a brighter dot where the beam dwells.
- Persistence: also draw the moving object at t−0.035, t−0.07 and t−0.105s at 35%, 18% and 8% alpha for a phosphor smear, computed from t.
- Tube: barrel-distort every projected vertex (r' = r(1 + 0.045r²), r normalized to the half-diagonal), splitting long lines into 24px pieces so they bow. Over it, 1px scanlines every 3px at 7% black and a corner vignette to 55% black. Brightness may breathe ±3% on a 0.7Hz sine, nothing faster.
- World: a perspective ground grid (lines every 2 units, 40 deep) scrolling toward camera, a horizon of 26 seeded jagged peaks as one polyline, a 48-segment moon with three crater ellipses.
- Object: a wireframe icosahedron inside a larger counter-rotating dodecahedron, 22°/s on Y and 9°/s on X, projected in plain JS (focal length 900px).
- Type: title outline only (strokeText, never fillText) in Orbitron 700, 120px, letter-spacing 0.18em, through the same glow passes. HUD readouts in Share Tech Mono 22px, numbers derived from t.
- Draw-on: new geometry traces along its length (setLineDash, lineDashOffset) with a hot dot at the tip.
Banned: filled shapes, gradients along lines, RGB split or glitch (raster artifacts), pixel fonts, flicker faster than 1Hz, a second hue, full-frame bloom, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: tube warms: a center dot stretches into a horizontal line (peak 70% brightness) that fades as the scene begins.
- 0.8–2.4s: grid traces from horizon toward viewer; mountains draw left to right.
- 2.4–4.4s: object edges draw on, 40ms apart, then rotation starts.
- 4.4–7.0s: fly forward: grid scrolls at 6 units/s, HUD numbers count, moon parallaxes.
- 7.0–8.6s: title reveals left to right behind a moving clip whose edge carries a beam head; the object shrinks to 60% above it.
- 8.6–9.3s: subline types on at 28 characters/s with a block cursor blinking at 1.5Hz.
- 9.3–10.0s: hold.
Scale the fly-forward beat for other lengths.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- Engine: Canvas 2D, no libraries.
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. The glow must stay crisp, not foggy; the title must clear the object and HUD; no grid moiré and no blown-out white frames. Confirm the final frame holds as a composed end card.
</check>
```
