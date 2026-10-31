# Kaleidoscope


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/kaleidoscope-symmetry) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/kaleidoscope-symmetry) · [对应动效输出](https://www.aicssanimations.com/previews/kaleidoscope-symmetry.mp4)

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
Make a 10-second kaleidoscope: translucent colored glass drifts and tumbles in the object cell, and two mirrors at 30° multiply it into twelve images.

<inputs>
Name: TURNLIGHT. Line: "Glass, two mirrors, a quarter turn." Detail: Kaleidoscope workshop · Weller Yard Studio 14. Duration: 10s.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Look: backlit and luminous, as if held up to a bright window. The stage is warm paper #EFE8DC. The view is a circle 920px across centered at (700, 540), lit from behind by a diffuser #FBF8F1, with a soft 40px inner vignette at its rim (#2A2420, 0 → 35%) like the inside of the tube, and a 6px brass ring #A07A3C with a 1px highlight.
Glass: 140 seeded pieces scattered over a disk of radius 480, so about a dozen sit in the visible wedge at any moment: shards (4–6 sided polygons), triangles, round beads, a few thin rods, and some clear pieces that show only their edges. Colors: magenta #D9327F, saffron #F2A31B, teal #13A39A, cobalt #2E57D0, leaf #77B83A, coral #FF6B4A, violet #7A4BC0. Pieces are translucent (alpha 0.6–0.75, 'multiply'), so overlaps mix into deeper new colors like gel filters; each has a 1.5px darker edge in its own color and a thin white specular stroke along one edge; beads get a small highlight dot. Sizes run 30–220px, for hierarchy.
Mirrors: two mirrors meeting at 30° make twelve images, six rotated copies of the wedge and six mirrored. Render the object cell to an offscreen canvas, clip a 30° wedge from the view center, and draw it twelve times (rotate by k·60°; for the mirrored copies scale(1, −1), then rotate), so every seam is a true reflection with no gap or overlap. A faint 1px seam line at 6% sells the mirrors.
Motion: pieces drift and tumble, all analytic in t: position = base + slow drift + small sine sway, rotation ±10–40°/s, seeded. Drive the drift from a warped clock that runs at full speed until 7.4s and eases to a stop at 8.6s, so motion stays continuous. Twice the tube turns: the object cell rotates about the view center on cubic-beet(0.45, 0, 0.55, 1) while pieces slide 20–60px toward the new "down", rearranging the whole pattern. Keep every on-screen speed under 500px/s so nothing strobes.
Type, #2A2420, left-aligned at x 1250, vertically centered: Syne 800, 84px, tracking 0.02em, for the name; Syne 500, 30px, for the line; Syne 500, 22px, uppercase, tracking 0.1em, for the detail.
The real thing feels physical: weight in the tumble, glass that mixes where it overlaps, seams that are true mirrors. The cheap version is a flat mandala spinning at constant speed with hue cycling.
Banned: hue cycling, continuous whole-image spinning, dark backgrounds, glow or bloom, clip-art shapes (hearts, stars, flowers), seams with gaps, extra glass colors, motion blur, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.9s: the paper stage; the view opens like an iris from a 40px circle to full size on cubic-bezier(0.16, 1, 0.3, 1), glass already drifting inside.
0.9–3.0s: drift: pieces sway and tumble and the pattern evolves continuously.
3.0–4.4s: first turn: the cell rotates 45° and the pattern rearranges.
4.4–6.0s: drift.
6.0–7.4s: second turn, 30° the other way; larger pieces settle toward the center.
7.0–8.0s: the name rises 16px and fades in; the line and detail follow 0.15s apart.
7.4–8.6s: the drift slows to a stop.
8.6–10.0s: hold, completely still.
For other durations, scale every timestamp proportionally; keep each turn at 1.2s or longer.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek. No other libraries (no three.js: this style is flat). Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the canvas's CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the font wait matters. Each frame, render the object cell to an offscreen canvas, then draw the twelve wedge copies. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.
window.seek(t), t in seconds, must compute every visual from t alone, clamping past the end to the last frame: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG.
Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Zoom the mirror seams to 300%: no gaps, overlaps or misalignment. Count twelve images. Check overlaps mix into new colors, no area strobes during the turns, and everything is still in the hold. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
