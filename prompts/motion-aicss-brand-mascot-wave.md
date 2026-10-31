# Brand Mascot


[原作](https://www.aicssanimations.com/directory/Motion-Prompts/brand-mascot-wave) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/brand-mascot-wave) · [对应动效输出](https://www.aicssanimations.com/previews/brand-mascot-wave.mp4)

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
Make a 10-second brand mascot sting: an original vinyl-toy mascot hops in, waves, beams with a heart, then catches a sign with the brand name.

<inputs>
- Brand: "Potterwick" (a fictional houseplant delivery shop).
- Mascot: Pim, a small terracotta plant pot with a two-leaf sprout (design below).
- Tagline: "Plants, delivered happy."
- Backdrop: mint.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Look: a soft vinyl designer toy photographed in a seamless studio cove.
Palette: cove mint #BFE8D4 (floor a touch lighter, #CDEFDF), pot terracotta #D9734E with rim #C4623F, soil #5A3A2A, leaves #4DB36B and #7BD389, eyes #1E1A1A, cheeks #FF8FA3, mouth #5C2333 with tongue #FF7A8A, heart #FF5C7A, sign board cream #FFF6E8 with deep green type #1F5C3A, tagline #1F5C3A.
Model, all procedural: the pot body is a LatheGeometry profile (base radius 0.62, top 0.80, height 1.25) with a rim band 0.18 tall and slightly wider; a soil disc on top; a curved TubeGeometry stem 0.35 tall carrying two leaves (flattened, pointed spheroids, 0.34 × 0.06 × 0.18) angled outward. Face on the front: two glossy ellipsoid eyes (0.11 × 0.15 × 0.05) half-embedded, each with a small white specular dot; a mouth extruded from a rounded "D" shape, with a tongue; blush discs. Arms are short capsules (radius 0.08, length 0.26) with ball hands; feet are two flattened spheres.
Materials: MeshPhysicalMaterial, roughness 0.45, clearcoat 0.6, clearcoatRoughness 0.3, for a vinyl sheen; eyes at roughness 0.1.
Light and camera: RoomEnvironment through PMREMGenerator (environment intensity 0.6), a key DirectionalLight from the upper left (intensity 2.2) with PCFSoft shadows on a 2048 map, and a warm fill; ACESFilmic tone mapping, sRGB output. The cove is one plane curving up into a wall, with a ShadowMaterial catcher grounding Pim. PerspectiveCamera at fov 30, framed so the final pose fills about x 640–1280 and y 250–860 on the stage, with a slow 4° orbit across the piece.
Animation follows the classic principles literally: anticipation before every big move, squash on landing (scaleY 0.82, x and z 1/√0.82) and stretch on take-off (1.12), arcs for the hands, overlapping action (arms settle 60ms after the body), and follow-through on the sprout leaves as a damped spring lagging the body by 80ms, θ(τ) = A·e^(−5τ)·sin(14τ). Everything is a closed-form function of t.
Face acting: blinks squash the eyes to 10% height over 0.12s; the happy emote swaps the eyes for upward arcs (half TorusGeometry), brightens the cheeks and opens the mouth wider; a bevelled 3D heart (ExtrudeGeometry from a heart Shape) springs up above the sprout, floats 0.3 units and shrinks away.
The sign: a rounded board (RoundedBoxGeometry, 2.3 × 0.7 × 0.08) whose face is a CanvasTexture of the brand name in Baloo 2 800, drawn after the font loads (sRGB color space, maximum anisotropy). Pim holds it in front of the lower pot with a hand on each top corner, the face and sprout fully visible above it.
Tagline: HTML text in Baloo 2 600, 40px, centered at y 960.
Premium: toy-like materials under real light, the principles visible in every move, a restrained palette and one idea per beat. Cheap: rigid parts sliding around, default plastic, a clip-art face, constant bouncing.
Banned: likenesses of existing mascots (no owls, no candy-shell characters, no tire men), loaded models, image textures (the sign's canvas texture is the only texture), 3D text geometry, harsh black shadows, motion that never settles, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: an empty mint cove in soft light.
- 0.6–2.2s: Pim hops in from frame left in three hops (each a 0.5s parabola 0.6 units high, stretch on take-off, squash on landing), arriving center at 2.0s; the leaves flop and settle.
- 2.2–2.6s: Pim turns 15° toward camera and blinks.
- 2.6–4.0s: wave: a small dip (anticipation), the right arm rises, the hand waves three arcs of ±30°, the body sways against it.
- 4.0–5.4s: emote: happy-arc eyes, brighter cheeks, and the heart springs up behind the sprout, shrinking away by 5.3s.
- 5.4–6.2s: Pim looks up, leaning back 8°; the sign drops in from above on a spring.
- 6.2–6.6s: catch: hands on the top corners, squash 0.85, leaves flop.
- 6.6–7.6s: a small proud hop lifts the sign 0.15 units and settles; the tagline rises 16px and fades in (0.5s).
- 7.6–8.4s: a last blink and smile; the leaves settle.
- 8.4–10.0s: hold, still.
Other lengths: stretch the wave and the hold; keep each action's own timing.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative (growth, simulation, particles) is precomputed once at load at a fixed step or solved analytically, so seek can jump to any time. Past the end, hold the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`), with RoundedBoxGeometry and RoomEnvironment from the addons. WebGLRenderer with preserveDrawingBuffer: true and setPixelRatio(devicePixelRatio); seek sets every transform and material value from t, then renders once.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the face is never hidden by the sign or an arm, hands touch what they hold, nothing interpenetrates (hands through the pot, the sign through the body), squashes keep volume, the shadow grounds Pim at every landing, and the sign text is sharp at 1280×720. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
