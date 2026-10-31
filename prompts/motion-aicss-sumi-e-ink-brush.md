# Sumi-e Ink Brush


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/sumi-e-ink-brush) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/sumi-e-ink-brush) · [对应动效输出](https://www.aicssanimations.com/previews/sumi-e-ink-brush.mp4)

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
Make a 10-second sumi-e ink painting: bamboo stalks, branches and leaves brushed stroke by stroke on rice paper, finished with a red seal.

<inputs>
Title: Bamboo After Rain. Line: "Bends in the storm, stands after it." Studio: Kurohane Ink Studio. Seal character: 竹 (bamboo). Duration: 10s.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Paper: rice paper #F2ECDF, generated once at load: soft mottling and a few hundred faint long fibers. Ink is one ink at three dilutions: dense #141210, mid (55%) and pale (25%), laid with 'multiply'.
Composition: a front stalk in mid ink, 44px wide, rises from below the bottom edge at x 540 and leans right to leave the top edge at x 760; a back stalk in pale ink, 30px wide, rises from x 380 to a cut end at x 470, y 140. Leaves hang down and to the right after rain in three clusters: two dense front clusters on twigs from the upper nodes (around 820, 300 and 700, 520) and one pale cluster behind (around 520, 260). The right 40% stays empty paper apart from the text and seal.
Stalks: segments 140–240px long, shortest at the base, each a single stroke brushed bottom to top: a little wider at the start and end (the stroke's bone), darker along both edges where ink pools, with dry-brush streaks opening through the middle toward the top. Leave a 10px gap between segments; each gap later gets a node, a short dark stroke like a flattened bracket, wider than the stalk.
Branches: thin, quick strokes (6–10px) from the nodes, with small knuckles.
Leaves: each one press-and-lift stroke 140–220px long: it starts light and narrow, swells to full width (24–34px) about a third along, then tapers to a sharp tip. Group them in threes to fives fanning from a twig end, overlapping like the classic 个 and 介 groupings; front leaves in dense ink, back leaves pale for depth.
Brush model: 28 bristles across the stroke. Each bristle lays its own track of small overlapping ellipses along the path, with an ink load that depletes along the stroke; where a bristle runs dry it skips, opening the white streaks of kasure. Width, pressure and ink load follow per-stroke curves. Wet starts bleed 2–3px into the paper (a soft 15% halo). A stroke lands 8% darker and dries to its final tone over 1.5s.
Type, #1C1A17, left-aligned at x 1320: Zen Old Mincho 600, 54px, for the title (baseline 680); Zen Old Mincho 400, 28px, for the line (baseline 730); 22px, tracking 0.12em, for the studio (baseline 790). The seal: a 72px vermilion #B32D2A square at x 1320, y 840, the character reversed out in Zen Old Mincho 900, edges slightly ragged, ink faintly uneven.
Motion is decisive: each stroke is one confident gesture at its own speed (stalk segments 0.32s, leaves 0.16–0.24s, branches 0.12s) on cubic-bezier(0.3, 0, 0.2, 1), so the brush starts deliberately and flicks off, with a 60–100ms lift between strokes. Paint in the painter's order: stalks, nodes, branches, then leaves front to back.
The real thing is economy: every stroke laid once, tone and dryness doing the shading. The cheap version is vector leaves under a brush texture, or a bamboo clip-art silhouette.
Banned: outlines around leaves, uniform stroke widths, flat vector fills, an ensō, cherry blossoms, moons or red suns, brush fonts for Latin text, a second seal, any color besides ink and vermilion, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.6s: paper alone.
0.6–2.8s: the front stalk, six segments brushed bottom to top.
2.8–3.5s: the back stalk in pale ink, four quicker segments.
3.5–4.1s: nodes on both stalks, bottom to top, 50ms apart.
4.1–4.7s: branches from the upper nodes.
4.7–7.2s: leaves: the lower front cluster (5), the upper front cluster (4), then the pale back cluster (4), with a 0.2s pause between clusters.
7.2–8.0s: title, line and studio appear line by line (0.5s each, 0.15s apart) with a 4px blur-to-sharp ink bleed.
8.0–8.3s: the seal presses in: scale 1.05 → 1 and full ink in 0.2s.
8.3–10.0s: hold; the last strokes finish drying by 8.8s, then nothing changes.
For other durations, keep stroke speeds fixed and scale the pauses and holds.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek. No other libraries (no three.js: this style is flat). Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the canvas's CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the font wait matters. At load, precompute every stroke's stamps from the seeded PRNG and render each finished stroke once into its own offscreen canvas; seek(t) draws finished strokes as images and stamps only the stroke in progress. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.
window.seek(t), t in seconds, must compute every visual from t alone, clamping past the end to the last frame: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. Anything cumulative is precomputed once at load from the seeded PRNG at a fixed step, or solved analytically, so seek(t) can jump to any time.
Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check strokes show pressure and kasure rather than uniform ribbons, leaves taper to sharp tips, back leaves read paler and behind, at least 40% of the frame is empty paper, and no two strokes look identical. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
