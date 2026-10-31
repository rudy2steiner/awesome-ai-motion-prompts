# World Map Level Select


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/world-map-level-select) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/world-map-level-select) · [对应动效输出](https://www.aicssanimations.com/previews/world-map-level-select.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** interactive
- **作品发布时间：** 2026-10-19
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
Make a 10-second game overworld level select: on an illustrated island map, path dots draw between level nodes, a character token hops to the last level of World 1, a new path crosses the sea, World 2's first node unlocks with a flourish, and the token hops over to it.

<inputs>
If I don't give you something, use the default and don't ask.
- Game: Moss & the Tidelands (fictional). Token: Moss, a round teal sprout creature (original).
- World 1: "TANGLE SHORE", levels 1-1 to 1-5, with stars earned 3, 2, 3, 1 and, after the clear, 3 for the fortress 1-5.
- World 2: "LUMEN PEAKS", first level 2-1 "Frostlight Steps".
- Chips: "WORLD 1 CLEAR!" and "NEW PATH!"
- Level card: "2-1 · Frostlight Steps" · "★ 0/3 · Best time --:--" · "PLAY"
- Length: 10 seconds.
</inputs>

<direction>
- Look: a bright storybook overworld, drawn as flat vector illustration with soft shading: chunky islands with visible cliff sides, lollipop trees, a windmill and cottages, waves drawn as little curved strokes, puffy clouds casting shadows on the sea, bold red path dots and round level nodes, a cute token with squash and stretch. Everything is readable from across a room and alive in small ways.
- Palette: sea periwinkle #9AA8F0 with wave strokes #B9C3F7 and deeper water #7584DB near cliffs; foam #FFFFFF; sand butter #F7DE8A; grass moss #8CC66A with sunlit tops #B5E08A; cliff sides rust #C9653F with darker bands #9A4630; trees #4E9E4A and #6DB85A with trunks #8A5A3A; cottage walls #FFF3E0 with roofs #E8434B and #F29A3D; World 2 snow #F6F3FF with lilac shadows #B7A9E8, pines teal #2F8C7E, a frozen lake #CFE6FA; path dots candy red #E8434B with a 2px cream #FFF6E3 rim; completed node tops butter #FFD45C, locked node tops lilac grey #B9B3D6, stars gold #FFC83D with an ink edge; Moss teal #2FA59B with a belly #8FDCCF and a leaf #7CC35A; outlines and type ink #2A2340; banners butter with ink type. Red dots and butter nodes against periwinkle and moss are the readable layer; everything else stays softer.
- The map, in map units (a 3600 × 1400 world, drawn once as SVG at load):
  - World 1, x 200–1500: a large island with a beach rim, a meadow, a cluster of 30 lollipop trees, a windmill whose sails turn slowly, three cottages, a river ending in a little waterfall off the cliff edge; nodes 1-1 at (360, 860), 1-2 at (600, 700), 1-3 at (860, 820), 1-4 at (1080, 640), and the fortress 1-5 on a rocky headland at (1380, 760): a tiny two-tower fort with crenellations, a door and a flag;
  - between them, x 1500–2150: four small islets with a palm or a rock each, the last two joined by a wooden plank bridge on rope rails;
  - World 2, x 2150–3400: an island of snowy peaks in lilac shadow, pines, a frozen lake and a softly glowing crystal outcrop; node 2-1 at (2380, 780);
  - every island is two shapes: a top (grass or snow, with a soft lighter radial highlight toward its upper left) and a cliff band 26 units below it in rust (or lilac grey for World 2) with darker strata, ringed at the waterline by a dashed white foam line;
  - sea texture: 400 seeded wave strokes (short arcs) that bob ±3px on their own sines and drift left at 6 units/s; cloud shapes (overlapping circles) with their shadows as darker periwinkle blobs offset 60 units down-right on the sea; a cloud bank hides World 2 at the start.
- Paths: SVG paths between consecutive nodes, curving through the scenery; dots placed every 34 units along each path (sampled once at load with getPointAtLength). A path draws by popping its dots in order, 40 ms apart, each from scale 0 to 1.3 to 1.0 over 0.15 s.
- Nodes: an ellipse top 74 × 44 on a 12-unit-thick side band, a soft shadow below; completed nodes are butter with a small red pennant on a pole and their stars in an arc above (earned stars gold, missing ones as ink outlines); the label ("1-1") beneath in Baloo 2 800, 24px, ink with a 4px cream stroke; locked nodes are lilac grey with a padlock (a rounded body with a keyhole and a shackle).
- The unlock flourish for 2-1: the padlock jiggles twice (±10°), its shackle pops open, the lock drops with a half spin and fades; the node's top turns from lilac grey to butter in a radial wipe from its center; a ring of eight five-point star shapes bursts outward 80 units and fades; the label pops; a pennant springs up on its pole with a damped wobble.
- Moss, the token: a round body 72px tall, teal with a pale belly, two big eyes (white, ink pupils, one glint each) that blink once at 1.2 s, rosy cheeks, two stubby feet and a leaf sprout on top on a little spring (its angle lags the body's motion, closed form). Idle: a 2 Hz bob of 4px. Hops: from dot to dot in jumps of three dots (0.28 s each), arcing 40 units high, squashing to 1.15 × 0.85 on takeoff and landing and stretching to 0.9 × 1.12 at the top, its ground shadow shrinking with height, three cream dust puffs on each landing. The plank bridge dips 6 units under it and springs back.
- Camera: the SVG viewBox moves on cubic-bezier(0.45, 0, 0.2, 1): it opens at scale 1.0 centered on World 1 at (850, 720); pulls back to scale 0.56 centered at (1800, 720) for the new path so both worlds are whole in view; then pushes in to scale 1.0 centered on World 2 at (2650, 720), following Moss. Clouds pan 1.15× as fast as the map for parallax. Node labels, stars, chips and Moss keep their on-screen size as the camera zooms (counter-scale them by 1 ÷ scale), so labels never drop below 22px. A seeded paper-grain filter (feTurbulence, fixed seed) multiplies over everything at 6% and never moves.
- UI (fixed on screen, inline SVG and HTML): a butter ribbon banner at x 120–760, y 90–190 with folded ends, "WORLD 1" in Baloo 2 800, 26px, over "TANGLE SHORE" in Baloo 2 800, 52px, ink; chips ("WORLD 1 CLEAR!", "NEW PATH!") as rounded butter pills with an ink 3px edge in Baloo 2 800, 28px, that pop in near the action and leave after 1.2 s; the level card at x 1340–1800, y 800–990: a cream card #FFF6E3 with an ink 3px edge and 20px radius, the level name in Baloo 2 800, 34px, the stars and best time in Nunito 700, 24px, and a red rounded PLAY button with a cream triangle.
- Premium: a map that feels like a place (islands with cliff sides, moving water and clouds, a turning windmill), paths that pop in rhythm, a token with real squash, stretch and follow-through, and an unlock with several layered beats. Cheap: flat circles on a blue rectangle, a token that slides without hopping, dots that fade in all at once, a camera that cuts.
- Banned: real game characters, worlds, logos or fonts, look-alikes of any existing game mascot, realistic terrain or real geography, dark or desaturated colors, glow effects, motion blur, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.6s: on World 1: waves bob, clouds drift, the windmill turns; the banner unrolls; the dots of the cleared paths pop in from 1-1 to 1-4 (0.4–1.5 s) and each node's stars pop above it as its path completes; Moss idles on 1-4 and blinks.
- 1.6–3.0s: the path from 1-4 to the fortress draws (1.6–2.0 s); Moss hops along it (2.0–2.6 s) and lands at the gate; the fortress pennant flips to teal, three stars pop over it and "WORLD 1 CLEAR!" pops (2.7 s).
- 3.0–4.4s: "NEW PATH!": the dots run from the fortress across the four islets and the plank bridge toward World 2 (3.0–4.2 s) as the camera pulls back; the cloud bank over World 2 parts and drifts away (3.4–4.4 s), revealing the snowy peaks.
- 4.4–5.4s: 2-1 unlocks: the padlock jiggles, pops and drops, the node wipes to butter, the star ring bursts, the label and pennant spring up.
- 5.4–6.0s: settled. The 6.0 s frame shows both worlds whole: World 1 complete with all its stars, the red path across the sea, 2-1 unlocked and Moss waiting at the fortress.
- 6.0–8.0s: Moss hops the path from the fortress to 2-1, across the islets and over the bridge (it dips under each hop), as the camera pushes in on World 2; it lands on 2-1 with a big squash and its leaf spins once (7.9 s).
- 8.0–8.8s: the banner swaps: World 1's ribbon slides up out of frame and "WORLD 2 · LUMEN PEAKS" unrolls in its place; the level card slides in at the lower right.
- 8.8–10.0s: hold: Moss idles on 2-1, the waves bob and the clouds drift.
For other lengths, change the number of hops and the dot spacing in time; keep the unlock beats and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: inline SVG in the page: the map is built once at load as SVG groups (islands, scenery, paths, dots, nodes, clouds, waves) from a seeded PRNG, and each seek sets the viewBox, transforms, scales and opacity of what moves; the fixed UI is HTML and inline SVG above it. No canvas and no libraries.
- Dot positions come from getPointAtLength once at load; dot pops, hops, squash and stretch, the leaf's lag, the bridge's dip, the unlock beats, the wave bob, the cloud drift and the camera are closed-form functions of t from their start times.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check islands read with their cliff sides and foam lines, the dots pop in order along each path and never all at once, the stars match 3, 2, 3, 1 and then 3, Moss lands exactly on dots and nodes with squash, stretch and a shadow that shrinks in the air, the padlock opens and drops before the node changes color, both worlds are fully visible at 6.0 s, the banner and level card stay clear of the token and nodes, and nothing important sits within 60px of an edge. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
