# Lava Lamp

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/lava-lamp-metaballs) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/lava-lamp-metaballs)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** music-audiovisual
- **作品发布时间：** 2026-10-16
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second lava lamp title: a 1970s lamp warms up beside a late-night radio show title, and its wax rises, merges, splits and sinks.

<inputs>
- Show title: "Mellow Hours" (a fictional late-night radio show), set on two lines.
- Tagline: "Slow songs for warm rooms."
- Details: "Fridays · 11 PM · 94.7 FM".
- Lamp: tangerine wax in plum liquid, brass base and cap.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: walnut wall #2A1A14 (board highlights #3A261C, grooves #160D09), sideboard top #1C110C with a #4A2E1E front edge, brass #6E4A1F → #C8913F → #F1CF86, liquid plum #3B1238 at the top warming to #A8396B near the bulb, wax tangerine #FF6A1A with a hot core #FFC15E and a cool skin #B83A12, glow #FF7A2A, type cream #F6E3C3, small text #D9B89A.
Type: the title in Shrikhand at 150px, cream, with a hard 6px tangerine offset shadow down-right, left-aligned at x 1010 on baselines y 450 and 600. Tagline Outfit 500, 36px, cream, at y 700. Details Outfit 600, 24px, uppercase, tracking 0.18em, #D9B89A, at y 768.
The lamp is symmetric about x 600. Base cone from y 930 (300px wide) up to y 700 (124px). Glass from y 700 to y 210, its half-width a smooth profile: 62px at the bottom joint, swelling to 98px at y 560, tapering to 46px at the top joint (two cubic segments, no kinks). Cap cone from y 210 (92px) to y 140 (40px) with a small knob. It stands on a sideboard whose top runs the full width at y 930.
Wall: vertical walnut boards 120px wide with 3px dark grooves and faint long grain streaks at 6% contrast, procedural and seeded. The lamp's light pools on the wall as a soft radial glow centered on the glass (radius 640px, up to 22% in screen blend) and as a warm streak along the sideboard top, both following the bulb.
Wax as metaballs: one puddle (a wide, flattened blob resting on the bulb plate) plus eight blobs, radii 26–70px. Field f = Σ (1 − d²/R²)³ for d < R, with R = 2.1·r; the surface is f = 0.5. Each blob is an ellipse in the field: vertical stretch sy = 1 + min(|vy|/320, 0.45) and sx = 1/√sy, so blobs elongate while they move and round up at rest. Centers come from authored keyframes (t, x, y, r) interpolated with easeInOutSine plus a 5px lateral wobble, sin(1.3t + φ), never from stored state. Keep every blob at least 10px inside the glass; anything that travels to the narrow top stays at r ≤ 36px.
Honor the physics: wax heats at the bottom, swells and domes, necks and pinches off; rising blobs travel 70–140px/s, pause and flatten under the cap as they cool (sy 0.85), then sink more slowly (50–80px/s) near the glass wall. Merges and splits happen through the field, so necks form and thin naturally; nothing pops.
Shading, in a fragment shader: anti-alias the wax edge over 1.2 screen pixels (divide by the field gradient). Wax color by height and thickness: hot core near the bulb, tangerine mid-lamp, cool skin toward the top; lighter where f is high, a soft darker rim, and a highlight from below using the field gradient as a normal. Liquid: a vertical gradient from the plum top to the bright bottom, plus a faint 6% plume of light rising from the bulb. Glass: two vertical specular streaks that follow the profile (white at 16% and 7%) and 12px of edge darkening inside the silhouette. Brass: horizontal brushed noise, one vertical specular band, rings at the joints.
Warm-up: at 0s the bulb is off: liquid #1E0A1C, wax a dull #7A2E10 puddle, no glow. The bulb comes up over 0.3–1.8s on easeInOutSine, with no flicker.
Type motion: title letters rise 40px out of a heat-haze blur (8px → 0) with a small sine wobble that decays, 0.9s each on cubic-bezier(0.22, 1, 0.36, 1), 70ms apart. The other lines fade up over 0.7s, rising 12px.
Premium: an object in a room, with wax that stretches as it moves, necks before it pinches and lingers at the top, and glass, brass and wall glow that sell the lamp. Cheap: bouncing circles in a rectangle, fast motion, neon gradients, no lamp at all.
Banned: bulb flicker, blob speeds over 160px/s, perfect circles, aliased edges, neon or cyan, wax escaping the glass, 3D libraries, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.3s: a dim room, the lamp off.
- 0.3–1.8s: the bulb warms; the glow rises on the wall and the sideboard; the puddle brightens and domes.
- 1.8–2.6s: a dome lifts, necks, pinches off at 2.4s and rises.
- 2.6–4.0s: two more blobs lift at 2.9s and 3.4s; the title letters rise in from 2.8s.
- 4.0–5.0s: the second blob catches the first and they merge at 4.6s into one tall blob.
- 5.0–6.0s: the merged blob reaches the top and flattens under the cap; the tagline fades up at 5.2s.
- 6.0–7.0s: it splits in two: a neck forms at 6.2s and parts by 6.6s, and the lower half starts to sink.
- 7.0–8.4s: a cooled blob slides down near the right wall and rejoins the puddle at 8.0s; the details fade in at 7.4s.
- 8.4–9.0s: motion eases into a resting arrangement: one blob hovering mid-glass, one under the cap, the puddle.
- 9.0–10.0s: hold; no blob drifts more than 6px.
Other lengths: add or remove whole rise-and-sink cycles at the same speeds, and end on at least 1s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative (growth, simulation, particles) is precomputed once at load at a fixed step or solved analytically, so seek can jump to any time. Past the end, hold the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Engine: one WebGL canvas whose fragment shader draws the wall, glow, sideboard, lamp and wax full-frame (preserveDrawingBuffer: true, drawn once per seek); blob centers, radii and stretch are computed in JS from t and passed as uniforms; type is HTML on top. No three.js.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that every neck pinches over several frames (no single-frame pops), blobs stay inside the glass, the lamp is symmetric and stands on the sideboard, the glow never flickers, and the title stays legible against the wall. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
