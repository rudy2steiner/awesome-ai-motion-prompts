# Arcade High Score


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/arcade-high-score) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/arcade-high-score) · [对应动效输出](https://www.aicssanimations.com/previews/arcade-high-score.mp4)

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
Make a 10-second arcade high-score sequence: a cabinet tallies a player's score, the player enters three initials with the joystick, takes third place on the table, and the machine falls into attract mode.

<inputs>
If I don't give you something, use the default and don't ask.
- Game: COMET ALLEY (fictional), on the marquee.
- Player: score 103780, initials VAL.
- Table before: 1 ZED 128450 · 2 MKO 117900 · 3 ACE 98650 · 4 JUN 87200 · 5 RAY 76400 · 6 PIX 65150 · 7 BOB 54300 · 8 LIL 43900 · 9 TAM 32750 · 10 KIT 21600. VAL goes in third, everyone below moves down one, and KIT drops off.
- Attract text: INSERT COIN and 1 OR 2 PLAYERS.
- Length: 10 seconds.
</inputs>

<direction>
- The cabinet, seen straight on from a player's eye height, in a dark arcade #0B0716 with a few soft out-of-focus glows of other machines (magenta and teal, 20%) behind it: an upright cabinet in deep violet #2A1240, its side panels showing as narrow trapezoids at x 230–420 and 1500–1690, printed with orange-to-magenta comet streaks (#FF8A2B → #FF3D8B) and edged with #9C4DFF T-molding that catches a highlight.
- Marquee (x 420–1500, y 70–200): a backlit translucent panel lit evenly from behind, falling off slightly at its ends; COMET ALLEY in "Bungee" 400, 96px, cream #FFF3D6 with a 6px violet outline, over printed comets on deep blue; a row of 24 small bulbs along its lower edge.
- Bezel (x 420–1500, y 215–905): glossy black with thin orange pinstripes and small comet art in its corners, with a soft reflection of the marquee along its top.
- Monitor (x 520–1400, y 240–900, 880×660): the screen is drawn into a 220×165 buffer and scaled ×4 with nearest neighbour, under slightly convex glass: 10% darker toward the corners, a faint band reflecting the marquee and a 2px phosphor glow. No distortion, no scanlines.
- Control panel (y 915–1080, cropped by the bottom edge): violet with the same art, a red ball-top joystick at x 760 on a black shaft with a dust washer, two round buttons with light rings (FIRE in cyan #35D6F4 at x 1060, JUMP in magenta #FF4FD8 at x 1170) and a small 1P START button. The stick tils 18° toward wherever it is pushed; buttons dip 4px when pressed.
- Screen font: "Press Start 2P" at 8px in the 220×165 buffer, alpha thresholded at 50% so every pixel is on or off; headings at 16px.
- Screen palette: black, white #FFFFFF, red #FF3B30, orange #FF9F1C, yellow #FFE14D, green #3BE27A, cyan #35D6F4, blue #4A6CFF, magenta #FF4FD8.
- Entry screen: GAME OVER in red at 16px; CONGRATULATIONS! in yellow; YOUR SCORE with its digits counting up; RANK 3RD; ENTER YOUR INITIALS; three letter slots with underlines; STICK + FIRE in cyan.
- Letter entry, the way these machines did it: the active slot shows a letter, and holding the stick steps through the alphabet at 8 letters a second, wrapping around. For V the stick pulls down and the letter steps back A, Z, Y, X, W, V; for A, FIRE goes straight away; for L the stick pushes up from B to L. Each FIRE press locks the letter, which turns yellow, and moves the underline on.
- Table screen, in buffer pixels: HIGH SCORES at 16px from y 6; the headings RANK SCORE NAME at y 28; ten rows at 11px pitch from y 40, such as "3RD 103780 VAL", rank colors running red to magenta down the rows; the attract line at y 154.
- Insertion: the table draws in its old order with a gap at third place; rows 3–9 slide down one row (11px) in whole-pixel steps over over 0.4s while KIT slides off below; then VAL's row types in, a character every 40ms.
- Attract mode: the table's colors roll down the rows one step every 0.5s; the marquee bulbs chase, every third bulb lit and the pattern moving one bulb every 0.25s (so each bulb blinks about once a second); the panel buttons breathe between 60% and 100% over 1s; the attract line alternates between INSERT COIN and 1 OR 2 PLAYERS once a second; a small 16×8 comet sprite with a three-frame tail glides across behind the HIGH SCORES heading every 2.5s.
- Motion on the screen is digital, in whole pixels and instant changes; the only smooth motion is the physical controls and a slow camera push from 1.00 to 1.04 toward the monitor across the piece, on easeInOutSine.
- Premium: an exact low-resolution screen of on-or-off pixels, a cabinet whose marquee is really lit, controls that move with the entry, and a table whose numbers stay in order. Cheap: neon text on black with a glow filter and smooth fades.
- Banned: real game, company or character names or look-alike sprites, smooth fades or tweens on the screen, anti-aliased screen text, a glow filter over everything, scores out of order, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.5s: the cabinet glows in the dark hall; GAME OVER on the screen.
- 0.5–1.4s: CONGRATULATIONS!; YOUR SCORE counts 000000 → 103780; RANK 3RD.
- 1.4–1.6s: ENTER YOUR INITIALS; slot 1 shows A.
- 1.6–2.4s: the stick pulls down: A, Z, Y, X, W, V; FIRE locks V at 2.4s.
- 2.4–2.8s: FIRE locks A at 2.7s.
- 2.8–4.5s: the stick pushes up through B to L; FIRE locks L at 4.4s.
- 4.5–4.9s: VAL holds in yellow; the screen wipes to the table, top to bottom.
- 4.9–5.4s: the table draws row by row, 40ms apart, with a gap at third place.
- 5.4–5.8s: the rows slide down, KIT drops off and VAL types in.
- 5.8–8.6s: attract mode.
- 8.6–10.0s: hold: the colors stop rolling, every bulb lit, INSERT COIN steady, the comet gone.
For other lengths, stretch attract mode; keep the entry timing and at least 1s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, the backing store sized from CSS size × devicePixelRatio. Draw the parts of the cabinet that never change (side art, bezel art, marquee print, hall) once at load into offscreen canvases; each seek rebuilds the 220×165 screen buffer from t and composites everything with the lights at their current levels.
- The letter steps, table positions, bulb pattern and button states are functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every screen pixel sits on the 220×165 grid with no smoothing, the letters step the right way for each stick move, FIRE dips on each lock, the final table is in descending order with VAL third and KIT gone, no bulb or text blinks more than twice a second, and the cabinet reads as a lit physical machine. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
