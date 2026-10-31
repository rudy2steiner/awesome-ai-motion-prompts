# Fluid Spring Interface


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/fluid-spring-interface) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/fluid-spring-interface) · [对应动效输出](https://www.aicssanimations.com/previews/fluid-spring-interface.mp4)

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
Make a 10-second fluid-interface film: a black pill on a phone morphs into a notification, live card and player on springs.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Morrow (a mobile OS concept)
- Tagline: "Interfaces with momentum."
- States: notification "Ana: running 5 min late"; live card "Car arriving in 2 min"; player "Low Tide, Mara Vale"
- Accent: #FF8A3D
- Length: 10 seconds
</inputs>

<direction>
- Stage: warm grey #E9E7E3. A CSS phone left of center: a 470×1000 #111113 body, 64px corners, screen inset 12px, #1B2236 → #3A2140 wallpaper, lock-screen clock in DM Sans 300, 150px, white. Right: a caption column, one word per state ( ("Notify", "Live", "Play") in DM Sans 600, 88px, #1A1A1A, over a 26px line naming the spring.
- The pill is ONE element whose width, height, radius and y each ride a spring, never cross-fading into another shape. Radius = min(height ÷ 2, 48px). Content enters with blur 6px → 0 and scale 0.94 → 1, 60 ms after the container moves; outgoing content leaves in 120 ms.
- Springs: with ω₀ = √(k/m), ζ = c ÷ (2√(km)) and ωd = ω₀√(1 − ζ²), the offset from target is d(t) = e^(−ζω₀t)·(d₀·cos ωd·t + ((v₀ + ζω₀·d₀) ÷ ωd)·sin ωd·t). Carry v₀ across hand-offs so motion keeps momentum. Presets (mass 1): snappy k 420, c 32; bouncy k 300, c 18; gentle k 170, c 24.
- Squash: while width grows fast, height dips up to 4%, from the spring's analytic velocity.
- Player: an #FF8A3D → #E8336E album square, a 24-bar seeded-noise waveform, a scrubber.
- Premium is one continuous object you could touch, overshoot sized to the gesture, text that never wobbles.
Banned: ease-in-out tweens on the pill, overshoot on text, blur above 8px, more than one accent per state, copied OS status icons, emoji, real brand names.
</direction>

<structure>
- 0.0–0.8: Lock screen; pill idle at 126×38.
- 0.8–2.4: The pill bursts into a 400×92 notification (bouncy); caption "Notify".
- 2.4–3.0: It snaps toward pill size without stopping, carrying its velocity on.
- 3.0–5.0: It grows into a 400×190 live card; an ETA bar fills (gentle); caption "Live".
- 5.0–5.6: The card is flicked up (v₀ ≈ −2400 px/s); the spring catches it into the pill, overshooting visibly.
- 5.6–7.6: It expands into a 400×230 player; the waveform moves; caption "Play".
- 7.6–8.4: A swipe dismisses it into the pill, momentum intact.
- 8.4–10.0: The phone eases 60px left; "Morrow" and the tagline replace the caption. Hold.
For other lengths, scale beats but never cut a settle short; drop a state instead.
</structure>

<build>
- One self-contained index.html (inline CSS and JS) with a fixed 1920×1080 (16:9) stage scaled to fit the window; design for 60fps.
- window.seek(t), t in seconds, sets every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames. Randomness comes from a seeded PRNG; springs are closed-form functions of time.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser; with ?render, don't start that loop.
- Google Fonts via <link> are fine. Build it in HTML/CSS with inline SVG; no canvas or three.js needed.
</build>

<check>
Before showing me, screenshot seek(0) through seek(10), one frame per second, and look at each. Fix overlaps, clipped or cramped text, and anything generic. Also step 0.8–1.4 s at 0.1 s: no corner kinks, no content outside the pill, caption clear of the phone. Confirm the final frame holds.
</check>
```
