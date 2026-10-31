# Rubber Hose Cartoon


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/rubber-hose-cartoon) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/rubber-hose-cartoon) · [对应动效输出](https://www.aicssanimations.com/previews/rubber-hose-cartoon.mp4)

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
Make a 10-second 1930s rubber-hose cartoon: an original teakettle character dances a Charleston to the beat on a vaudeville stage, then the picture irises out.

<inputs>
- Character: Tippy, a dancing teakettle (design below).
- Cartoon title: "Tea Time Trot".
- Studio line: "A Dimwhistle Cartoon".
- End card: "The End".
- Tempo: 120 BPM.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Look: a black-and-white cartoon print from around 1930. Palette, nothing else: black #141312, paper white #ECE8DF, greys #4A4744, #8C8883 and #BDB8AF.

Type: Limelight for everything (title 120px, studio line 40px, "The End" 110px), tracking 0.04em.

Tippy, original and built from simple shapes: a squat round kettle body 300px wide in #BDB8AF with a 6px black outline; a lid that is a black bowler-hat dome with a round knob; a short black spout pointing right; a black handle looping over the back. On the front, two tall white oval eyes (36×58px) touching each other, each with a tall black pupil missing a 60° pie-cut wedge, and a wide smile with a dark grey mouth and a small tongue. Limbs are rubber hoses: single 12px black strokes, cubic Béziers from shoulder or hip to wrist or ankle, no elbows or knees, free to stretch ±20%. White four-finger gloves with black outlines, puffy cuffs and three stitch lines; big black oval shoes with a white highlight. Squash and stretch keeps volume: body scaleY s and scaleX 1/s, with s between 0.86 and 1.12.

Stage: grey curtains (vertical folds in alternating #4A4744 and #8C8883 bands under a scalloped, black-edged valance), a plank floor in one-point perspective (#8C8883 with black plank lines converging on center), and a spotlight pool on the floor (a #ECE8DF ellipse at 30%) that follows Tippy. A potted daisy stands stage left and a sugar bowl stage right, and both squash on every beat too, because in this era the whole world dances.

Beat: 120 BPM, beat n at n × 0.5s. A contact squash (s 0.88) lands on each beat and a stretch (s 1.08) on each off-beat. Animate on twos: drive all character and prop motion from tq = floor(t·12)/12, six drawings per beat, with sine easing inside each beat. Film at 24fps (film frame f = floor(t·24)): grain from eight precomputed noise tiles cycled by f at 9% opacity; gate weave of ±1.5px x and ±1px y per film frame from a seeded PRNG; 0–2 dust specks per film frame (2–6px, black or white) and a thin vertical scratch that lasts 4 frames, twice; a soft vignette (35% at the corners); exposure breathing of ±2% on a slow 0.5Hz sine, never jumping frame to frame.

Iris-out: a black field with a circular hole, closing on Tippy's eyes with cubic-bezier(0.55, 0, 0.45, 1).

Premium: everything on twos and on the beat, curves for limbs, pie-cut eyes, true black-and-white values, honest film wear. Cheap: smooth 60fps tweens, a sepia filter over a modern vector character, limbs that bend at joints. Banned: any color or sepia tint, elbows or knees, five-finger hands, character outlines thinner than 5px, smooth unstepped character motion, mouse ears or any resemblance to an existing cartoon character, modern fonts, heavy flicker, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: title card: paper white with a grey radial vignette, an ornate double-rule frame with corner flourishes, "A Dimwhistle Cartoon" above "Tea Time Trot". Hard cut on the beat at 1.0s.
- 1.0–3.0s: the stage; Tippy bounces in from the right in three hops that land on beats, arriving center stage with the shoes at y 880.
- 3.0–5.0s: Charleston: heels swivel out and in on each beat, the leg hoses bow inward and cross at mid-length on beats 2 and 4, arms swing in big opposed loops, the head tilts ±8°.
- 5.0–7.0s: hat pop: the lid flies up 160px on beat 1, spins one turn and lands back on beat 3; steam puffs from the spout on beats 2 and 4 (white circles that grow and fade over 0.4s).
- 7.0–8.0s: big finish: jazz hands up, legs apart, a held pose that vibrates slightly on each beat.
- 8.0–8.8s: the iris closes to a 170px-radius circle around Tippy's eyes; Tippy winks at 8.6s.
- 8.8–10.0s: hold: the winking Tippy inside the iris and "The End" in white below it on the black, baseline 120px above the bottom edge. Grain, weave and dust carry on.
Other lengths: add or remove whole bars of four beats, keep 120 BPM and twos, and end on at least 1s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative (growth, simulation, particles) is precomputed once at load at a fixed step or solved analytically, so seek can jump to any time. Past the end, hold the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Engine: inline SVG for the stage and character, with path data rebuilt from the pose in every seek and the gate weave as a transform on the stage group; a canvas overlay for grain, dust, scratches and vignette.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that every limb is a smooth curve with no kinks (the Charleston leg cross is deliberate), gloves and shoes stay attached, each squash lands on a beat, the stepping on twos is visible, the film wear is present but never busy, and "The End" is legible. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
