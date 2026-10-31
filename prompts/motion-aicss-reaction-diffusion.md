# Reaction-Diffusion


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/reaction-diffusion) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/reaction-diffusion) · [对应动效输出](https://www.aicssanimations.com/previews/reaction-diffusion.mp4)

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
Make a 10-second reaction-diffusion title: Gray–Scott coral grows out of a word, fills the frame, relaxes into fingerprint ridges, then pulls back so the word stands clear.

<inputs>
- Word: "BIOME" (4–6 letters seed best).
- Lab line: "Kelpwork Materials Lab".
- Caption: "Patterns that grow themselves."
- Colors: deep-sea ground and coral, as below.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: ground #08161B, trough shadow #040B0E, coral body #EE6440, coral crest #FF9A70, highlight #FFE4D2, type ivory #F6EDE3, readout and plate grid teal #7FA3A6.

Type: the word in Syne 800, uppercase, tracking 0.04em, sized to span 56% of the stage width, centered on x 960 with its baseline at y 600. Lab line Syne 600, 24px, uppercase, tracking 0.16em, top-left at (96, 104). Caption Syne 500, 36px, centered under the word at y 700. Readout JetBrains Mono 400, 22px, at (96, 1000).

Simulation: Gray–Scott on a 640×360 grid (one cell = 3px) in Karl Sims' form: 3×3 Laplacian (center −1, edges 0.2, corners 0.05), Du 1.0, Dv 0.5, dt 1.0, zero-flux borders. Start at U 1, V 0. Draw the word into a 640×360 mask at a third of its display size and position. Until 7.2s every step re-imposes U 0.5, V 0.25 inside the letters (with ±3% fixed seeded noise), so the letters are the source the pattern grows from. Feed and kill: coral, F 0.0545 and k 0.062, until 5.2s; then a glide to fingerprint, F 0.037 and k 0.060, by 7.0s (easeInOutSine). At 7.2s the letters stop seeding (reset to U 1, V 0) and an extra decay of −0.05·m·V per step switches on, where m is 1 within 26 cells of the letters or the caption box and feathers to 0 over 12 more: the pattern recedes from the word with rounded, living ends.

Pace: steps per 1/30s frame ease from 0 to about 40 over 0.6–1.2s, hold, then ease to 0 over 8.4–8.9s, so growth slows to a stop instead of freezing. Tune the rate so the coral reaches every stage edge at about 5.0s, not before 4.4s.

Precompute: run the whole simulation once at load in WebGL2 (RGBA32F ping-pong textures, EXT_color_buffer_float). After each 1/30s frame, write V × 560 (clamped) into one layer of an R8 TEXTURE_2D_ARRAY. seek(t) samples the two nearest layers and blends by the fraction. Keep load under 15s.

Shading, in a full-resolution display shader: bilinear-sample V, then h = smoothstep(0.17, 0.27, V) for crisp edges about 1.5px wide. Treat V as height: normals from central differences (scaled so ridge flanks tilt about 40°), light from the upper left. Color = mix(ground, coral body, h) under 0.55 ambient plus 0.45 Lambert, the crest color on lit flanks, a tight specular (power 48, 30%, in the highlight color), and troughs pulled toward the shadow color by a cheap occlusion term (V blurred over 6 cells, minus V). The ground carries the plate grid: 1px lines every 60px at 7%. The crisp word sits on top in ivory with a 3px ground-colored outline, so it reads against the coral at every moment. The readout reports the live simulation, "GRAY–SCOTT F 0.0545 k 0.0620 STEP 004 800", with F and k counting during the glide.

Camera: a 4% push-in centered on the word across 1.0–8.9s (easeInOutSine).

Premium: a wet-looking lit relief with crisp edges and one hue family, and growth you can watch branch out of the letters. Cheap: a blurry upscaled grayscale field, a rainbow colormap, a pattern that already fills the frame on frame one. Banned: rainbow or hue-cycling colormaps, visible grid pixels or stair-steps, blur upscaling, glow or bloom, noise reseeded per frame, a word that ends illegible, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: ground and plate grid; the lab line and readout type on at 30ms per character; the word rises 18px out of a mask, letters 50ms apart.
- 0.6–1.4s: the step rate ramps up and the first coral buds push out of every letter edge.
- 1.4–5.2s: coral branches outward, tips splitting, and touches every edge at about 5.0s; the push-in runs.
- 5.2–7.0s: F and k glide; the branches fuse into parallel fingerprint ridges that wrap the letters; the readout counts to the new values.
- 7.2–8.6s: the letters stop seeding and the pattern pulls back from the word and caption; the caption rises 12px and fades in at 7.8s (0.6s, easeOutCubic).
- 8.4–8.9s: growth slows to a stop.
- 8.9–10.0s: hold the finished plate.
Other lengths: stretch the growth phase first; keep the glide at least 1.5s and the hold at least 1s.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative (growth, simulation, particles) is precomputed once at load at a fixed step or solved analytically, so seek can jump to any time. Past the end, hold the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Engine: one WebGL2 canvas for the simulation and the shading (preserveDrawingBuffer: true, drawn once per seek); the word, lines and readout are HTML on top. No three.js.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the coral visibly branches out of the letters rather than appearing everywhere at once, reaches every edge by about 5s, never dies out or floods into a solid sheet, shows no stair-steps or banding at 1280×720, and leaves a clean clearing around the word and caption. The readout must match the parameters in use. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
