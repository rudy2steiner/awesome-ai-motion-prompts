# Domino Chain Reaction


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/domino-chain-reaction) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/domino-chain-reaction) · [对应动效输出](https://www.aicssanimations.com/previews/domino-chain-reaction.mp4)

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
Make a 10-second domino chain reaction: a spiral of dominoes topples with true cascading timing, then grows into giant dominoes that fall flat to spell a word.

<inputs>
- Word: NUDGE (4–6 letters, one per giant domino).
- Line: "One small push starts everything."
- Brand: Kindling Studio.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Set: a matte cobalt table #2B47B8, vignetted to #1C2F80. Dominoes are ivory #F3EEE2 with ink #1C1D24 pips on the forward face; the back face (facing back along the chain) is painted, so fallen ones show only paint from above, ramping coral #FF6A4D → marigold #FFB531 → pink #FF8DB8 along the spiral. The giants' painted faces each carry one Archivo Black letter, upright from the final camera.
Real scale: 48 × 24 × 7.5 mm dominoes, g = 9.81 m/s², 30 mm pivot to pivot, so the wave settles near 1 m/s. About 160 wind outward from the center on an Archimedean spiral 60 mm between turns, leave on a curve that straightens to run left to right, grow 1.4× per domino for five steps, then end in a row of giants spaced 0.85× their height, so each lands almost flat.
Physics, solved once at load at a fixed 1/2000 s step, no library: each domino tips about its front bottom edge, I·θ'' = m·g·r·sin(θ − θc), r = ½√(h² + t²), θc = atan(t/h), I = m(h² + t²)/3. When its top reaches the next, that one starts from a mostly inelastic impact and the striker rides on it, its lean solved from contact geometry, so the trail settles into an even shingle. Tune count and the ball's timing so the last giant lands by 8.4s.
A steel ball rolls in and taps domino 1. A warm upper-left key with soft shadows.
Camera: fov 32, starting low (20°) at the center, aimed at the wavefront averaged over the last 0.4s, climbing on easeInOutSine to 72° by 8.4s: the fallen spiral upper left, the word across the lower half at 55% of frame width.
Type (HTML): the line in Schibsted Grotesk 600, 38px, #F3EEE2, left-aligned with the word, 70px below it; the brand under it in Schibsted Grotesk 500, 22px, uppercase, tracking 0.18em; both rise 14px over 0.5s, easeOutCubic.
Premium is timing you can feel: a wave that gathers speed then holds it, big dominoes falling slower, every piece resting on the next. Cheap is dominoes rotating on a fixed timer like a stadium wave.
Banned: falls on a fixed interval, pieces passing through each other, floating or sliding dominoes, motion blur, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: low over the table at the spiral's center; the ball rolls in and taps the first domino.
- 0.8–5.8s: the wave runs outward round the spiral at a steady pace; the camera follows and climbs.
- 5.8–6.9s: the chain leaves the spiral through five growing dominoes, each falling slower.
- 6.9–8.4s: the giants fall left to right, landing almost flat; the word appears letter by letter.
- 8.4–9.0s: line and brand rise in below the word.
- 9.0–10s: hold.
Other lengths: change the spiral's domino count, never the physics; keep 1s of hold.
</structure>

<build>
One self-contained index.html, inline CSS and JS, on a 1920×1080 (16:9) stage scaled to fit the window, built for 60fps. Google Fonts via <link>, awaited with document.fonts.load() before seek exists.
window.seek(t) sets every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Simulate the toppling once at load and store angles at 1/240 s; seek(t) only reads them.
Without ?render in the URL, drive seek from requestAnimationFrame; with ?render, don't start that loop.
three.js as an ES module pinned to three@0.160.0 via a jsDelivr import map (`three`, `three/addons/`); preserveDrawingBuffer: true; one render per seek. No image, model or typeface files beyond Google Fonts.
</build>

<check>
Before showing me, step through one frame per second (0–10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style or Banned. Look for a wavefront that stutters, dominoes moving before they are struck, intersecting or floating pieces, letters out of order or upside down. Confirm the final frame holds.
</check>
```
