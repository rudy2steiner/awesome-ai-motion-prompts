# Generative Flow Field


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/generative-flow-field) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/generative-flow-field) · [对应动效输出](https://www.aicssanimations.com/previews/generative-flow-field.mp4)

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
<inputs>
- WORD the particles form. Default: "DRIFT".
- LOGO: optional SVG/PNG; if given, particles form it instead.
- TAGLINE. Default: "Fieldnote Studio — generative identity".
- COLORS. Default: ink #0B0F17, ivory #EDE6D6.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Fine particles ride an invisible current, gather into a word, hold it like a living engraving, let go and gather again. Think pen plotter, not fireworks.
- Palette: two tones only, #0B0F17 and #EDE6D6; depth comes from alpha (0.12–0.55) with 'lighter' compositing.
- Type: render target glyphs offscreen in Archivo Black so the word spans 62% of frame width. Tagline: IBM Plex Mono 400, 20px, letter-spacing 0.12em, 60% opacity.
- Field: 6,000 particles. Write a small seeded 3D simplex noise and take its curl (finite differences, eps 1px) so flow never clumps. Scale 0.0016/px, time axis 0.06/s, a second octave at 2.1× frequency and 0.35 weight, speed 1.8–2.6px per 1/60s step.
- Trails: each particle is a 1px polyline through its last 16 positions, alpha fading toward the tail; batch into a few paths by alpha.
- Forming: sample targets from the glyph mask (alpha > 128, ±2px jitter); sort targets and particles by x before pairing so paths don't scissor. Step = mix(curl × speed, (target − p) × 0.075, w); w rises over 2.4s on easeInOutCubic, each particle's start staggered 0–0.7s left to right. Keep 15% curl during the hold so letters breathe by 1–2px.
- Premium: curved approach paths, feathered edges, density variation, generous empty space. Cheap: straight-line tweens, uniform dots, everything landing at once.
Banned: hue cycling, bloom halos, a third color, trails faked by painting translucent black over the last frame, a word that simply fades in, teleporting particles, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: field only, already flowing (simulate from t = −2s so frame 0 isn't empty), drifting left to right.
- 1.2–4.0s: convergence; the word assembles left to right.
- 4.0–6.0s: hold; letters shimmer, a few strays orbit the edges.
- 6.0–7.6s: dissolve; w falls in a left-to-right sweep and the current carries particles up and out to the right.
- 7.6–9.0s: re-form at 70% size, 40px above center; at 8.6s the tagline rises 12px and fades in beneath (600ms, easeOutCubic).
- 9.0–10.0s: hold the lockup.
For other lengths, scale convergence and holds proportionally; keep the dissolve at 1.2s or longer.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- Engine: Canvas 2D. At load, once Archivo Black has loaded, integrate every particle from the warm-up start at a fixed 1/60s step into a Float32Array; seek(t) reads and interpolates it. Never step particles in the rAF loop.
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. Letters must read clearly at 1080p, the tagline needs room, and the field should have no dead patches or clumps. Confirm the final frame holds as a composed end card.
</check>
```
