# CRT Channel Surf


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/crt-channel-surf) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/crt-channel-surf) · [对应动效输出](https://www.aicssanimations.com/previews/crt-channel-surf.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** interactive
- **作品发布时间：** 2026-10-18
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
Make a 10-second channel surf on a 1970s CRT television: the set warms up in a sunlit den and its dial clicks through a test card, snow, a weather report and a cartoon before landing on a show's title card.

<inputs>
If I don't give you something, use the default and don't ask.
- Set: a 1970s walnut tabletop television with a chrome badge reading "Belvane" (fictional).
- Station on the last channel: QV9, Quarry Valley (fictional).
- Show title: "Rabbit Ears". Line: "Stories from the antenna years · Sundays at 8".
- Channels, in order: 2 a test card · 3 snow · 4 "Quarry Valley Weather" (tonight: Millbrook 46°, Ashby 44°, Pine Gap 39°, Lowfield 47°; "Showers clearing late") · 6 the cartoon "Puddlejump", a round blue bird hopping over striped hills · 9 the title card.
- Length: 10 seconds.
</inputs>

<direction>
- Room: a daytime 1970s den seen straight on. The wall is wallpaper of interlocking rounded squares in #C9803E, #8E4F24 and #E7C38A, blurred 6px as if out of focus, lit by a window off-frame left: 12% brighter at the left, falling off to the right. The set stands on a teak sideboard (#7A4A26, a 30px front edge with a highlight along its top) whose top runs at y 950, with a soft contact shadow under the cabinet.
- The set: a walnut-veneer cabinet at x 250–1670, y 120–950, corners rounded 36px. Generate its grain once at load (long wavy streaks of #5A3418 over #7B4A26 with a few cathedral arches) under a satin finish: a soft highlight band along the top and a 2px lighter bevel on the front edges. The tube sits at left in a dark bezel (#1A1714, 24px wide, with a thin chrome trim line); the picture opening is x 330–1250, y 180–870, a 4:3 rectangle with corners rounded 70px. The control panel at right (x 1310–1610) is brushed aluminium: a VHF channel dial 190px across at (1460, 340) with a ribbed edge, a pointer and the channels 2–13 printed around it every 30°; a smaller fine-tuning knob and a volume knob below it; woven speaker cloth (#3A2E24 with a 3px cross weave) from y 640 to 900, with "Belvane" in chrome script ("Damion" 400, 56px) across it. Rabbit-ear antennas rise from a small dome on the cabinet top: two 3px chrome rods with ball tips at 30° and 58° from vertical, cropped by the top edge.
- The tube: draw each channel into a 640×480 offscreen canvas (sizes below are in that buffer; one buffer pixel is about 1.44 stage pixels) and map it onto the opening through a WebGL fragment shader: barrel distortion (k 0.10) so the picture bulges toward the center of the glass, corners darkened 30%, scanlines as a soft 9% sinusoidal darkening at 160 lines over the picture height (about 4.3 stage pixels each, coarse enough not to moiré at 1280×720), a 4px phosphor bloom on bright areas, and 1px red and blue convergence fringes only at the outer edges. Over the picture, the glass: a fixed reflection of the den's window (a soft rounded rectangle with two mullions, white at 7%, bent to the glass curve) at upper left, a curved specular streak along the top, and an inner shadow where the glass meets the bezel. With the set off, the tube is a dark green-grey #2E3430 carrying only those reflections.
- The channels, drawn in code:
  - 2, test card: a grey #6B6B6B field with a white grid, black-and-white castellations around the border, a central circle holding seven 75% color bars (white, yellow, cyan, green, magenta, red, blue) over a six-step grey scale, a center cross, and "QV9" in white in a black box. Original, not a copy of any real card.
  - 3, snow: 12 noise frames at 320×240, generated once at load and shown at 12 per second, mean brightness 45% and held within ±3% from frame to frame, with a faint ghost of the weather picture (12%) drifting sideways and two soft dark hum bars rolling slowly down.
  - 4, weather: a #1E4C8F header bar reading QUARRY VALLEY WEATHER in "Archivo Narrow" 700, 34px, white; a flat map of a fictional valley (land #5E9A4C, hills #8DB36A, a winding river and a lake in #3B78B5); four town dots with their names and temperatures in "Archivo Narrow" 700, 40px, white with a 3px black outline; a flat sun, a cloud and a rain cloud; a lower band reading "TONIGHT · Showers clearing late".
  - 6, cartoon: flat cel colors animated on twos (12 drawings a second): sky #8FD3F4, hills in alternating stripes of #7CC24A and #A6DB6B, one slow cloud, and the bird, a round #3B6FD1 body with a cream belly, an orange beak and big eyes, hopping in squash-and-stretch arcs; "Puddlejump" in "Chewy" 400, 44px, on a yellow banner at the top.
  - 9, title card: five thick bands in #8B3A1E, #E8572A, #F29A2E, #F6C543 and cream #F4E6C8 curving in from the left like a 70s station ident, a small drawing of a rabbit-ear antenna, "Rabbit Ears" in "Righteous" 400, 76px, #3A1A0C, and the line in "Archivo Narrow" 600, 22px, beneath.
- Tuning: each channel step turns the dial one 30° detent in 0.12s with a 3° overshoot and settle, with 0.08s between steps on multi-channel jumps. While the dial moves the tube shows snow; when it stops, the new picture locks in one of two ways: a vertical roll (the picture slides up through a 40px black blanking bar and slows to rest over 0.45s, easing out) or a horizontal tear (rows shear sideways by up to 60px on a decaying sine that settles over 0.3s).
- Power on: from the dark tube, a bright horizontal line across the middle opens vertically into the full picture over 0.35s while brightness ramps from 40% to 100% over 0.6s. Never a white flash.
- Safety: picture changes are cuts no closer than 0.4s apart; the snow's mean brightness stays close to the pictures' so cuts don't flash; no change of mean screen brightness over 20% happens more than 3 times in any second.
- Camera: a slow push from 1.00 to 1.05 toward the tube across the whole piece, on easeInOutSine.
- Premium: a real object in a real room, with wood grain, glass that holds the window's reflection, a dial that clicks, and pictures that roll and tear before they lock. Cheap: a flat rectangle with a scanline overlay and an RGB-split glitch.
- Banned: RGB-split glitch effects, VHS tracking lines, on-screen channel numbers, remote controls, flat-screen sets, real station logos or copied test cards, a white power-on flash, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.5s: the den; the set is off, the tube dark with its window reflection, the dial at 2.
- 0.5–1.1s: power on: the line opens into the test card and the brightness settles.
- 1.1–2.2s: the test card holds; the camera push is under way.
- 2.2–3.0s: the dial clicks to 3: snow, with the ghost drifting and the hum bars rolling.
- 3.0–3.7s: a click to 4; the weather locks with a vertical roll.
- 3.7–4.8s: the weather holds; the four temperatures pop in 0.12s apart (scale 1.2 → 1) and the TONIGHT band slides in.
- 4.8–5.4s: two clicks (5, then 6) through snow; the cartoon locks with a horizontal tear.
- 5.4–7.0s: Puddlejump hops three times across the hills.
- 7.0–8.0s: three clicks (7, 8, 9) through snow; the title card locks with a vertical roll.
- 8.0–8.8s: the bands sweep in, "Rabbit Ears" bounces in letter by letter (60ms apart, 8% overshoot) and the line fades up.
- 8.8–10.0s: hold on the title card glowing in the den.
For other lengths, stretch the channel holds; keep every lock transition whole and at least 1s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas. A 2D canvas for the den, the cabinet and the controls; one WebGL canvas over the picture opening (preserveDrawingBuffer: true, drawn once per seek) that warps the 640×480 channel canvas, uploaded as a texture each seek; a 2D canvas above it for the glass reflections and the bezel. Generate the wallpaper, the wood grain and the 12 snow frames once at load.
- The dial angle, the roll and tear offsets and every channel's animation are closed-form functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the set reads as a wooden 1970s television in a lit room from the first frame, the picture bulges with the glass on every channel, the dial moves before every change, no two cuts fall within 0.4s, the snow never reads as a flash, and the 6s frame shows the cartoon fully locked. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
