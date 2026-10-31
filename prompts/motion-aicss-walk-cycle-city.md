# Walk Cycle


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/walk-cycle-city) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/walk-cycle-city)

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
Make a 10-second character walk: a crafted side-view walk cycle down a city street in parallax, ending as the walker stops at a cafe door.

<inputs>
If I don't give you something, use the default and don't ask.
- Walker: a young woman in a cobalt coat, a tomato-red scarf, charcoal trousers and cream sneakers, a mustard tote on her shoulder.
- Street: Hazel Row (fictional), passing Hazel Row Bakery, Second Shelf Books and Fern & Stem, and stopping at Ninth Hour Cafe.
- Title: "On Foot"
- Line: "Hazel Row, 7:45 am"
- Length: 10 seconds.
</inputs>

<direction>
- Look: editorial illustration in gouache: flat shapes in a warm morning palette, each with a dry, slightly uneven painted texture and soft irregular edges, staged as a side-scrolling street in four parallax planes. The walk is the star.
- Palette: sky #F7DCBF with a pale sun disc #FFF0D6 high right; far skyline #C2B0CF and #AE9BC0; shopfronts terracotta #D8684A, sage #8DAE8A, mustard #E2AE4A and teal #2F6F73, cream trim #F4E8D4, window glass #3E4A5C with a warm reflection band #F5C88E; awnings striped in pairs of those colors; sidewalk #DCCDB7 with paving joints #C4B39B; curb #B4A28B; road #6E6874; lamp posts #24423A; walker coat #2D4EA6 (shade #213B7E), scarf #E2483D, trousers #2B2A33, sneakers #EFE6D6 with soles #C9BBA5, skin #C68A64, hair #2A1D19, tote #E8B847; text #2B2A33.
- Gouache texture, generated once at load: a seeded paper grain plus a directional brush-streak texture, multiplied over every plane at 18%; each shape's edge is displaced by fixed seeded noise (+/-1.5px) so it reads painted and never boils.
- Layout: the walker stays at x 820 with her feet on y 905. The sidewalk spans y 850-940, the curb 940-960, and a strip of road runs below. Shopfronts stand on y 850 and rise no higher than y 330; everything above y 320 is sky, clouds and the sun, so the title sits on open sky.
- Planes and speeds, as the camera tracks the walker: clouds 0.08x, far skyline 0.3x, the shop row 0.85x, sidewalk and curb 1.0x, and foreground lamp posts on the curb at 1.35x. Paint the shop row once at load into a long offscreen strip: four shops separated by brick piers, each with a striped awning, a sign, windows with goods on shelves (loaves, book spines, flower buckets, cups and a coffee machine), a door and a planter. Solve its offset so the cafe door is centered at x 1080 when she stops. Foreground lamps pass in front of her only around 1.6 s and 4.2 s, never near 6.0 s or after 7.0 s.
- The walker: 470px tall, in profile facing right, a 2D rig drawn from joint positions every frame: pelvis, torso, neck, head with hair, upper and lower arms, hands, thighs, shins, feet, and toes that bend at toe-off. The coat hem, scarf ends and tote are secondary chains.
- The walk, from real key poses: one step every 0.5 s (a 1.0 s cycle) with a 230px stride, so the ground moves at exactly 460 px/s and the planted foot never slides.
- Contact (0% of a step): front leg forward and straight, heel down and toe up 15 deg; back leg behind, on its toe; arms at their widest, opposite to the legs.
- Down (20%): weight drops onto the front leg, knee bending 18 deg; the pelvis at its lowest (-14px).
- Passing (50%): the support leg under the hips, nearly straight; the swing leg bent about 60 deg at the knee, foot 40px up; arms passing the body.
- Up (75%): the support leg pushes off, heel lifting; the pelvis at its highest (+8px); the swing leg reaches forward.
Interpolate joint angles between the keys with a Catmull-Rom spline over the step phase. The head follows the pelvis bob 0.04 s late with a 2 deg nod; the shoulders counter-rotate against the hips (shown as a 3% change in torso width); the hands travel in arcs.
- Follow-through, computed analytically from the walk phase: the scarf (a 10-segment chain) trails back and lifts on each up, its tip 0.12 s behind; the tote swings as a damped pendulum 0.1 s behind the shoulder; the coat hem flips 6 deg on each passing.
- The stop: the last steps shorten (230, then 150, then 70px) as the ground slows to match; both feet plant, the body overshoots 6px forward and settles back on cubic-bezier(0.2, 0, 0, 1) over 0.5 s; the scarf and tote swing forward past vertical and settle over 0.6 s; the head turns toward the camera through one in-between drawing into a three-quarter view.
- Type: shop signs in "Instrument Serif" 400, 48px, with small lines in "Instrument Sans" 600, 20px, uppercase, tracked 0.18em; the title in Instrument Serif italic, 120px, #2B2A33, top-left at (120, 90); the line in Instrument Sans 500, 26px, uppercase, tracked 0.16em, beneath. Text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: a walk with weight (contact, down, passing, up), a foot that sticks to the pavement, arcs and follow-through, and parallax that sells depth. Cheap: scissor legs swinging from the hip, a body gliding at one height, feet skating over a scrolling ground. Banned: feet sliding during contact, legs with no knee bend, a constant-height body, motion blur, outlines on every shape, real shop or brand names, crowds or traffic, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0-0.6s: already walking from the first frame (t = 0 is a contact pose), the street scrolling, the bakery behind her.
- 0.6-2.4s: past Hazel Row Bakery; a lamp post sweeps by in front around 1.6 s.
- 2.4-4.4s: past Second Shelf Books; a gust at 3.2 s doubles the scarf's swing for one cycle; a second lamp passes around 4.2 s.
- 4.4-6.6s: past Fern & Stem; she glances at the flower buckets (the head dips 6 deg and returns, 5.2-5.8 s). At 6.0 s she is on a contact pose in front of the florist with no lamp near her: a clean, complete stride.
- 6.6-8.0s: the cafe comes into view; her strides shorten and the ground slows.
- 7.6-8.6s: the title and line rise in.
- 8.0-8.8s: the stop at the cafe door: feet planted, overshoot and settle, scarf and tote swing and settle, the head turns toward the camera.
- 8.8-10.0s: hold, still.
For other lengths, add or remove whole walk cycles before the stop and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920x1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size * devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. No other libraries.
- Paint the sky, skyline, shop strip and textures once at load into offscreen canvases; each frame composites the planes at their offsets and draws the walker's rig fresh. Distance walked is the closed-form integral of speed, and the step phase comes from that distance and the step table (full strides, then 150 and 70px), so every pose and secondary chain is a direct function of t. Request Instrument Serif in both roman and italic.
</build>

<check>
Before showing me, step through one frame per second (t = 0...10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the planted foot holds still against the pavement through every contact (log its position relative to the ground across a step: drift under 1px), the pelvis is lowest on down and highest on up, the arms swing opposite the legs, the 6.0 s frame is a clean contact pose with no lamp over her, the cafe door lands centered at x 1080, and the title sits on open sky. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
