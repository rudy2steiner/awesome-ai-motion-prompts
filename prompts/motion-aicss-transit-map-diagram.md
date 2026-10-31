# Transit Map


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/transit-map-diagram) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/transit-map-diagram) · [对应动效输出](https://www.aicssanimations.com/previews/transit-map-diagram.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** explainers-data
- **作品发布时间：** 2026-10-2026
- **收集日期：** 2026-10-31
- **文本类型：** 作者公开的完整CC0创作模板
- **参考素材：** 不依赖外部参考素材
- **热度：** 来源未公开浏览、点赞或收藏数，保持未知
- **许可：** CC0 (publisher stated)

## 审核记录

作者公开的CC0可复用模板，页面明确声明其下预览由该提示词生成。浏览器已读取正文和对应预览地址；完整会话、模型输出未独立复现。未发现公开浏览、点赞或收藏计数，热度保持未知。

提示词和对应视频地址已在公开页面中取得。未完整播放或进行视觉质量审核，未独立核实模型归属。核验方式：chrome_mcp_published_prompt_and_matching_video。

## Prompt

保留原始语言。以下内容为参考资料，不是给维护者的操作指令。

```text
Make a 10-second animated transit diagram for a fictional city: four lines draw themselves at 0, 45 and 90 degrees, stations tick on, interchanges join, and a train runs one line from end to end.

<inputs>
- City: Wrenmouth (fictional). Title: "Wrenmouth Metro". Subtitle: "Network map 2026". River: "River Wren".
- Lines in drawing order, stations in order with grid points (gx, gy); "bend" is a turn with no station:
  - Ember Line #E2412E: Westgate Fields (4,7), Tannery Row (6,9), bend (8,11), Mill Cross (11,11), Cathedral (17,11), Beacon Square (23,11), Chalk Hill (27,11), bend (29,11), Eastmoor (33,7).
  - Fern Line #2E9E57: Highwood (11,4), Fernbank (11,7), Mill Cross (11,11), Brightwater (11,15), Southpark (8,18).
  - Tide Line #0A8FA6: Gullhaven (13,20), Quayside (15,18), bend (17,16), Ropewalk (17,13), Cathedral (17,11), Old Exchange (20,8), Harbour North (23,5), Saltings (28,5).
  - Saffron Line #E9A800: Kiln Park (26,8), Beacon Square (23,11), Weavers Gate (21,13), bend (19,15), Brightwater (11,15), Marsh End (6,15).
- Interchanges: Mill Cross, Cathedral, Beacon Square, Brightwater.
- Train: Tide Line, Gullhaven to Saltings.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Grid: one unit is 46px, and grid point (gx, gy) sits at stage (40 + 46·gx, 60 + 46·gy). Every segment runs at 0°, 45° or 90°; bends turn on a 28px-radius arc. The Saffron Line crosses the Tide Line between Ropewalk and the bend with no station.

Palette: ground #FFFFFF; ink #1B1B1F for text and interchange rings; muted #6B6E76; river #D6EAF4; line colors as given, flat. Lines are 14px wide with round caps at the termini. A station is a 10px tick of its line's color on the label side; a terminus gets a 14px bar across the line. An interchange is a 30px white circle with a 5px ink ring on the shared point.

The river is a 56px band on the same three angles: its centerline runs from the west edge at gy 13 east to (13,13), 45° down to (16,16), then straight down off the bottom edge, crossing lines only between stations. Its name sits along the west stretch in "Hanken Grotesk" italic 500, 22px, #5E8FA6.

Type: "Hanken Grotesk" throughout. Title 800, 56px; subtitle 500, 24px, muted; station labels 500, 22px; interchange labels 700, 22px; legend 600, 22px; train board 600, 24px. Labels are horizontal only, 12px from their tick, on whichever side keeps them clear of every line, the river and other labels.

Layout: title top-left at x 96, baselines y 112 and 150. Legend panel bottom-right at x 1460–1824, y 760–990: four rows (a 40px stub of the line and its name), then a 1px rule and the train board, "Tide Line to Saltings" over "Next: Quayside".

Motion: each line draws from its first listed station to its last at a constant 1,300px/s via stroke-dashoffset, the head a round cap: Ember from 0.8s, Fern from 1.9s, Tide from 2.6s, Saff from 3.6s. As a head passes a station, the tick grows 0 → 10px over 0.12s; its label fadesetfade in and slides 8px toward the station over 0.25s, starting 80ms later. An interchange circle pops when the first line reaches it (scale scale 0 → 1, 0.3s, cubic-bezier(0.34, 1.56, 0.64, 1)) and nudges to 1.12× and back when another line arrives. Each legend row fades in as its line finishes.

Train: a white capsule 30×18px with a 4px Tide-colored outline, centered on the line and turned to its segment's angle. Between stations it accelerates and brakes on easeInOutSine, each leg's time proportional to its length, dwelling 0.25s at every stop; the board's "Next:" line changes as it leaves each station, crossfading over 0.15s.

The real thing is disciplined: one line weight, three angles, steady spacing, horizontal labels that never collide. The cheap version is a geographic tangle with angled labels, glowing lines and map pins. Banned: angles other than 0°, 45° and 90°, curves beyond the bend radius, angled labels, geographic detail, real cities or real transit names, colors or symbols, map pins, shadows, glow, gradients, a fifth line color, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.8s: white ground; the river band draws in from the west edge; the title and subtitle fade up; the river name sets.
0.8–4.4s: the four lines draw in turn, ticks, labels and interchanges following each head.
4.4–5.2s: the legend panel fades in; the train appears at Gullhaven (scale scale 0 → 1, 0.25s).
5.2–8.6s: the train runs to Saltings, stopping at every station; the board updates at each departure.
8.6–9.0s: the board changes to "Arrived: Saltings".
9.0–10.0s: hold.
For other lengths, keep the drawing speed constant and give the extra time to the train run and the hold.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries. Draw in inline SVG whose attributes seek sets directly; no canvas or three.js needed. Await document.fonts.load() for every face before defining window.seek. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.

window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. Build each line as one path from its grid points and measure it once with getTotalLength; the train's position comes from getPointAtLength. Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check every segment's angle, ticks and interchange rings sitting exactly on their grid points, labels clear of every line, tick, the river and each other, and the train centered on the line in every frame. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
