# Monster in a Box


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/monster-in-a-box) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/monster-in-a-box)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** characters-stories
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
Make a 10-second character reveal: a cardboard box rattles, its flaps pop open, and a fuzzy friendly monster peeks out, blinks and waves.

<inputs>
If I don't give you something, use the default and don't ask.
- Monster: Fennick, turquoise and fuzzy, with two small cream horns and one tooth.
- Box: a stamp reading "HANDLE WITH CARE" and a shipping label reading "To: Room 4".
- Title: "Fennick has arrived", set on two lines: "Fennick" / "has arrived".
- Line: "Some deliveries are friendlier than others."
- Length: 10 seconds.
</inputs>

<direction>
- Look: a warm picture-book room with one hero texture, fur: flat, softly shaded shapes for the room and the box, and a monster built from thousands of drawn strands so it looks touchable.
- Palette: wall mustard #E6AE3A with faint vertical stripes #DDA332; wainscot cream #F4E4C4 with a rail shadow #D9C39C; floorboards walnut #7A4C2C with seams #5E381E; box kraft #C99B62, flap tops #D8AE77, side face #A87A45, inside #2B1A10, flutes #B4844E; tape #E6D7B4 at 80%; stamp red #B5372E; label white #F7F3EA; fur base #158A86, mid #2FC1BA, tips #A6F0E4; horns #F4E7CC with ring lines #D6C29E; eye whites #FFFFFF, irises #3A2A62, pupils #120E1F; mouth #5A1E3A; tooth #FFFFFF; text #3A2416.
- Room: the wall runs down to y 760 with a wainscot rail at y 640; floorboards below 760; a small framed crayon drawing of a house at upper right (x 1530-1750, y 160-360). Warm light from the upper left: the box casts a soft shadow to the right (30px blur, 25%) and sits on a tight contact shadow.
- Box: front face x 820-1380, y 520-900, seen nearly head-on from a little above, so the top opening shows as a 110px-deep trapezoid behind the front rim and a narrow side face (70px) shows at the right. Real corrugated cardboard: wavy flutes along every cut edge, a dented lower-left corner, tape across the closed flaps, the red stamp (with two small up arrows) at y 700-800 and the label at lower right, both below where the opened front flap will hang. Four top flaps hinge on the rim: the front and back flaps swing as foreshortened quads (the front one ends hanging down over the top of the front face), and the side flaps swing out left and right.
- Fennick: a soft pear-shaped body 420px wide, centered at x 1100, whose head and chest rise about 330px above the front rim when fully up (horn tips near y 150); two horns, two big eyes (90px, set close), a wide mouth with one tooth, and short arms ending in three-fingered mitten hands. Build the fur once at load: 7,000 tapered strands (10-28px long, 3px at the root) rooted across the body and along its silhouette, pointing outward along the surface normal with seeded jitter and a gentle swirl; dark base strands first, lighter tips over them, longest at the edges so the outline is fuzzy, shortest around the eyes and mouth. Each frame, every strand's tip bends against the motion: offset = -k*velocity, with velocity taken analytically from the body's motion curve, plus a damped 4px spring after each pop. Eyes, horns, mouth and hands are drawn over the fur with clean edges. The body is clipped behind the box's front face; hands on the rim are drawn in front of it.
- Eyes: lids close top-down for blinks (0.08 s to close, 0.12 s to open); pupils dart in 0.06 s and hold; one fixed catchlight at the upper left of each eye.
- Comic timing: the rattles escalate with real pauses between them. Each is a hop of 6-14px with a +/-3 deg twist, landing with a 4% squash, the flaps lifting a crack to show darkness inside. Pops use anticipation: squash 10% for 0.15 s, stretch 18%, then settle on 1 - e^(-8s)*cos(16s), with s the seconds since the pop. Looks and waves use cubic-bezier(0.45, 0, 0.2, 1) over 0.3-0.5 s.
- Type: title in "Chewy" 400, 96px, #3A2416, two lines at x 120 with baselines at y 430 and 525; the line in "Nunito" 700, 30px, #3A2416 at 75%, at most 560px wide, from baseline y 590. The stamp in Nunito 900, 30px, uppercase, rotated -6 deg; the label in "Gochi Hand" 400, 30px.
- Premium: fur that bends with every move, cardboard that looks like cardboard (flutes, tape, a dent), and comic timing with pauses. Cheap: a fuzzy outline filter on a flat blob, a box that shakes nonstop, a reveal with no anticipation. Banned: scary teeth or claws, horror lighting, slime, glowing eyes, fur that re-randomizes between frames, nonstop shaking, more than one tooth, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0-0.6s: the quiet room; the taped box sits still.
- 0.6-2.4s: the rattles: a small hop at 0.7 s; stillness; two quick hops at 1.4 and 1.6 s; stillness; a big hop at 2.2 s that splits the tape and lifts the flaps a crack.
- 2.4-3.2s: in the dark crack, two eyes appear, look left, look right and blink once.
- 3.2-4.0s: the flaps pop open on springs, 60 ms apart (the front folds down over the face of the box, the back swings up, the sides out), and Fennick pops up to chest height with the squash, stretch and settle; the fur ripples outward and settles.
- 4.0-5.2s: the mitten hands grip the front rim; Fennick looks around the room (eyes dart left, then right), then at the camera, and blinks.
- 5.2-6.6s: a wide smile; the right arm rises and waves three times (+/-20 deg, 0.4 s each), the arm fur trailing. At 6.0 s the wave is at its widest with Fennick facing the camera: a complete, cheerful frame.
- 6.6-8.0s: the title and line rise 12px into place over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1); Fennick tilts its head 10 deg and holds the right hand up, open.
- 8.0-8.6s: the fur springs settle to rest.
- 8.6-10.0s: hold, still.
For other lengths, stretch the pauses between rattles and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920x1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size * devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. No other libraries.
- Generate the room, the box faces and the fur strand table (root, direction, length, width and color for each strand) once at load from the seeded PRNG; each frame draws the room and box, then the fur and features from the analytic body motion at t, clipped behind the box's front face. Batch strands by color so 7,000 strokes a frame stay fast.
</build>

<check>
Before showing me, step through one frame per second (t = 0...10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the fur never re-randomizes between frames and bends against the motion, Fennick always sits behind the box's front face with only the hands over the rim, the flaps stay hinged to the rim, the rattles have stillness between them, the eyes read clearly at 1280x720, and the title sits clear of the box and the monster. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
