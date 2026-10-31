# Stained Glass


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/stained-glass-window) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/stained-glass-window) · [对应动效输出](https://www.aicssanimations.com/previews/stained-glass-window.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** motion-studies
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
Make a 10-second stained-glass animation: lead lines draw, the panes fill, the sun comes out, and the window's colors slide across a stone floor as the sun moves.

<inputs>
Studio: Hollin Glass Works. Line: "Light, held in lead." Detail: Open studio · Saturdays 10–4.
Window: a round-arched window of a sun rising behind a tree over three hills, inside a border of alternating ruby and straw panes.
Duration: 10s.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Scene: a dim stone interior seen straight on, wall above and floor below. Pinhole camera: eye 1.7m above the floor, 10m from the wall, focal length 1500px, principal point (960, 420). The wall meets the floor at y 675. The window is 2.6m wide and 3.6m tall with a semicircular head, sill 0.6m up, spanning x 565–955, y 45–585.
Wall: ashlar blocks about 0.5 × 0.3m, #2B2521 to #3B332C, ±6% per block, 2px mortar #1D1916, fine seeded noise. Floor: 0.8m stone flags in perspective, #3E362F with #26211D seams and a faint worn sheen.
Glass: about 40 panes as a planar subdivision (neighbors share edges): a 22px ruby and straw border following the arch, a cobalt #1F4FB5 and sky #5E9BD8 sky, an amber #E3961B sun with straw #F1DE9C rays in the arch, a tree with an emerald #1E8A4C canopy split into six panes, hills in olive #6E8B2A, emerald and violet #6A3E9E, and ruby #B11F2C in the border. Each pane gets seeded streaks along one direction (±10% lightness) and a few seed bubbles. Unlit glass shows 25% of its color; lit glass glows at full color with a soft 6px bloom inside the window.
Lead: 8px came #18181A along every shared edge with a 1px #3A3A3E top highlight; two 4px iron saddle bars cross the window.
Light: the sun is a direction d (into the room, downward). Its elevation falls 46° → 38° and its azimuth swings from 12° left to 18° right of the wall normal. Project each pane onto the floor (window point + d·(height ÷ −d.y)), then through the camera: an inverted, stretched copy of the window whose top lands nearest the viewer. Draw the projections to an offscreen canvas with ctx.filter blur(9px) and composite with 'screen' at 60% on the floor. Shafts: faint quads from each pane to its floor patch, additive at 5–8%, fading toward the floor. 160 seeded dust motes drift under 6px/s and show only inside the shafts. While lit, a warm glow (≤20%) spreads on the wall around the window.
Type, on the wall at x 1300–1800, y 170–400, ivory #EFE6D4: Spectral SC 500, 56px, tracking 0.06em, for the studio; Spectral 300 italic, 34px, for the line; Spectral 400, 22px, tracking 0.08em, for the detail.
Motion is calm, a time-lapse of an afternoon. Lead grows at about 1,500px/s from where it meets lead already drawn. Light changes ease over at least 1s on cubic-bezier(0.45, 0, 0.55, 1); the sun moves continuously.
The real thing is colored light that obeys geometry, patches stretching and sliding exactly as the sun moves and matching the panes; the cheap version is a glowing window with a colored blur pasted on the floor.
Banned: religious figures or symbols, text in the glass, lens flares, light that ignores the window shape, rainbow glow, flicker or pulsing, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.6s: the dim room in cool ambient light; the window opening is dark.
0.6–2.4s: lead draws: the arch frame first, then the main divisions, then the pane outlines.
2.4–3.8s: glass fills pane by pane from the bottom up, each in 0.25s with a rising fill edge, still unlit and dull.
3.8–5.0s: the sun comes out: panes brighten to full glow over 1.2s as the shafts and floor patches fade up with them.
5.0–8.8s: the sun moves in one continuous ease-in-out; the patches slide right and stretch toward the viewer; dust drifts in the shafts.
6.6–7.6s: the studio name rises 12px and fades in; the line and detail follow 0.2s apart.
8.8–10.0s: hold; only the dust drifts.
For other durations, scale every timestamp proportionally; keep the sun's move at 3s or longer.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek. No other libraries (no three.js: the perspective here is simple enough to compute by hand). Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the canvas's CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the font wait matters. Generate the stone, floor and glass textures once at load into offscreen canvases. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.
window.seek(t), t in seconds, must compute every visual from t alone, clamping past the end to the last frame: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG.
Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check the floor patches match the panes in shape and color order, sit only on the floor, and line up with the shafts; lead joins with no gaps; light ramps smoothly with no pulsing; the type stays readable on the wall. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
