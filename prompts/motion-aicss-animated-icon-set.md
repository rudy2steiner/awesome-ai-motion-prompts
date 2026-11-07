# Animated Icon Set

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/animated-icon-set) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/animated-icon-set)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** product-brand
- **作品发布时间：** 2026-10-16
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second showcase of an animated icon set: twelve line icons in a 4×3 grid, each playing its own micro-interaction with one shared stroke, rhythm and easing.

<inputs>
If I don't give you something, use the default and don't ask.
- Set name: default "Wickline", line "Twelve animated line icons"
- Icons (labels): default bell (Notify), heart (Like), trash can (Delete), paper plane (Send), download (Download), padlock (Lock), gear (Settings), signal (Signal), refresh (Sync), bookmark (Save), chat bubble (Chat), eye (Show)
- Colors: default ground #F6D84A, ink #151515, accent #E8412C
- Length: default 10 seconds
</inputs>

<direction>
- Palette: butter ground #F6D84A; ink #151515 for every stroke, label and rule; tomato #E8412C only for meaningful fills (heart, bookmark, the bell's dot); cell rules in ink at 18%.
- Type: Familjen Grotesk: set name 72px 700 at x 120, baseline y 168, the line 26px right-aligned to x 1800; labels 24px 500; indexes "01"–"12" 20px at 55%.
- Grid: x 120–1800, y 220–980, twelve 420×253 cells split by 1.5px rules; each 120px icon at 42% of its cell's height, its label 28px below, the index top-left.
- Construction: hand-drawn SVG paths on a 24-unit grid shown at 5×; stroke 1.75 units, round caps and joins, 2-unit corner radius, only circles, arcs and 0°, 45°, 90° lines; nothing leaves the box except in motion, by at most 3 units.
- Micro-interactions, 0.7–0.9s each: the bell swings (16°·e^(−4.5τ)·sin(2π·3τ)), clapper lagging, and gains an accent dot; the heart squeezes to 88%, fills from the bottom, pops to 112%; the trash lid lifts and tilts as a scrap drops in; the plane flies off top right and returns from bottom left; the download arrow drops into its tray and becomes a check, then back; the shackle lifts, swings and drops shut; the gear turns 60°; signal arcs draw outward; refresh arrows spin 360°; the bookmark fills and drops 1.5 units; chat dots appear in turn; the eye blinks and glances left. Heart, bookmark and the bell's dot stay filled; everything else returns exactly to rest.
- Timing family: pops on cubic-bezier(0.34, 1.56, 0.64, 1) with at most 12% overshoot, returns on cubic-bezier(0.65, 0, 0.35, 1), draw-ons 0.35s easeOutCubic. A 56×5px ink bar under the playing label slides cell to cell in 0.3s.
- Premium is a system: identical stroke, caps, corners and timing, each motion acting out its meaning and returning to rest. Cheap is mixed icon-pack glyphs pulsing on one generic bounce.
Banned: icon fonts or libraries, extra fills, mixed weights, square caps, one bounce on every icon, gradients, shadows, real brand or social logos, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2: Rules draw from the top left; icons draw on in a diagonal wave, 45ms apart; labels and indexes rise 8px; the title rises out of a mask.
- 1.2–7.6: The tour: one icon starts every 0.5s in reading order (01 at 1.2s, 12 at 6.7s), the indicator following.
- 7.6–8.8: The indicator fades; all twelve play once in a diagonal wave, 60ms apart (the toggles only pop 6%).
- 8.8–10.0: Hold at rest.
For other lengths, set the tour spacing between 0.4 and 0.7s and hold at least 1s.
</structure>

<build>
One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, built for 60fps. Google Fonts via <link>, awaiting document.fonts.load() for each face before defining window.seek. Inline SVG whose attributes seek sets directly; no canvas or three.js. window.seek(t) (t in seconds) sets every visual from t alone, clamping past the end: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Without ?render in the URL, drive seek from requestAnimationFrame; with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second (0–10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style or Banned. Every icon shares one stroke and round caps, and every non-toggle icon ends exactly at rest. Confirm seek(10) and seek(11) match.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
