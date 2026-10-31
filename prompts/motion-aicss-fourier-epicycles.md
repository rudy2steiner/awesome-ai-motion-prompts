# Fourier Epicycles


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/fourier-epicycles) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/fourier-epicycles) · [对应动效输出](https://www.aicssanimations.com/previews/fourier-epicycles.mp4)

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
Make a 10-second Fourier epicycle drawing: a chain of rotating circles, computed from the outline of an ampersand, traces that ampersand in one turn.

<inputs>
- Shape: the ampersand "&" in Playfair Display 900 italic.
- Circles: the 160 largest terms.
- Title: "160 circles draw an ampersand".
- Caption: "Each circle is one term of the outline's Fourier series."
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
The math is the art direction:

1. Outline: at load, draw the ampersand 760px tall onto an offscreen canvas; trace every contour with marching squares (the outer edge and each counter); join each counter to the outer contour at their closest points with a there-and-back cut, so the glyph becomes one closed loop; resample that loop to N = 1,024 points evenly spaced by arc length, as complex numbers z_n.

2. Coefficients: c_k = (1/N) Σ z_n · e^(−2πi·k·n/N) for k from −512 to 511. Sort by |c_k|, largest first, and keep 160, with k = 0 (the center) always first.

3. Chain: at phase s in [0, 1], each circle is centered on the previous circle's tip, with radius |c_k| and arm angle arg(c_k) + 2π·k·s; the last tip is the pen. The trace is the same sum evaluated at 2,048 evenly spaced phases from 0 to s, recomputed every frame, never accumulated.

Show real numbers: a table lists the eight largest terms after k = 0 as computed (k, |c_k| in px to one decimal, phase in degrees), and a counter shows how many circles are in play.

Look: pale green engineering paper #E8EFE1; minor grid every 20px #D3DFC9 and major every 100px #BFD0B2, both 1px. Circles #2F3B35 at 1px and 30% opacity; arms #2F3B35 at 1.5px and 70%; the pen a 9px #D2452A dot; the trace #D2452A at 4px with round joins; the target outline as the 1,024 sample points, 2.5px dots of #8EA596 at 60%. Only the 60 largest circles get arms; smaller ones show just their rim, so the chain never strobes.

Type: title "Spectral" 500, 60px, #1F2722; caption "Spectral" italic 400, 30px; table, counter and labels "DM Mono" 400 and 500, 22px, tabular figures, #2F3B35.

Layout: the drawing is centered at (800, 560), the k = 0 term at that point; if any circle would cross the table panel, scale the whole drawing down. Title top-left at x 96, baseline y 116. Table on the right in a 1px #BFD0B2 ruled panel at x 1360–1824, y 200–620: a header row "k |c_k| phase", then eight 40px rows. Counter beneath at baseline y 680: "circles 160 of 1,024". A round magnifier 280px across, centered at (1592, 860), shows the pen tip at 4× inside a 1.5px #2F3B35 rim, redrawn from the same math with screen-constant line widths. Caption bottom-left at x 96, baseline y 1000.

Motion: assembly comes first, with s held at 0: circles join largest first, each scaling up from its parent's tip over 0.25s on cubic-bezier(0.22, 1, 0.36, 1), the first five 0.25s apart, then accelerating so all 160 are in by 2.8s; the counter climbs with them and the table rows write on top to bottom. Then one full turn: s runs from 0 to 1 between 2.8s and 7.8s at constant speed, and the trace closes exactly on its start. The camera never moves: this is a precise instrument.

The real thing shows its math: honest coefficients, a trace that closes on itself, circles shrinking toward the pen like the sections of a telescope. The cheap version hand-sizes the circles, fakes the path with a stroke reveal of the outline, or makes it glow. Banned: glow, gradients, a stroke-dashoffset reveal of the outline, hand-picked circle sizes, a trace accumulated in a buffer between frames, colors beyond the palette, a moving camera, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–1.0s: paper and grid; the title writes on with a left-to-right clip (0.6s); the 1,024 sample dots appear around the outline in arc-length order (0.8s).
1.0–2.8s: the chain assembles from the center outward, largest to smallest; the table writes on; the counter climbs to 160.
2.8–7.8s: one turn: the pen traces the ampersand and closes where it began; the magnifier follows the pen, showing the smallest circles still turning.
7.8–8.6s: circles and arms fade to 12%; the sample dots and the magnifier fade out; the caption writes on.
8.6–10.0s: hold, perfectly still, the chain parked at s = 1.
Other lengths: give the turn every extra second; keep the assembly at least 1.5s and the hold at least 1s.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries. Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the font wait matters here. Await document.fonts.load() for every face before defining window.seek. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.

window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. The contour trace, resampling, transform and sort run once at load; each frame evaluates the chain at its phase. Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check that the trace closes exactly and reads clearly as the ampersand, the table shows the computed values, the magnifier stays centered on the pen and never strobes, and the counter matches the circles drawn. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
