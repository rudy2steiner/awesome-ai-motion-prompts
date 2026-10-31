# Liquid Glass Interface


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/liquid-glass-interface) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/liquid-glass-interface) · [对应动效输出](https://www.aicssanimations.com/previews/liquid-glass-interface.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** product-brand
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
Make a 10-second liquid-glass film: refractive panels float over a vivid background, bending it at their edges.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Aurelle
- Tagline: "Light passes through."
- Background colors: #FF6A13, #E8237E, #2D4BFF, #B6F03C
- Track: "Low Tide" by Mara Vale
- Length: 10 seconds
</inputs>

<direction>
- Background: redraw every frame into an offscreen 2D canvas: four large soft color fields drifting, crossed by bold diagonal stripes (white 18%, 60px) and the product name, huge and outlined ("AURELLE"), 520px tall. Refraction only reads with structure behind the glass.
- Glass: one full-screen WebGL fragment shader samples that canvas. Each panel is a rounded-rectangle SDF uniform (center, size, radius). Inside:
  - lensing: displace samples along the SDF normal, strongest in the outer 36px (up to 30px), like a convex rim;
  - frost: average 12 samples from a seeded 10px disc;
  - dispersion: red and blue offset ±1.5px near the edge;
  - body: 8% white tint, saturation × 1.15;
  - specular: a 1.5px rim, bright where the normal faces the light (top-left), plus a soft bottom inner shade.
  Outside, a 10% black, 40px soft shadow. Join panel SDFs with a smooth minimum (k ≈ 28px) so meeting shapes fuse like liquid.
- Content is HTML on top: Manrope 600, white at 92%; track title 40px, artist 26px, weather "18° Clear" 72px; SVG controls; a 10% dark tint wherever contrast drops.
- Motion: springs (stiffness 180, damping 20); fusing 0.5–0.7 s; the light swings 40° once. The background drifts ~30px/s, panels faster, so lensing visibly slides.
- Premium is refraction visible at the rims, highlights that answer the light, and heavy, calm motion. Generic is a blurred translucent box.
Banned: plain backdrop blur posing as glass, white panels above 25% opacity, grey backgrounds, thick or neon outlines, text under 4.5:1 contrast, emoji, real OS or brand names.
</direction>

<structure>
- 0.0–1.2: The background flows; stripes and word drift.
- 1.2–2.6: A 760×420 player panel springs up from below; stripes bend through its rim.
- 2.6–3.8: A weather panel slides in from the left, a notification pill from the right.
- 3.8–5.4: Two 96px round buttons drift together and fuse into a pill that stretches into a scrubber.
- 5.4–7.0: All panels glide 80px left as the light swings; highlights travel the rims.
- 7.0–8.4: Panels gather and merge into one 360px round lens as content fades.
- 8.4–10.0: The lens settles over the background word, which fills solid white under it; the tagline appears below. Hold.
For other lengths, scale beats; keep the fuse and a 1.5 s minimum final hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS) with a fixed 1920×1080 (16:9) stage scaled to fit the window; design for 60fps.
- window.seek(t), t in seconds, sets every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames. Randomness comes from a seeded PRNG; springs are closed-form functions of time.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser; with ?render, don't start that loop.
- Google Fonts via <link> are fine. Redraw the canvas and run the shader in every seek (preserveDrawingBuffer: true); position HTML from the same panel values. No three.js.
</build>

<check>
Before showing me, screenshot seek(0) through seek(10), one frame per second, and look at each. Fix overlaps, clipped or cramped text, and anything generic. Stripes must bend only at the rims, and panel text must stay readable over bright colors. Confirm the final frame holds.
</check>
```
