# Starling Murmuration


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/boids-flocking) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/boids-flocking) · [对应动效输出](https://www.aicssanimations.com/previews/boids-flocking.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** 3d-simulations
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
Make a 10-second starling murmuration at dusk: thousands of birds flow into shapes and out again, then pour down into the reeds.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "The Gathering"
- Line: "Starlings over Reedmoor Fen, 16:52" (fictional)
- Flock: 3,600 birds.
- Length: 10 seconds.
</inputs>

<direction>
- Palette: sky from #5A6797 at the top through #A98FB0 and #E7AE98 to #F6D0A0 at the horizon, with a pale low sun #FFE9C6 half-veiled in haze at x 1500; distant tree line #5C5068 hazed toward the sky; marsh water #E9BC9A reflecting the horizon; reed bed #241F2D; birds #1F1A27 at 80% opacity; title #2A2233, line #4A3F57.
- Landscape: horizon at y 880; a low hazy tree line above it; a thin strip of marsh water from 880 to 925; theet bed fills the bottom from 925, with seeded stems and seed heads standing up to y 840 at the left and right edges. A faint seeded grain (2%) on the sky only, fixed, not boiling.
- Simulation (3D, precomputed): 3400 birds in a 3D volume seen through a perspective perspective camera, simulated at a fixed 1/60 s step from t = −2 s so the first frame is already flowing. Each bird follows Reynolds' rules with topological neighbors, as real starlings do: alignment and cohesion with its 7 nearest birds (found with a uniform grid), separation inside 0.35 units, speed held between 9 and 13 units/s, turning limited to 220°/s, and a soft pull back into the flock's volume. Choreograph it only through invisible targets, never by placing birds: a roost attractor on a slow path, which splits into two targets 2.6 units apart for the hourglass and merges again; a falcon that crosses once and repels birds within 1.5 units; and finally a sink in the reeds that pulls the flock down.
- Drawing: each bird is a short dark stroke 1.4–3.2px long and 1.2px thick, its length following how side-on it is to the camera, with a per-bird wingbeat that changes its length on 5 drawings per second. Dense regions and sheets turned edge-on build up dark bands through overlapping alpha: that rolling darkness is the look. The falcon is one larger silhouette with pointed wings, 14px across.
- Composition: the flock lives between x 160 and 1760 and y 260 and 830, never touching the title or the frame edge. Birds that drop below the reed tops are hidden behind the reed layer.
- Type: title in Newsreader 500 italic, 72px, top-left at (120, 120); line in Karla 500, 22px, uppercase, tracked 0.18em, beneath.
- Premium: one living mass that thickens and thins as it turns, waves of turning sweeping through it, a drop into the reeds like sand through a funnel. Cheap: a 2D swarm of evenly spaced dots, birds clumping and jittering. Banned: a word or logo made of birds, colored birds, V-shaped bird icons or emoji, birds over the title, jitter or teleporting, birds leaving the frame, motion blur, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: a loose stream of birds pours in from the right edge into the dusk sky.
- 1.2–3.2s: it gathers into a tilted teardrop that rolls and folds over itself; dark bands sweep across as the sheet turns edge-on.
- 3.2–4.6s: the falcon cuts through from the upper left; a hollow opens around it and a wave of turning ripples outward through the flock.
- 4.6–6.6s: the flock stretches into a long ribbon, then pinches into an hourglass of two lobes joined by a thin neck.
- 6.6–8.2s: the lobes merge into a dense ball low over the reeds, which funnels down into them; the last birds pour in.
- 7.6–8.6s: the title and line rise 10px as they fade in.
- 8.6–10.0s: hold: an empty, glowing sky over the reeds. For other lengths, stretch the shape beats; keep the drop at least 1.2 s and the hold at least 1 s.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter.
- The flock is simulated once at load at a fixed 1/60 s step from a seeded PRNG into one Float32Array (keep load under 10 s); seek(t) only reads and interpolates it and never steps the simulation.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the flock thickens and thins rather than looking uniform, no birds stack into identical clumps, the flock stays inside its band and off the title, and the drop reads as a funnel into the reeds. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
