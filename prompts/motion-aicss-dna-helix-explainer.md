# DNA Helix Explainer


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/dna-helix-explainer) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/dna-helix-explainer) · [对应动效输出](https://www.aicssanimations.com/previews/dna-helix-explainer.mp4)

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
Make a 10-second 3D science explainer: a DNA double helix turns, its parts get labeled, then it unzips and copies itself.

<inputs>
If I don't give you something, use the default and don't ask.
- Series: Small Machines, from Oakmere Learning (fictional).
- Title: "How DNA copies itself"
- Captions, in order: "Two strands, paired A–T and G–C." · "Helicase unzips the pairs." · "Each strand is a template for a new one." · "Two copies, each half old and half new."
- Sequence (strand 1, 5′ to 3′, 36 bases): ATGCGTACCTAGGCTAATCGGATCCATGCAATTGCC
- Length: 10 seconds.
</inputs>

<direction>
- Look: a clean textbook model in matte clay on a pale ground, lit like a studio product shot. Background #F3F5F7 with a soft #FFFFFF radial lift behind the helix; a ShadowMaterial floor 1.8 units below catches a soft contact shadow (opacity 0.12) from a high key light (PCFSoftShadowMap), with a HemisphereLight fill.
- Palette: parent strands ink #26304F and slate #5C6A8A; new strands coral #EE6A4D; adenine #E9A23B, thymine #3FA391, guanine #5B7FD6, cytosine #D8607C; hydrogen-bond dots #9AA3B5; text #1B2133, secondary #5E6678. MeshStandardMaterial, roughness 0.65, metalness 0.
- Geometry, true to B-DNA at 1 unit = 1 nm: right-handed, 10.5 base pairs per turn, 0.34 rise per pair, radius 1.0 (2 nm wide). Strand 2's backbone sits 150° (not 180°) around the axis from strand 1's, so a wide major groove alternates with a narrow minor groove and each rung is the straight chord between the backbones. Backbones are chains of phosphate beads (radius 0.11) joined by short capsules (radius 0.055), all instanced, so any deformation is just new endpoints. Each base is a rounded slab (RoundedBoxGeometry) from its backbone to just short of the rung's midpoint, colored by base; the gap holds two bond dots for A–T and three for G–C. The strands run antiparallel: small 5′ and 3′ labels mark the ends.
- Layout: the helix lies horizontally, centered on y 540, 1,400px long; camera fov 28, 10° above. The whole model turns about its own axis at 20°/s, easing to rest by 8.8 s.
- Replication, computed per nucleotide from the fork position f(t), with s = x − f: ahead of the fork (s > 0) the parent helix; at the fork a helicetase ring (a slate torus, radius 0.9, tube 0.3) that the strands pass through; behind it the two templates part into a Y, the upper rising and the lower falling, untwisting as they go. From 0.6 units behind the fork, new nucleotes snap onto each template one at a time: each flies in from 0.4 units out and scales 0.7 → 1 over 0.25 s (easeOutBack, 3% overshoot), joining a new coral backbone. From 2.4 units behind, each template and its new strand twist back into a complete daughter helix. Pairing is always correct: A with T, G with C.
- Type (HTML over the canvas): kicker "SMALL MACHINES · 01" in Schibsted Grotesk 600, 20px, tracked 0.14em, coral; title Schibsted Grotesk 700, 64px, top-left at (120, 96); captions Schibsted Grotesk 500, 34px, bottom-left with the baseline at y 960, one at a time, crossfading with a 10px rise. Labels in Schibsted Grotesk 500, 22px, each on a 1px #9AA3B5 leader ending in a 5px dot on the exact part it names, following it as the model turns; never more than three at once.
- Easing: fork and camera on easeInOutSine; text in over 0.5 s on cubic-bezier(0.22, 1, 0.36, 1). One idea at a time.
- Premium: correct grooves and handedness, antiparallel ends, pairs that obey the rules, soft daylight shadows. Cheap: a glowing blue ladder twisting in a particle void. Banned: a left-handed helix, a symmetric ladder with no grooves, mismatched pairs, glow, bloom, particles or bokeh, dark backgrounds, chrome, colors beyond the palette, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: the base pairs click in from left to right, 25 ms apart, as the helix turns; the backbones draw along with them.
- 1.0–2.0s: the kicker and title rise in; the first caption appears.
- 2.0–3.8s: three labels attach 0.2 s apart: "Sugar-phosphate backbone", "A–T: two hydrogen bonds", "G–C: three hydrogen bonds".
- 3.8–4.2s: the labels clear; the second caption; the helicase ring slides onto the left end.
- 4.2–7.8s: the fork runs left to right along the whole helix (easeInOutSine) and new nucleotides snap in behind it; the third caption appears at 5.4 s.
- 7.8–8.8s: the helicase slides off the right end; the two daughter helices finish twisting and settle with their axes 3.0 units apart while the camera eases back 10% so both fit between title and caption; a small key ("old strand" in ink, "new strand" in coral) and the last caption rise in.
- 8.8–10.0s: hold, still. For other lengths, stretch the fork run first; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Every nucleotide's transform is a function of t and the fork position f(t), set on InstancedMesh matrices each seek.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the helix is right-handed (it twists like a standard screw thread), the grooves alternate wide and narrow, every pair is A–T or G–C with the right number of bond dots, each label points at the right part, and both daughter helices sit inside the frame clear of the type. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
