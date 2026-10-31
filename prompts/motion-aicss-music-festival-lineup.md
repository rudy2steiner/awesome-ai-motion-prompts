# Festival Lineup


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/music-festival-lineup) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/music-festival-lineup) · [对应动效输出](https://www.aicssanimations.com/previews/music-festival-lineup.mp4)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 in Claude Code（来源声明，未独立复现）
- **分类：** music-audiovisual
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
Make a 10-second kinetic-type festival lineup poster: tiers of act names by day, stages and a sponsor strip build in on a beat in a bold, printed-looking palette.

<inputs>
If I don't give you something, use the default and don't ask.
- Festival: FERNHOLLOW FIELDS (fictional). Line: "Summer Sound · 16–18 July · Mossgrove Meadows".
- Badge: "3 DAYS · 4 STAGES · 27 ACTS ·"
- Friday 16 July: headliner MARIGOLD ENGINE; second tier Velvet Harbour · Tin Comet · Juniper Lows; third tier Saltlick · Penny Arcadia · Hollis Moon · Dusk Pilots · The Wren Machine.
- Saturday 17 July: headliner HALCYON TRAMS; second tier Lumen Swim · Brass Owls · Kettle & Kite; third tier Paper Orchard · Glow Fen · Mira and the Moths · Low Lantern · Okra Club.
- Sunday 18 July: headliner ORCHID TELEGRAPH; second tier Pebble Choir · Static Peaches · Cloudberry Club; third tier Moss & Marrow · June Avenue · Little Gale · The Otter Bells · Plum Radio.
- Stages: Main Meadow · The Barn · Woodland Stage · Late Tent.
- Sponsors: Halden Cider · Northlight Radio · Kestle Bikes · Oakum Coffee · Mapleway Rail.
- Stamp: SOLD OUT, on Friday. Tickets line: "Weekend and day tickets on sale now".
- All acts, sponsors and places are fictional: 27 acts in all.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a screen-printed summer festival poster set in motion: flat inks, a strict tier hierarchy, everything justified to its column, landing hard on a beat.
- Palette, five inks on a green ground: ground bottle green #0E4A37 with field rings in #0C4231; pink #FF8FC4 for the title, the day chips and the stamp; cream #FFF1DC for the headliners and the sponsor strip; tangerine #FF8A2B for the second tier, the badge and the marquee band; mint #A8E6C4 for the third tier and the line; type on pink, tangerine and cream is the ground green. Pink and tangerine sit side by side without touching; the green makes both glow without any glow effect.
- The field: eight broad concentric rings centered at (960, 1240), alternating #0E4A37 and #0C4231, in an SVG behind everything; they open from the center at the start and then breathe ±6px in radius on a 3s sine, easing still by 8.4s.
- Layout on the 1920×1080 stage:
  - the title FERNHOLLOW FIELDS in Big Shoulders Display 900, uppercase, on one line fitted to x 120–1560 (about 190px tall), pink, top at y 90; the line beneath it in Rubik 600, 30px, uppercase, tracked 0.12em, mint, baseline y 340;
  - the badge: a tangerine disc 220px across centered at (1700, 200) carrying the badge text around its edge in Rubik 700, 20px, green, and a small eight-spoke asterisk at its center;
  - three day columns, 540px wide, at x 120, 690 and 1260, from y 380: a pink pill chip 44px tall with the day in Rubik 700, 22px, green; the headliner in Anton 400, uppercase, its size solved so it spans exactly 540px (between 80 and 150px; a long name may compress to scaleX 0.86 first); a 2px mint rule at 40%; the second tier in Barlow Condensed 700, uppercase, about 46px, separated by small asterisks, in at most two lines, each line justified to 540px; the third tier in Barlow Condensed 500, uppercase, about 30px, in two justified lines;
  - the marquee: a tangerine band across the full width at y 868–918, the stages in Rubik 700, 26px, green, separated by asterisks (inline SVG), scrolling left;
  - the sponsor strip: a cream band across the full width at y 940–1015 with SUPPORTED BY in Rubik 600, 20px, tracked 0.14em, the tickets line in Rubik 500, 22px, and five fictional wordmarks in green, each its own treatment: Halden Cider in Lobster Two 700 italic, NORTHLIGHT RADIO in Righteous 400 with a small three-arc wave mark, Kestle Bikes in Syne 800 with a wheel circle, OAKUM COFFEE in Bitter 800 with a bean, Mapleway Rail in Krona One 400 with two parallel rails. Every name stays whole on one line; a name never breaks across lines.
- Fitting: after the fonts load, measure every headliner and tier line (canvas measureText or the DOM) and solve its size and word spacing so it lands exactly on the column edges; store the results so seek only applies them.
- Motion on a beat: the big landings fall on a 120 BPM grid (every 0.5s). Title letters drop 120px from above and land with a squash (scaleY 1.25 → 1 on cubic-bezier(0.2, 0.9, 0.3, 1), 0.22s), 45ms apart, each landing nudging its left neighbor down 4px and back over 0.12s. Chips flip in about their top edge (rotateX −90° → 0 with perspective, 0.3s). Headliners rise letter by letter through a mask at their baseline (30ms stagger) starting tracked +0.3em and tightening onto their fitted width over 0.35s on cubic-bezier(0.16, 1, 0.3, 1). Second-tier names drop 30px word by word on cubic-bezier(0.34, 1.56, 0.64, 1) over 0.3s, 40ms apart; the third tier cascades word by word, 30ms apart, rising 12px. The badge rolls in from the right edge like a wheel (rotation = distance ÷ radius) and keeps turning at 12°/s. The stamp slams from scale 1.3 to 1 in 0.12s, jolting its column down 3px. Nothing fades in by opacity alone.
- The stamp: SOLD OUT in Rubik Mono One 400, 34px, pink, inside a 4px pink rounded rectangle 250 × 70, at −9° over the right end of Friday's chip, clear of the headliner, with slightly rough ink edges (a seeded mask).
- Texture: a faint print grain (3%, seeded, static) over the inks, and each ink layer sits 1px off its neighbors at a fixed seeded offset, like a screen print.
- Premium: a strict hierarchy where every line meets its column edges, headliners that fit exactly, motion that lands on the beat, a palette that feels printed. Cheap: centered text in one font on a neon gradient, everything fading up at once. Banned: real artists, festivals, venues or sponsors, neon glow, gradients on type, drop shadows, 3D or extruded type, emoji, stock icons, a sixth color, names broken across lines, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.5s: the green ground; the field rings open from the bottom center.
- 0.5–1.4s: FERNHOLLOW FIELDS slams down letter by letter from the left.
- 1.5–2.0s: the line types on left to right; the badge rolls in and settles at its spot, still turning.
- 2.0–2.4s: the three day chips flip in, 0.1s apart.
- 2.5–3.9s: headliners: Friday at 2.5s, Saturday at 3.0s, Sunday at 3.5s, each rising and snapping to its column width; their rules draw.
- 4.0–5.4s: the second tier drops in column by column, then the third tier cascades.
- 5.5–6.0s: the marquee slides in from the left and scrolls at 120px/s; the sponsor strip rises from the bottom and its wordmarks pop in, 60ms apart (the 6.0s frame: the whole poster complete and readable).
- 6.5s: SOLD OUT slams onto Friday.
- 6.5–8.4s: the marquee eases to a stop with whole stage names in view; the badge and the rings ease to rest.
- 8.4–10.0s: hold, still.
For other lengths, keep the 0.5s beat grid and add or remove beats between tiers; keep at least 1s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: HTML/CSS: absolutely positioned elements (one span per animated letter or word) whose transforms, clip-paths and positions are set from seek; the field rings, asterisks and wordmark marks in inline SVG; the print grain and the stamp's rough edge drawn once at load into canvases.
- The marquee offset, the badge angle and the ring breathing are closed-form functions of t; every fitted size is measured once after the fonts load.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check each headliner spans exactly its 540px column, every tier line is justified to both edges, tiers step down clearly in size, no name breaks across lines, the stamp sits clear of every headliner, all text is at least 20px, the 6.0s frame is the complete poster, and big landings fall on the 0.5s grid. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
