# Broadcast Lower Thirds

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/broadcast-lower-thirds) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/broadcast-lower-thirds)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** explainers-data
- **作品发布时间：** 2026-10-12
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
<inputs>
- NETWORK. Default: "KESTREL SPORTS".
- MATCH. Default: Harbor City (HBC) 1–1 Rivergate (RVG), clock from 63:40; HBC scores at 64'.
- NAMES. Default: presenter Mara Velden, Lead Analyst; scorer J. Okonkwo-Hale.
- HEADLINES. Default: four invented league headlines.
- COLORS. Default: navy #0B1A33, white #F6F8FB, orange #FF5A1F.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
A live-sports package keyed over a match feed: engineered, aligned, snappy.
- Feed stand-in: blurred stadium gradients (stands #101826, pitch #2F6B3F → #23552F), 30 seeded floodlight bokeh circles (#FFF5DE, 8–18% alpha), panning 12px/s.
- Layout: all text inside title-safe (96px sides, 54px top and bottom), on an 8px grid; only the ticker band bleeds to the frame edges.
- Type: Barlow Condensed 600/700 for names, codes and ticker; Barlow 500 for titles; tabular-nums on every figure so the clock never jitters.
- Score bug (top-left at 96,54): navy plate 360×56, team codes, white scores in #1E3A6B cells, orange clock, 4px orange underline.
- Lower third (left 96px, bottom edge 168px up): orange bar 8×88; white plate, name in Barlow Condensed 700 54px navy; navy sub-plate, title 26px white.
- Ticker: a 60px navy band on the bottom safe line (y 966–1026), orange "LATEST" block, headlines crawling right to left at a constant 130px/s, a glyph between items.
- Build grammar: accent first (scaleX 0→1 from the left, 220ms easeOutQuint), plate wipes behind it 60ms later (320ms easeOutQuint), text slides up 18px from a mask (280ms easeOutCubic, 50ms stagger). Exits reverse at 220ms easeInCubic.
- Goal: the digit rolls up (300ms), its cell pulses orange once, and a stat bar slides out of the bug: "POSSESSION 58% · 42%", bars filling over 600ms.
- Bumper: navy, orange and white parallelograms skewed −16° sweep across 70ms apart (480ms easeInOutQuart) to the network card: wordmark Barlow Condensed 700 110px plus "UP NEXT · Post-match analysis" 28px.
Banned: glossy bevels, reflections, lens flares, sparkles, fade-only entrances, bouncy easing, a second accent color, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: feed only.
- 0.6–1.2s: score bug builds (1–1, clock running).
- 1.2–1.8s: ticker band rises and starts crawling.
- 2.0–2.7s: lower third builds.
- 2.7–4.8s: hold; clock and ticker run.
- 4.8–6.6s: lower third exits; at 5.1s the goal: score rolls to 2–1, lower third returns as "GOAL · J. Okonkwo-Hale 64'", stat bar slides out.
- 6.6–7.2s: all graphics exit in reverse build order.
- 7.2–8.6s: bumper panels sweep through; card text slides up at 8.0s.
- 8.6–10.0s: hold on the card.
For other lengths stretch the holds, never the builds.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- Engine: HTML/CSS; clock, ticker offset and every transform and clip-path come from seek(t).
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. Keep text inside title-safe, names inside their plates, and clock digits fixed in width. Confirm the final frame holds as a composed end card.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
