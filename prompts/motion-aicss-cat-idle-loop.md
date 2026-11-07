# Cat Idle

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/cat-idle-loop) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/cat-idle-loop)

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
Make a 10-second character idle animation: a cartoon cat waits on a cushion, blinking, flicking an ear, swishing its tail, yawning and stretching, then settles into a loaf.

<inputs>
If I don't give you something, use the default and don't ask.
- Character: Biscuit, a ginger tabby cat.
- Title: "Biscuit"
- Line: "Idle test · take 3"
- Action labels, in order: blink, ear flick, tail swish, yawn, stretch, loaf.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a studio animator's character test: flat fills, a confident ink line and timing that carries all the personality, set in a sunlit corner of a warm room.
- Palette: wall oat #F2E4CF; a window-shaped sunbeam on the wall #FFF3DD (two panes and a mullion, 40px soft edge) at x 1180–1660, y 170–690; skirting line at y 820 and floor #E6D2B5 below it; cushion dusty teal #6FA3A0 with piping #4F807D and a shade side #5C8F8C; cat ginger #E8944A, stripes #C46B2A, cream muzzle, chest and paws #FBE6C8, inner ears #F2A49C, nose #DE766E, eyes #2A1F1A with two white catchlights, mouth interior #B9484A, tongue #EF8A86; ink #3A2921; secondary text #8A7462.
- Line and fill: every cat shape is a flat fill outlined in ink at 4px with round joins and caps; whiskers and toe lines at 2.5px. Stripes are clipped to the shape they sit on. The only soft things are two contact shadows (#3A2921 at 12%): a wide one under the cushion and a tight one where the cat meets it.
- The rig: SVG groups with explicit pivots. The cat is seen in three-quarter view, body side-on facing left, head turned toward the camera; sitting, it stands about 520px tall, centered at x 780 on the cushion (an ellipse 640×150 whose top is at y 760).
  - Head 230×200 with three scalloped cheek tufts a side, pivoting at the neck. Ears with rounded tips, each pivoting at its base. Almond eyes 46px tall, each with an upper-lid shape that slides down over it. A heart nose and a W mouth that opens into an oval showing the tongue and two small fangs. Three whiskers a side, each its own path.
  - Body: one closed path whose points interpolate between three keyed shapes with the same point count: sit (a pear), stretch (a long low arch, chest down and rear up, about 760px long) and loaf (a rounded rectangle about 380×210).
  - Front legs as tapered capsules with oval paws and two toe lines each; a hind haunch oval; three forehead stripes, four back stripes and rings on the tail.
  - Tail: a 16-segment chain from the rump, 300px long, tapering from 34px to 16px, drawn as one smooth outline around the chain.
- Motion is classic character animation: every action has anticipation, overlap and a settle.
  - Breathing: body scaleY 1 ± 1.2% on a 3.0 s sine, pivot at the base; the head follows 0.15 s later by 2px.
  - Blinks: lids close in 0.1 s, hold 0.04 s and open in 0.14 s; the eyes squash 10% at the bottom of the blink.
  - Ear flicks: rotate −24° in 0.08 s, then return on a damped spring, 1 − e^(−9s)·cos(22s) with s the seconds since the flick, settled by 0.4 s.
  - Tail: segment i's angle = its pose angle + A(t)·sin(ω·t − 0.42·i), with amplitude growing from 0.6× to 1.6× toward the tip, so each swish travels base to tip and the tip curls last.
  - Whiskers and ear tips lag the head by 0.06 s. Paws stay planted except while stepping into the stretch.
  - Pose changes ease on cubic-bezier(0.45, 0, 0.2, 1) over 0.3–0.8 s; arriving in a pose overshoots 3% and settles in 0.25 s.
- Dope sheet: a 1px #8A7462 line from x 120 to 1800 at y 968 that maps 0–10 s, with a small tick at each action's start time and its label in "Kalam" 400, 26px, alternating above the line (baseline y 952) and below it (baseline y 1004) so neighbors never collide. A playhead dot runs along the line. Labels wait at 40% ink and turn full ink when their action starts. A frame counter, "f 000 / 300", in "Courier Prime" 400, 22px, right-aligned at (1800, 100), counts frames at 30 fps.
- Type: title in "Kalam" 700, 72px, #3A2921, top-left at (120, 100); the line in Kalam 400, 28px, #8A7462, beneath. Text rises 10px as it fades in over 0.5 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: weight, timing and small overlapping details (whiskers lagging, the tail tip curling last, a 3% settle) that make a simple design feel alive. Cheap: a sticker bobbing on a sine, a tail wagging like a metronome, eyes that blink by vanishing.
Banned: gradients on the cat, line boil or jittering outlines, motion lines, hearts, sparkles or "zzz" marks, the cat sliding on the cushion, a mechanically looping wag, two blinks closer than 0.3 s, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: Biscuit sits breathing, the tail curled around the front paws, its tip lifting slowly; the title, line and dope sheet rise in.
- 0.8–1.4s: a blink at 1.0 s.
- 1.4–2.2s: the left ear flicks at 1.5 s; both ears then swivel 15° to the right and the head turns 8° after them, as if toward a sound.
- 2.2–3.4s: the tail lifts off the paws and swishes three times, each wave running base to tip, then lies back down.
- 3.4–5.0s: the yawn: the head dips 6px and the eyes squint (0.25 s of anticipation), then the head tilts back 12° as the mouth opens wide over 0.4 s, eyes shut and ears pressed back; hold 0.4 s; the mouth closes and the tongue flicks once over the nose.
- 5.0–7.0s: the stretch: the front paws step forward twice (5.0–5.6 s), the chest lowers and the rear lifts into a long arch with the tail straight up, held from 5.7 to 6.6 s, so the 6.0 s frame is a clean, complete stretch silhouette; then it rises back to sitting.
- 7.0–8.4s: the settle: the body turns 10° toward the camera, the front paws tuck under the chest, the body sinks into the loaf with a 3% overshoot and the tail wraps along its side.
- 8.4–8.8s: a slow blink to half-closed, contented eyes; breathing eases to stillness.
- 8.8–10.0s: hold, perfectly still: the loaf on the cushion in the sunbeam, all six labels in full ink.
For other lengths, stretch the gaps between actions, keep each action's own timing and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: inline SVG, setting path data, transforms and opacity from seek. No other libraries (no three.js: this style is flat).
- The body's three keyed shapes share one point count so they blend cleanly; the tail outline is rebuilt each seek from its chain angles, and every angle, blend weight and spring is a closed-form function of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the tail wave travels base to tip, the paws never slide on the cushion, outlines stay closed through every body blend, the 6.0 s frame is a clean stretch, the dope-sheet labels never overlap, and the eyes and catchlights read clearly at 1280×720. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
