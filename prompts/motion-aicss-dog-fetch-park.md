# Dog Fetch

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/dog-fetch-park) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/dog-fetch-park)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** characters-stories
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second cartoon in the 1950s modern style: a scruffy terrier chases a thrown ball across a park, skids, catches it and trots back proud.

<inputs>
If I don't give you something, use the default and don't ask.
- Dog: Pepper, a rust-and-white terrier.
- Owner: only the legs and one throwing hand are ever seen.
- Title: "Good Dog, Pepper"
- Credit: "A Bramblewood Picture" (fictional)
- Length: 10 seconds.
</inputs>

<direction>
- Look: mid-century modern animation: flat graphic shapes, color fills that sit slightly off their loose ink lines, stylized backgrounds of geometric trees and simple planes, dry-brush texture, and limited animation timed on twos. Design over realism.
- Palette: sky cream #F2E5C6; far hills olive #A5A458 and teal #4E8A80; grass #B8B24A with darker tufts #8F8A33; path blush #E9B6A0; tree crowns teal #3F7E78, olive #7E8A3A and mustard #E0A93A on ink stick trunks; bench and lamp post in ink; pond #4E8A80; Pepper rust #D3602A with white patches #FBF4E6, ears and nose in ink; ball red #D63A2C with a cream band; owner trousers navy #2E3A5C, shoes oxblood #6E2A26, a mustard sleeve cuff #E0A93A, hand #E8B38E; ink #1B1916; text #1B1916.
- Off-register color: every fill is its shape, simplified a little and shifted 6px up-left of its ink outline, so color and line never quite meet. Ink lines are 3–5px with a slight seeded taper, broken at a few joints. Fills carry a static dry-brush texture (an SVG feTurbulence mask with a fixed seed), and the grass gets crayon-like tufts.
- Background: a 4,200px pan built once at load in two planes: sky and far hills at 0.4×, and the park at 1.0×: lollipop trees (circles, ovals and tall triangles on stick trunks, each with five short scribbled leaf marks), a bench, a lamp post, a pond as a flat ellipse with three reed strokes, and the path. The owner stands at the pan's left end: long, stylized legs rise from the shoes at y 900 straight out through the top edge of the frame, and the throwing hand reaches down into frame on an arm from the top edge. Nothing above the legs is ever seen.
- Pepper: a terrier designed from angular shapes: a long rectangular body with a squared chest, a lozenge head with a beard block, triangular ears that flop two frames late, a stub tail and four stick legs with oval paws; about 230px long standing, feet on y 900. Eyes are ink dots that become arcs when happy; the mouth opens to hold the ball.
- Limited animation: Pepper's drawings change on twos (the pose index comes from floor(t × 12)), while the camera pan and the ball move on every frame. The run is four drawings (stretch, gather, extension, airborne) at three cycles a second; one drawing per cycle is a smear, the legs shown as three dry-brush multiples and the body stretched 20%. Holds are real holds: a drawing kept still for 6–12 frames.
- The ball flies true parabolas (g = 2,400 px/s²), squashes to scaleY 0.7 for two frames on each bounce and keeps 55% of its height after each one.
- The skid: four drawings, front legs braced, body tilted back 15°, three flat cream dust puffs that pop out and shrink and two grass clods that flick up; it travels 140px and stops dead.
- Easing: camera pans on cubic-bezier(0.45, 0, 0.2, 1); takes are snappy, a 2-frame anticipation and then the new pose, held.
- Type: the end card is a mustard rectangle (980×300, x 820–1800, y 130–430) with its fill off-register like everything else; the credit in "League Spartan" 700, 24px, uppercase, tracked 0.3em, along its top; the title in "Caveat Brush" 400, 120px, ink, beneath.
- Premium: strong graphic design, off-register color, held poses and snappy timing on twos, and a background that looks painted by a layout artist. Cheap: smooth tweened puppets, gradients, a clip-art dog sliding across a stock park.
Banned: gradients, soft shadows, realistic dog anatomy, smooth puppet tweening of the dog, fills that match their outlines exactly, blur, strobing speed lines, any of the owner above the legs, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: the owner's legs stand at left with Pepper sitting beside them, tail wagging on three drawings; the hand reaches down, winds back (a 2-frame anticipation) and throws at 0.8 s.
- 1.0–1.6s: the ball sails right across the sky; Pepper does a double take (head snaps to follow, ears flip up) and gathers into a crouch.
- 1.6–3.6s: the chase: Pepper runs right and the camera pans about 1,800px with it; trees, the bench and the lamp slide past; the ball bounces twice ahead.
- 3.6–4.6s: the overshoot: a bad bounce sends the ball back left; Pepper skids 140px past it in dust and clods, stops dead, holds 8 frames, then scrambles around.
- 4.6–5.4s: Pepper leaps and snaps the ball out of the air off its third bounce, landing in a four-drawing settle.
- 5.4–7.4s: the proud trot back: head high, ball in mouth, chest out, a prancing trot on twos as the camera pans back left. At 6.0 s Pepper is mid-trot in profile on open grass with trees behind: a clean, complete frame.
- 7.4–8.4s: Pepper drops the ball at the owner's shoes, sits, looks up and thumps its tail; the hand pats its head once.
- 8.0–8.8s: the end card wipes in from the left over the sky: the credit, then the title.
- 8.8–10.0s: hold, still.
For other lengths, stretch the chase and the trot and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: inline SVG, setting path data, transforms and opacity from seek. No other libraries (no three.js: this style is flat).
- Build the background pan once at load as grouped shapes under a static feTurbulence dry-brush mask, and build Pepper as a library of drawn pose groups, showing one per frame from the on-twos index. The ball, the pan and every parabola are closed-form functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check Pepper's drawing changes only every second frame while the pan stays smooth, fills sit off their outlines everywhere, the ball follows true parabolas and bounces lower each time, the skid stops dead, the 6.0 s frame is a clean trot pose, nothing of the owner shows above the legs, and the end card reads clearly over the sky. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
