# UI Flythrough Launch Film


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/ui-flythrough-launch-film) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/ui-flythrough-launch-film)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** product-brand
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
Make a 10-second software launch film in three.js: the camera glides low across a tilted wall of the product's screens with shallow depth of field, focus racing from one live screen to the next, then rises and pulls back until the whole wall sits behind the product name and "Available today".

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Tidewell (fictional), field-service software for plumbing, heating and electrical companies. Company: Tidewell Labs (fictional). URL: tidewell.app
- Customer shown in the screens: Ridgeway Mechanical (fictional), 14 technicians. Day shown: Thursday, Nov 5, 2026.
- Title lockup: "Tidewell" . "Run every job from one screen." . "Available today" . after the poster: "tidewell.app . Web, tablet and phone"
- Twelve screens on a 4 x 3 wall, columns left to right:
  Top row: Today's Schedule, Crew Chat, Weekly Report, Route Planner.
  Middle row: Customer Profile, Dispatch Map, Job #4821, Invoices.
  Bottom row: Team Settings, Parts Inventory, Technician Today, Quote Q-1187.
- Hero screens, which the camera stops on and which change while in focus: Dispatch Map, Job #4821 and Quote Q-1187.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a quiet, expensive launch film. A dark, warm room holds a wall of bright, legible product screens, filmed with a long lens and a thin focal plane. The interface is the star: one screen at a time is razor sharp while its neighbors melt into soft rectangles of light. The move is one continuous glide, never a cut.
- Palette, room: background and fog #15130F; wall backing #1D1A16; screen bezels #2A2622 with a #4A433B top-edge highlight; title #F6F2EA; secondary title text #BDB5A8; tertiary #8A8276; brand tangerine #FF6A2B (the mark, the pill's border and dot) and its tint #FF8F5E (pill text).
- Palette, inside the screens (a light UI): content background #F6F4EF; cards #FFFFFF; hairlines #E3DED4; ink #1C1A17; secondary text #6F6A61; sidebar pine #1E3A34 with nav text #D9E5E0, the active item on #2C5048 with a 4px tangerine bar; status green #2F8F6B (done, on site), blue #3A6FD8 (scheduled, en route), amber #D99A1E (break, low stock), red #D24A3B (late, overdue); map land #ECE7DC, water #CDE0E3, parks #DCE6CF, roads #FFFFFF with #D6CEC0 casings; buttons tangerine with white labels.
- Type: Bricolage Grotesque 700 for the title (148px, tracking -0.02em) and 600 for screen headings; Figtree 400/500/600 for everything else. Inside the screens, at the screen canvas's own resolution: headings 34px, body 22px, small labels 18px, tabular figures for every number.
- Every screen is a 1600x1000 canvas drawn in code, with the same chrome: a 64px white top bar with a bottom hairline, holding the Tidewell mark and "Ridgeway Mechanical" at the left and a search field "Search jobs, customers, parts" at the center; a 220px pine sidebar with Dispatch, Schedule, Jobs, Quotes, Invoices, Customers, Inventory, Reports and Team, the item for that screen active. Content starts at (252, 96).
- Dispatch Map: a map of an original small city fills the content (a river crossing diagonally, a park, a street grid at a slight angle); four route lines in the status colors with numbered stop pins; six technician vans as 36px rounded markers with initials (DO, MR, SL, AP, JB, KM). A right rail at x 1240-1584 titled "Today . 38 jobs" with "21 done . 11 in progress . 6 scheduled" and six rows, each with a status dot: "D. Okafor . On site . #4821", "M. Reyes . En route . 12 min", "S. Lindqvist . On site . #4826", "A. Patel . En route . 6 min", "J. Brennan . Break", "K. Moreau . Available".
- Job #4821: heading "Job #4821 . Furnace not igniting", "Elena Vasquez . 214 Larch St", technician "D. Okafor", a status chip (blue "En route", later green "On site"); a checklist: "Check thermostat", "Inspect igniter", "Test gas valve", "Replace igniter", "Run full cycle", the first two ticked; a timeline at the right: "8:12 Assigned", "8:40 En route", "9:06 On site" (the last row appears with the chip change).
- Quote Q-1187: heading "Quote Q-1187 . Elena Vasquez"; a table: "Hot surface igniter . 1 x $64.00 . $64.00", "Flame sensor . 1 x $38.00 . $38.00", and later "Labor . 1.5 h x $95.00 . $142.50"; totals that read "Subtotal $102.00 . Tax 8.25% $8.42 . Total $110.42" before the labor line and "Subtotal $244.50 . Tax 8.25% $20.17 . Total $264.67" after it; a tangerine "Send quote" button.
- The other nine screens are as real, and static: a schedule grid of six technicians from 7 AM to 5 PM with job blocks; a crew chat with three short messages about a part pickup; a weekly bar chart "Jobs completed: Mon 31 . Tue 36 . Wed 29 . Thu 41 . Fri 38 . 175 this week" with "Revenue $48,920"; a route of seven numbered stops; Elena Vasquez's profile with "6 past jobs . $2,310 lifetime"; invoices INV-2203 to INV-2208 with Paid, Due and Overdue chips; a team table of 14 members; an inventory table with two amber "Low stock" rows; a technician's day view with a big next-job card. Never lorem ipsum, empty boxes or "Feature 1".
- The wall lies flat in the world XY plane, facing +Z, centered on the origin (units are meters). Tiles are 3.2 x 2.0 with 0.36 gaps, so column centers sit at x -5.34, -1.78, 1.78, 5.34 and row centers at y 2.36, 0, -2.36. Each tile is a thin rounded slab (RoundedBoxGeometry 3.32 x 2.12 x 0.06, radius 0.025) in the bezel color with its screen on a plane 0.031 in front of it (the canvas draws the screen with 24px rounded corners and transparent outside). Tiles sit +0.14 or -0.10 off the wall in a seeded pattern, for parallax. A large backing plane sits 0.3 behind the tiles. The tilt is all camera: it looks across the wall from the left and slightly below, rolled 5 deg (camera.up tilted), so the rows run diagonally and the far columns recede.
- Shadows: behind each tile, a canvas-generated shadow on the backing: a rounded rectangle blurred by 60px, offset 0.12 down, 45% black at its center falling to zero, depthWrite false. Never a hard slab.
- Lighting: the screens are self-lit: MeshBasicMaterial, so they always read at full brightness. Slabs and backing are MeshStandardMaterial (roughness 0.55 and 0.9) lit by a HemisphereLight (#FFF3E4 over #2A241E, intensity 1.4), a warm key DirectionalLight from the upper left (#FFE6CC, 2.2) and a soft fill from the right (#D9E4FF, 0.5). No tone mapping (NoToneMapping) and sRGB output, so screens keep their exact colors. Fog #15130F from 14 to 42. The room must never read as a black void: the backing shows a visible warm falloff around the tiles.
- Depth of field: EffectComposer with RenderPass, BokehPass and OutputPass. Focus tracks the camera's distance to the hero screen's center; tune the aperture so the hero is razor sharp, its neighbors blur by about 10-14px on screen, maxblur 0.012. Each rack between screens takes 0.45 s on easeInOutSine and lands as the camera arrives. In the pull-back the focus moves to the wall's middle and the blur eases down to about 4px, so the whole wall is soft but recognizable behind the title.
- Camera, field of view 30 deg, one continuous path through these keyframes (position -> look-at point, both world):
  0.0 s (-7.6, -0.6, 3.6) -> (-4.4, 0, 0);
  1.2 s (-3.8, -0.6, 3.6) -> (-1.78, 0, 0), Dispatch Map;
  2.6 s (-0.2, -0.6, 3.6) -> (1.78, 0, 0), Job #4821;
  4.0 s (3.3, -3.0, 3.7) -> (5.34, -2.36, 0), Quote Q-1187;
  5.6 s (-9.0, -2.0, 18.0) -> (-4.2, 0, 0), the pull-back;
  8.8 s (-9.3, -2.0, 18.8) -> (-4.2, 0, 0).
  Interpolate positions and targets on centripetal Catmull-Rom curves. Speed: ease in over the first 0.6 s, a steady glide that slows by only about 15% at each hero screen until 4.0 s, easeInOutCubic for the pull-back, then an easeOutQuad drift that comes to rest at 8.8 s. At 6.0 s the wall should fill roughly x 660 to past the right edge of the frame, leaving the left third open for the title; adjust the pull-back keyframe to hit that framing.
- Tile settle: during the pull-back the tiles' parallax offsets ease to zero (easeInOutCubic, 4.4-5.6 s), so the wall settles flat just before the title lands.
- Live hero screens: while in focus, the Reyes and Patel vans move 60-90px along their routes and their minutes tick down once (12 -> 11, 6 -> 5); the job chip cross-fades from "En route" to "On site" and "Test gas valve" ticks, its check drawing in 0.18 s; the labor line slides in on the quote and the totals count up with tabular figures; the "Send quote" button darkens 12% for 0.15 s as if pressed.
- Title lockup, an HTML layer over the WebGL canvas so it stays crisp: a scrim, a linear gradient from #15130F at 88% (x 0) to 0% (x 1150). The mark at (140, 404): a 72px tangerine rounded square (radius 18) with three white wave strokes (5px, round caps, each a gentle two-hump curve). "Tidewell" in Bricolage Grotesque 700 148px #F6F2EA, left edge x 132, baseline y 600. "Run every job from one screen." in Figtree 500 40px #BDB5A8, baseline y 664. The "Available today" pill at (140, 712): 52px tall, radius 26, 1.5px tangerine border, a 10px tangerine dot at its left, text Figtree 600 24px #FF8F5E. After the poster, "tidewell.app . Web, tablet and phone" in Figtree 500 24px #8A8276, baseline y 830.
- Motion rules: the camera never stops dead before 5.6 s and never shakes; nothing on the wall rotates or flips; screen content changes only through UI state (chips, ticks, numbers, vans), never wipes.
- Premium: a slow, confident glide; one screen in razor focus at a time, with real, readable UI that changes as you watch; soft shadows and a warm room with depth; a calm title that holds. Cheap: screens spinning into place, lens flares, every tile glowing, smeared motion blur, blur so heavy it looks broken, perspective so steep the text can't be read, dashboards of random squiggles, a black void around the wall.
- Banned: purple or blue gradients, neon glow, lens flares, chromatic aberration, camera shake, glitch transitions, cuts, mockups of real devices, hype copy such as "Revolutionize", real company names, logos and UI copied from existing products, anything flashing more than 3 times a second.
</direction>

<structure>
- 0.0-0.6s: the film fades up from #15130F over 0.3 s, close on the middle row at the left, Customer Profile drifting past soft; focus already finding the Dispatch Map.
- 0.6-1.8s: the Dispatch Map is razor sharp by 1.0 s; the Reyes and Patel vans travel along their routes and their minutes tick down (1.3 s and 1.5 s).
- 1.8-3.2s: the glide carries on; focus racks to Job #4821 (1.95-2.4 s); the chip turns "On site" at 2.5 s (0.2 s cross-fade) and the 9:06 row appears; "Test gas valve" ticks at 2.8 s.
- 3.2-4.4s: the camera descends to the bottom row; focus racks to Quote Q-1187 (3.4-3.85 s); the labor line slides in at 3.95 s and the totals count up to $264.67 by 4.3 s; "Send quote" presses at 4.35 s.
- 4.4-5.6s: the pull-back: the camera rises and retreats, the blur eases off, the tiles settle flat, the warm falloff of the room opens up; the scrim fades in from 4.8 s.
- 5.1-5.9s: the title lands: the mark scales up from 0.9 as it fades in (5.1-5.4 s, easeOutCubic); "Tidewell" rises 24px through a mask (5.2-5.6 s, easeOutExpo); the line fades up (5.45-5.8 s); the pill's border draws clockwise from the dot and its text fades in (5.6-5.9 s).
- 6.0s: the hero frame: the whole wall soft and recognizable across the right two-thirds, the complete title lockup on the left, every word readable.
- 6.0-8.8s: the slow drift back comes to rest; the URL line fades up at 7.0 s.
- 8.8-10.0s: hold, completely still.
For other lengths, stretch the glide between hero screens and the hold; keep the pull-back about 1.2 s and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920x1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face and weight before drawing any screen canvas and before defining window.seek.
- Engine: three.js through an importmap from jsDelivr: "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js" and "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/" (EffectComposer, RenderPass, BokehPass, OutputPass, RoundedBoxGeometry). WebGLRenderer with antialias and preserveDrawingBuffer: true, setPixelRatio(devicePixelRatio), sized to the stage; render the composer inside seek, never in a loop of its own.
- Screen textures: CanvasTexture with colorSpace SRGBColorSpace and anisotropy at the renderer's maximum. Draw all twelve at load; inside seek, redraw only the three hero canvases from t (their state comes from one timed script) and set needsUpdate. The title layer is HTML over the canvas, its state also set in seek.
</build>

<check>
Before showing me, step through one frame per second (t = 0...10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that at 1.0 s the Dispatch Map is razor sharp with its neighbors soft; at 2.6 s Job #4821 is sharp and reads "On site"; at 4.2 s Quote Q-1187 is sharp and its numbers add up to $264.67; the screens are bright and never underlit; the room shows a warm falloff, not a black void; no shadow reads as a hard grey slab; and the blur never looks like a rendering bug. At 6.0 s the whole wall sits across the right two-thirds with the complete title lockup on the left and every word readable. The final frame adds the URL line and nothing moves after 8.8 s. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
