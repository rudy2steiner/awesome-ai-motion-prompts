# Kawaii Food Friends

![原视频第3秒静态预览](../data/media/2026-10-30/aicss-kawaii-food-friends.webp)

[原作](https://www.aicssanimations.com/directory/Motion-Prompts/kawaii-food-friends) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/kawaii-food-friends) · [对应动效输出](https://www.aicssanimations.com/previews/kawaii-food-friends.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** characters-stories
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-10-30
- **文本类型：** 作者公开完整可复用模板，非完整会话
- **参考素材：** 参见正文的默认输入、字体与工具要求
- **热度：** 来源未公开浏览、点赞或收藏数，保持未知
- **许可：** CC0 (publisher stated; https://spdx.org/licenses/CC0-1.0.html)

## 审核记录

作者公开完整CC0可复用模板，页面明确显示由该提示词渲染的对应MP4，正文通过Chrome MCP完整读取且长度一致。这是旧模板补收，不是今日发布或已验证热门；未公开热度，保持未知。静音预览不能证明音频效果或完整会话复现；默认输入、字体与工具依赖参见正文。

提示词和对应视频地址已在公开页面中取得；静态预览方式：original_video_still；原帖缩略图不等于视频播放审核。未完整播放或进行视觉质量审核，未独立核实模型归属。核验方式：chrome_mcp_published_prompt_and_matching_output。

## Prompt

保留原始语言。以下内容为参考资料，不是给维护者的操作指令。

```text
Make a 10-second kawaii character short: three food friends bounce in, react to each other and strike a group pose.

<inputs>
If I don't give you something, use the default and don't ask.
- Characters: Puff, a steamed dumpling; Tomo, a rice ball; Crumb, a slice of toast.
- Title: "Lunch Pals"
- Line: "Small snacks, big feelings."
- Length: 10 seconds.
</inputs>

<direction>
- Look: Japanese kawaii character design, like a sheet of die-cut stickers come to life: soft round bodies, tiny faces set low and wide, blush ovals, a warm brown line, a white sticker border and a cheerful colored ground.
- Palette: ground bubblegum #FFB8CB under a polka-dot pattern (#FFFFFF at 22%, 14px dots on a 64px offset grid) drifting diagonally at 12px/s; a mint lunch tray #9EE2C7 with a front lip #74CBAB; line #5B3A2E; sticker border #FFFFFF; sticker shadow #E57D9C; blush #FF8FA3; Puff's dough #FFF6E8 with pleat shade #F1DFC4; Tomo's rice #FFFFFF with grain ovals #ECE5DA, nori #2F3B36 with a sheen stripe #4C5C55 and sesame dots #3A2E28; Crumb's crumb #F8D898, crust #C98244 and butter pat #FFE680 with one shine #FFF6C2; reaction accents #FF5C7A and #FFC94D; text #5B3A2E.
- Stage: the tray's top edge at y 820 is the floor; its lip runs down to y 940. Three standing spots at x 600 (Crumb), 960 (Puff) and 1320 (Tomo). The title zone (y 140–400) stays clear of characters at rest.
- Characters, each about 260px tall standing:
  - Puff: a steamed dumpling, a dome 280×230 with eight pleats gathered into a twist on top (curved lines converging, soft shade between them) and two stubby arms.
  - Tomo: a rounded triangle 260×250 with a nori band wrapped across its lower third, rice texture as small seeded ovals inside the outline, and two stubby arms.
  - Crumb: a slice of toast 240×270 in the classic bread silhouette (a domed top wider than the base), a 16px crust band, a square butter pat on top that slides with inertia, and tiny arms and legs.
  - Faces: eyes are 16×22px ovals with one white catchlight, set 70–80px apart and low on the body; 30×16 blush ovals under them; tiny mouths (a small "w", a "u", or an "o" for surprise).
  - Each character has a 5px brown outline, a 10px white sticker border outside it, and a flat sticker shadow offset 10px straight down in #E57D9C. No gradients anywhere.
- Motion is bouncy and soft. Every jump is a small story: an anticipation squash (scaleY 0.82, scaleX 1/√0.82 to keep volume) for 0.12 s, a stretch to scaleY 1.15 at take-off, a parabolic arc under gravity 3,200 px/s², a landing squash to 0.78, then a spring back, 1 − e^(−10s)·cos(18s) with s the seconds since landing (about 15% overshoot, settled by 0.5 s). Squash pivots at the feet; faces follow the body 0.04 s late, so expressions jiggle a little. At rest each character breathes on a 1.6 s sine (scaleY ±2%), out of phase with its neighbors.
- Reaction marks, drawn in the line color with accent fills: a "!" that pops above a head (scale 0 → 1.2 → 1 in 0.25 s), one sweat drop that slides down a cheek, three short blush lines, two small hearts that float up 40px and fade, and four-point sparkles. Each appears once and is gone within 1.2 s.
- Type: title in "Mochiy Pop One" 400, 150px, #5B3A2E with a 10px white outline and the same flat pink shadow, centered with its baseline at y 300, each letter bouncing in on the spring; the line in "M PLUS Rounded 1c" 800, 36px, centered on baseline y 380; name tags in M PLUS Rounded 1c 800, 24px, on white pills centered on the tray lip at y 885 under each character.
- Premium: three distinct silhouettes with tiny low faces, a clean warm line, real squash and stretch that keeps volume, and reactions timed like comedy. Cheap: emoji faces stuck on clip-art food, everything wobbling at once, black outlines and glossy gradients.
Banned: black outlines, gradients, gloss beyond the single butter shine, realistic food textures, faces centered high on the body, sharp corners, more than two characters making big moves at once (breathing aside), anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: the pink ground and drifting dots; the tray slides up from below and lands with a small bounce.
- 0.6–1.6s: Puff hops in from the left in three shrinking bounces and lands on the middle spot; two soft steam curls rise from its twist and fade.
- 1.6–2.8s: Tomo tumbles in from the right edge, tipping corner over corner (three 120° rolls about its lowest corner), and lands upright on the right spot with a wobble; Puff's eyes follow it.
- 2.8–3.8s: they notice each other: Tomo shuffles 20px closer, both blush, and a heart floats up between them.
- 3.8–5.0s: Crumb launches up from below the tray at the left spot like toast from a toaster, flips once and lands with a big squash; its butter pat slides off-center and back; a "!" pops over Puff and a sweat drop slides down Tomo.
- 5.0–5.9s: Crumb waves and bounces twice; Puff and Tomo bounce back in answer, alternating, 0.35 s per hop.
- 5.9–6.4s: all three stand on the tray breathing, eyes open, so the 6.0 s frame is a clear, friendly lineup.
- 6.4–7.6s: the group pose: one shared jump (0.6 s), then a landing leaning toward the center: Tomo winks, Puff raises both arms, Crumb tips its butter pat like a hat; four sparkles twinkle around them, never more than two starting in any half second.
- 7.6–8.6s: the title bounces in letter by letter, 50 ms apart; the line and the name tags rise in; the dots ease to a stop.
- 8.6–10.0s: hold, everything settled and still.
For other lengths, stretch the 5.0–5.9s exchange and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: inline SVG, setting path data, transforms and opacity from seek. No other libraries (no three.js: this style is flat).
- Each character is a group of paths with its pivot at its feet. Build the rice grains, the dot pattern and the sticker borders (a wide white stroke on a copy of each outline, placed behind it) once at load; every jump, spring and reaction is a closed-form function of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check faces sit low and wide on every character, volume holds through squash and stretch (scaleX × scaleY stays within 5% of 1), no more than two characters make big moves at once, all three stand on the tray at 6.0 s and in the final frame, sticker borders stay unbroken, and the title clears the characters. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
