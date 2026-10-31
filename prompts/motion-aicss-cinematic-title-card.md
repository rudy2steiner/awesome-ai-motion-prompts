# Cinematic Title Card


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/cinematic-title-card) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/cinematic-title-card) · [对应动效输出](https://www.aicssanimations.com/previews/cinematic-title-card.mp4)

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
If I don't give you something, use the default and don't ask.
- Presenter line: default "Coldwater Pictures presents"
- Title: default "THE LONG QUIET"
- Tagline: default "Some signals take a lifetime to arrive."
- Billing block: default "A FILM BY INES CALDER" / "MUSIC BY HALE ODUYA"
- Release line: default "THIS WINTER"
- Length: default 10 seconds
</inputs>

<direction>
The last card of a prestige drama trailer: dark, patient, expensive.

Frame: a 2.39:1 picture area (1920×803) centered, with solid #000000 bars of 139 px above and below that nothing ever enters. Keep type 10% inside the picture edges.

Palette: teal-black ground, #081214 at the edges to #13262A behind the title; light leaks amber #FF9B3D to #FFD08A; type warm silver #E6DFD2.

Type: title in Cormorant Garamond 600 caps, 96–112 px; tagline in its italic at 34 px. Oswald 300 for presenter and release lines (22–26 px, tracked 0.4em) and the billing block (20 px, tight tracking, line height 1.05).

Texture: grain at ±4% luminance, 10–30 dust specks and an occasional hair, re-seeded at film cadence; a 0.5 px gate weave seeded the same way; a soft vignette. Leaks: large blurred radial gradients composited with 'screen', drifting sideways, peaking slowly. Frame brightness never shifts more than 3% between film frames.

Motion: the picture layer, not the bars, pushes in 1.00 → 1.06 over the piece, easeInOutSine. The title resolves from blur: filter blur 24 → 0 px, tracking 0.45em → 0.24em, opacity 0 → 1, over 2.6 s, easeOutCubic. Other type fades over 0.6–0.8 s with at most a 6 px rise. Presenter line fully visible at least 1.2 s, tagline at least 2 s.

Authentic: deep blacks, slow light, controlled type, film-cadence texture, never heavy scratches.

Banned: lens flares, glitch or RGB split, sepia, camera shake, Cinzel, white flashes, flicker faster than 3 times per second.
</direction>

<structure>
Default 10 s:
- 0.0–1.0: black picture; grain and dust only.
- 1.0–2.8: presenter line fades in centered, holds, fades out by 2.8.
- 2.4–4.4: a light leak blooms from frame right, peaking near 35% at 3.4, then recedes.
- 3.4–6.0: the title resolves from blur, slightly above center.
- 6.0–8.2: tagline fades in below; hold as a fainter leak drifts in from the left.
- 8.2–9.0: billing block and release line fade up in the lower third.
- 9.0–10.0: hold the full card; only grain, dust and the push continue.

Other lengths: stretch holds first; keep the blur resolve 2–3 s and at least 1 s of full card.
</structure>

<build>
- One self-contained index.html, no libraries (three.js from a CDN only when a style truly needs 3D); a 1920×1080 (16:9) stage scaled to fit the window; designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames. Grain, dust and weave come from a seeded PRNG keyed to the film frame, floor(t×24).
- No ?render in the URL: drive seek from requestAnimationFrame so it plays in a browser. With ?render: don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Layers: background canvas (ground, leaks), DOM type (blur, tracking, opacity set in seek), top canvas (grain, dust, weave, vignette).
</build>

<check>
Before showing me, step through one frame per second and look at each. Fix overlaps, clipped or cramped text and anything off-style. Check nothing enters the bars and the title is fully sharp by 6.0. Confirm the final frame holds.
</check>
```
