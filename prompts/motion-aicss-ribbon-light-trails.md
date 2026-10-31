# Ribbon Light Trails


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/ribbon-light-trails) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/ribbon-light-trails) · [对应动效输出](https://www.aicssanimations.com/previews/ribbon-light-trails.mp4)

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
<inputs>
- WORD. Default: "NOCTURNE".
- TAGLINE. Default: "Light & Sound · 14 November".
- COLORS. Default: cool #47C8FF and warm #FF8A5B ribbons.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Ribbons of light sweep through deep space, spiral inward and converge to ignite a word, like a festival or launch ident.
- Ribbons: 14, alternating cool and warm. Each is a CatmullRomCurve3 through 6–8 seeded points: it starts far off-screen (z −40 to +8), arcs through frame, passes behind the word, then runs on as a long, gently undulating tail exiting right. Build each as a camera-facing flat strip of 400 segments with one slow twist so it goes edge-on and glints; width tapers with sin(πu), 0.22 units max.
- Shading: ShaderMaterial, AdditiveBlending, depthWrite false. A per-ribbon head uniform; visible span [head − 0.38, head] along u, smoothstepped to 0 at the tail, shifting to #FFF4E8 in the last 4% at the head. Far ribbons dim to 35%.
- Bloom: EffectComposer, RenderPass, UnrealBloomPass (strength 0.7, radius 0.45, threshold 0.15), OutputPass. Bloom is a halo, not fog; cores stay crisp.
- Background: #04030A with a faint radial #120C26 behind center; 500 seeded dust motes (0.5–1.5px, 10–25% alpha) parallaxing slowly.
- Camera: fov 35, z 14 → 11 over the piece (easeOutQuart), no shake.
- Type (HTML over the canvas): word in Sora 300, 168px, letter-spacing 0.24em, white, revealed by a left-to-right mask whose edge tracks the arriving heads, text-shadow 0 0 28px rgba(255,220,200,0.45). Tagline Sora 400, 22px, uppercase, letter-spacing 0.3em, #B9B4D6.
- Motion: heads travel on easeInOutCubic over 2.6–3.4s, starts staggered 0–1.4s, decelerating as they converge; afterwards they slow to 10% speed so light keeps moving while the composition holds.
Banned: lit TubeGeometry (reads as pipes), rainbow gradients, lens flares, shake, a white-out at convergence (brightness may rise 15% at most), kinked curves, glow that swamps the word, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: dust only.
- 1.0–3.4s: six ribbons sweep in long arcs from top-left and lower-right depth, crossing.
- 3.4–5.4s: the rest enter; curves tighten into a spiral around center.
- 5.4–6.6s: heads converge behind the word; letters reveal left to right.
- 6.6–8.4s: ribbons flow on into slow horizontal streams behind and below the word.
- 8.4–9.2s: tagline rises 10px and fades in.
- 9.2–10.0s: hold; streams drift at low speed.
Scale beats proportionally for other lengths.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- three.js as an ES module from a CDN, version pinned (import map: `three` and `three/addons/` to three@0.160.0 on jsDelivr). WebGLRenderer with preserveDrawingBuffer: true; render once per seek call.
- Call composer.render() once per seek in place of renderer.render().
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. Keep the word legible over the streams, tails soft, curves free of kinks, and the convergence frame not blown out. Confirm the final frame holds as a composed end card.
</check>
```
