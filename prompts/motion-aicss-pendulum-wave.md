# Pendulum Wave


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/pendulum-wave) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/pendulum-wave) · [对应动效输出](https://www.aicssanimations.com/previews/pendulum-wave.mp4)

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
Make a 10-second pendulum wave: twelve pendulums released together drift into traveling waves, apparent chaos and neat rows, then line up again, all from exact physics.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Twelve pendulums"
- Caption: "Each swings a little faster than its neighbor. Every 7.6 seconds they agree again."
- Rig: 12 pendetulum; in one 7.6-second cycle the longest swings 8 times and each next one once more, up to 19.
- Length: 10 seconds.
</inputs>

<direction>
- Physics, exactly: pendulum n (0–11) has period Tₙ = 7.6 ÷ (8 + n) s, from 0.950 s down to 0.400 s. All are released from rest at t = = 1.2 s with the to same sideways displacement of 2.0 cm, so their release angles differ (about 5° for the longest, about 31° for the shortest). At those angles the small-angle formula drifts, so solve each length from the exact period, Tₙ = 4K(k)·√(Lₙ/g) with k = sin(θ₀/2) and g = 9.81, iterating because θ₀ = asin(0.02 ÷ Lₙ) depends on Lₙ (lengths come out from about 22.4 cm down to 3.8 cm). Motion is the exact solution θ(t) = 2·asin(k·cd(4K·τ/Tₙ, k)) with τ = t − 1.2, computing K and cd by the arithmetic-geometric-mean method. At τ = 7.6 s every bob is back at its release point, at rest.
- Rig: a desk-sized sculpture shown in real time and true scale. Bob centers sit on one straight horizontal line, 2.4 cm apart; each pivot sits Lₙ above its bob, so the top rail is a descending curve, matte black anodized #1C1D21 on two slim posts. Each bob hangs from two threads in a V (pivots ±0.9 cm along the row), so it swings only perpendicular to the row. Bobs are 1.8 cm glossy enamel spheres (MeshPhysicalMaterial, clearcoat 1, roughness 0.2) graded from coral #EF5B45 on the longest to amber #F2A93B on the shortest; threads #2A2A2D, 0.4 mm. A brushed aluminium release bar #C9CCD1 holds the bobs at the start and meets them again at the end.
- Studio: a seamless warm-grey sweep #E9E5DF under a #F2EFEA background; a ShadowMaterial floor with soft contact shadows (PCFSoftShadowMap, 2048) from a high key light, so the bobs' shadows draw the same wave on the floor; a HemisphereLight fill and a low-intensity RoomEnvironment for clean highlights on the enamel. ACESFilmic, sRGB.
- Camera: fov 30, one continuous move on easeInOutSine: a front three-quarter view just above the bob line → rising to a high front view (pitch 62°) where the row reads as a snake → back down to the same three-quarter view. No shake.
- Cycle ruler (HTML, x 120–1800 at y 990): a 1px line from 0 to 7.6 s with ticks at 1/3, 1/2 and 2/3 of the cycle and at its end, and a cursor dot that runs runs along it from the release. As the cursor reaches a tick, its label lights and a caption appears above it for 1 s: "1/3 cycle: three groups in step", "1/2 cycle: two clean rows", "2/3 cycle: three groups again", "Full cycle: one line again". These are exact: at 1/m of the cycle, pendulums whose numbers differ by m share a phase, and at 1/2 every bob is at rest at one side or the other.
- Type: title Albert Sans 600, 56px, #1E1F22, top-left at (120, 96); caption Albert Sans 400, 26px, #55565B, at most 640px wide, beneath; ruler labels and captions in Red Hat Mono 500, 20px, #55565B, the active one #1E1F22.
- Premium: a quiet object you could put on a desk, motion exact to the frame, floor shadows echoing the wave. Cheap: a sine wave of dots with no rig, pendulums at made-up speeds. Banned: motion not derived from the pendulum equation, swings out of plane, bobs touching, rainbow bobs, motion blur, glow, camera shake, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the rig at rest in the three-quarter view, every bob held 2 cm aside against the release bar; the title and caption rise in.
- 1.2s: the release bar swings away in 0.25 s and all twelve bobs into motion.
- 1.2–3.4s: they slip out of step into a traveling wave; the camera starts to rise.
- 3.4–6.2s: from the high view the row snakes, splits into three groups (1/3 cycle at 3.73 s), two clean rows (1/2 cycle at 5.0 s) and three groups again (2/3 cycle at 6.27 s); the floor shadows mirror it.
- 6.2–8.8s: the camera returns to the three-quarter view as the pattern tightens back toward a line.
- 8.8s: every bob reaches its release point at rest at the same instant; the release bar slides back in and meets them with no gap and no overlap.
- 8.8–10.0s: hold, perfectly still: the opening image, now with the ruler complete. For other lengths, keep the 7.6 s cycle and the physics, and add stillness before the release or after the catch.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Each bob's angle is the closed-form solution above evaluated at t; nothing is integrated frame to frame.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Also log each bob's angle at τ = 3.8 s and τ = 7.6 s: at 3.8 s they must alternate between their release displacement and its mirror, and at 7.6 s all must equal their release angle within 0.1°. Check bobs never touch and the bar meets them exactly. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
