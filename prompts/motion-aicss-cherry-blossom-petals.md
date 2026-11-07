# Cherry Blossom

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/cherry-blossom-petals) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/cherry-blossom-petals)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second scene of a cherry branch in full bloom against a pale spring sky, petals letting go and tumbling down on the wind.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Ten Days of Blossom"
- Line: "Ilsey Gardens · 2–11 April" (fictional)
- Wind: a light breeze, with one gust crossing at 4.2 s.
- Length: 10 seconds.
</inputs>

<direction>
- Palette: sky #EAF1F6 at the top to #F8F1EE low down, with a faint warm haze; distant trees in bloom as soft masses #F4D7DE and #E9C3CF at 40%; bark #3B2B2A with lit edges #6B5450 and lenticels #8A7570; twigs #5A3A34; petals white #FFF8F8 flushing to #F7D3DC at the base; flower eyes #E58FA6; stamens #F5D5DF with anthers #F0C66A; buds #E7849D; young leaves bronze-green #9C8A4E; title #3A2A33, line #7B6570.
- The branch: it enters from the upper-left corner and reaches across to about x 1500 with three side twigs, drawn as tapered strokes: a dark core, a lit upper edge, short horizontal lenticel dashes (the mark of cherry bark), a few knots and short spurs. It stays within y 100–580.
- Flowers: 26 clusters of 3–5 flowers (about 95 in all) hanging on 20–40px stalks from the spurs, plus buds and a few young bronze leaves. Each flower has five rounded, slightly cupped petals with a small notch at each tip (that notch is how you tell a cherry), a pink eye, and 20–30 stamens with yellow anthers. Flowers face every way: some open to the camera, some side-on as ellipses, some showing their backs and reddish calyx. Draw each flower once at load as a sprite, then place it with its stalk's sway every frame.
- Depth: three planes: the hero branch, sharp; a second branch in the near foreground at the lower right, blurred 14px, with large flowers; and the far trees as blurred masses across the bottom (y 700–1080). Falling petals take size and blur from their depth: far ones small and softened, mid ones sharp, near ones large and soft.
- Petals: about 420 fall over the piece, each a real 3D petal (the notched outline as 24 points, slightly cupped) with position, velocity and orientation, simulated once at load at a fixed 1/120 s step from t = −4 s: gravity; drag split into a strong part across the petal's plane and a weak part along it; and a torque that pitches the leading edge up as it glides, so petals flutter side to side and some tumble end over end (one in three, at 0.8–2 turns a second). In still air they fall at 90–200px/s. Each frame, rotate the outline by the orientation and project it with a mild perspective, so a tumbling petal narrows to a sliver and flips. Shade it by how it faces the soft light from the upper right; when its back faces the light, tint it #F4BFCB, as light comes through a thin petal.
- Release: each falling petal leaves a specific flower, which keeps the gap. Petals let go at about 12 a second, rising to 90 a second during the gust, starting with their flower's orientation and the twig's sway.
- Wind: a 50px/s breeze to the right plus seeded curl noise; the gust raises it to 260px/s, rising over 0.5 s and decaying over 1.2 s, and travels across the frame left to right at 800px/s, so petals and twigs on the right react later. Each branch segment and stalk is a damped spring (period 1.6 s for the branch, 0.6 s for stalks, damping ratio 0.25) driven by that wind and solved at load; at the gust the branch tip swings about 26px and settles in two or three smaller swings.
- Type (HTML over the canvas): title in Zen Old Mincho 600, 84px, #3A2A33, baseline at (120, 930); line in Zen Kaku Gothic New 500, 24px, tracked 0.16em, #7B6570, baseline at (122, 980). Each rises 10px as it fades in over 1.0 s on cubic-bezier(0.22, 1, 0.36, 1). Mid and far petals may pass behind the type; near petals stay out of the region x 100–1000, y 820–1010.
- Premium: notched five-petal flowers with real stamens, bark with lenticels, petals that flutter and flip instead of sliding, depth from focus, a gust you can watch cross the frame. Cheap: pink ellipses drifting diagonally at constant speed over a pink gradient.
Banned: petals without the notch, heart shapes, sparkles, glow, saturated hot pink, mountains, temples, gates or lanterns, petals falling in straight lines or never landing, motion blur, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the branch in full bloom in a light breeze, a few petals already drifting down.
- 1.2–2.6s: the title and line rise in.
- 2.6–4.2s: a dozen petals let go and flutter down through the three depth planes; the view drifts 20px left on easeInOutSine.
- 4.2–6.2s: the gust crosses left to right: the twigs swing, the flowers bob, and a flurry of petals tears off and streams to the right, tumbling and flipping across the right half of the frame.
- 6.2–8.4s: the flurry sinks and thins; the branch settles in smaller swings; a few late petals let go.
- 8.4–10.0s: hold: the branch still, the breeze light, a few petals drifting down.
For other lengths, stretch 2.6–4.2s and 6.2–8.4s; keep the gust and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. Text is HTML over the canvas.
- Draw petals into three layer canvases (far, mid, near) and blur the far and near layers with one ctx.filter pass each per frame. The petal and spring simulations are precomputed into Float32Arrays at load; seek(t) only reads and interpolates them.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the notches show on petals at 1280×720, tumbling petals visibly flip and narrow, flowers that lost petals keep their gaps, the gust reaches the right side after the left, nothing falls in a straight line, and the title reads cleanly. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
