# Particle Text Morph


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/particle-text-morph) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/particle-text-morph) · [对应动效输出](https://www.aicssanimations.com/previews/particle-text-morph.mp4)

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
Make a 10-second particle morph: about 2,400 crisp colored particles flow from word to word, then sort themselves by color into a logo mark.

<inputs>
- Words: MANY, then PARTS.
- Brand: Fourfold (fictional). Tagline: "Many parts, one shape."
- Mark: four quarter-disc petals, one per color.
- Colors: ultramarine #2B3FE0, coral #FF5A4E, jade #11A38B, saffron #F5B700.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: ground #FBFAF7, ink #17181C for the wordmark, and the four colors, each carried by exactly a quarter of the particles. Nothing else.
Type: Syne 800 for the particle words (each sized to 1,400px wide) and the wordmark (96px); Syne 500 for the tagline (32px).
Particles: N = 2,400 opaque discs of 2.8px radius, colors assigned by a seeded shuffle (600 each). At speed each stretches along its velocity into a capsule up to 2.2× its diameter, returning to a round dot as it slows.
Targets: render each word, and the mark, to an offscreen canvas and sample its inside on a grid jittered by ±10% of its pitch: binary-search the pitch until the count is just over N, then drop the extras in a seeded order. Spacing stays even, with no clumps or holes. Center each shape at (960, 470).
The mark: a 400px square split into quadrants, each holding a quarter disc of radius 196px centered on the square's outer corner, so the four arcs face inward and leave a four-pointed star of empty ground in the middle; top left ultramarine, top right coral, bottom right jade, bottom left saffron.
Assignment decides the look. Between words, sort both point sets along a Hilbert curve and pair them by rank, so neighbors stay neighbors and the paths flow as one current. Into the mark, assign by color: each color's 600 particles go to their own petal, paired by Hilbert rank within the color, so the mixed confetti sorts itself into four clean quarters.
Paths: each particle follows a quadratic curve whose control point sits off the straight line by 12% of its length, all bending the same way within a morph and alternating between morphs. Travel takes 1.0s on cubic-bezier(0.65, 0, 0.35, 1) (1.2s into the mark), started with a stagger of up to 0.45s by the target's x, so each shape forms in a left-to-right wave. No overshoot and no stragglers: every particle lands within its window.
Idle: between morphs each particle circles its target on its own seeded orbit (radius 1.5px, period 2–3s), so the shapes breathe without blurring; the orbit fades to zero for the final hold.
The real thing looks like a choreographed flock: even spacing, coherent currents and every particle with a place. The cheap version is glowing dots exploding and collapsing, with clumps and late stragglers.
Banned: glow, blur, additive blending, gradients, particles piling into blobs, explosion bursts, 3D rotation, dark grounds, stragglers, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–1.0s: the particles fade in (opacity only, 0.6s) scattered over the stage on a seeded Poisson-disc spread, drifting slowly.
1.0–2.45s: they flow into MANY in a left-to-right wave.
2.45–3.4s: MANY holds, breathing.
3.4–4.85s: MANY flows into PARTS, swirling the other way.
4.85–5.8s: PARTS holds.
5.8–7.45s: PARTS flows into the mark, the colors sorting into their petals as they travel.
7.4–8.4s: the wordmark rises 16px out of a mask, centered at y 790, then the tagline at y 860, 0.2s later.
8.4–9.0s: the idle orbits ease to zero.
9.0–10.0s: hold.
For other durations, lengthen the holds between shapes, keep each morph at 1.0–1.2s, and hold at least 1s.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries (no three.js: this style is flat). Draw in Canvas 2D, repainting every frame from scratch, with the backing store sized from the CSS size × devicePixelRatio. Canvas won't fetch fonts itself: await document.fonts.load() for each face, then sample the targets, then define window.seek.
The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps.
window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. Sample every target set and solve every assignment once at load; each particle's position is then a closed-form function of t.
Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Also seek a few mid-morph times. Check both words read cleanly at 1280×720 with even spacing, mid-morph frames show coherent currents rather than a tangle, no particle arrives after its shape reads, each petal holds only its own color, and the wordmark clears the mark. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
