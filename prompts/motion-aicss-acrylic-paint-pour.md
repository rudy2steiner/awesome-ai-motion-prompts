# Paint Pour

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/acrylic-paint-pour) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/acrylic-paint-pour)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second fluid-art film: layered acrylic paint pours from a cup onto a canvas in rings, cells bloom open, and the canvas tilts so the paint stretches and runs off the edges.

<inputs>
If I don't give you something, use the default and don't ask.
- Studio: Pellmoor Pour Studio (fictional).
- Title: "Let it run"
- Line: "Acrylic ring pour on a 50 cm canvas · No. 118"
- Cup layers, in the order they leave the cup: apricot, pearl with silicone, oxblood, sea glass, copper metallic, persimmon, pearl with silicone, petrol.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a glossy studio close-up of wet acrylic: a 50 × 50 cm stretched canvas on kraft paper, the paint behaving like a heavy liquid (rings that push each other outward, cells that open, tongues that stretch as it tilts), with a broad softbox reflection sliding over the wet surface.
- Palette: kraft bench paper #C6A27A with a few old dried drips; canvas primer #F3F0EA with a fine weave; paints petrol #123C43, pearl #F1ECE2 with a faint mica shimmer, persimmon #E5613A, copper metallic #C27A4A, sea glass #8FC9B8, oxblood #6B1E2A, apricot #F2B07E; cell lacing darkens each color by 18%; type #2B1D16, secondary #6E513E, accent persimmon. Petrol and sea glass are the cool pair, persimmon, apricot and oxblood the warm run, copper the metal that catches light between them; the kraft ground keeps the whole thing warm.
- The paint model is exact and area-preserving, like real incompressible paint: the surface is a list of operations, and each fragment is colored by undoing them: the tilts newest first, then the spread, then the drops. Nothing is painted into a buffer, so any frame is direct.
  - Pour: the stream lands as 72 small drops, one every 33 ms over 2.4 s, at a pour point that wanders on a slow 4 cm loop. Drop i of radius rᵢ at cᵢ pushes everything outward; to undo it for a point q: if |q − cᵢ| < rᵢ the paint is drop i's color, else q ← cᵢ + (q − cᵢ)·√(1 − rᵢ²/|q − cᵢ|²). Each drop takes the cup layer leaving at that moment, in the order above and by volume, so the puddle grows off-center concentric rings. The drops total 1,050 cm², a puddle about 37 cm across.
  - Spread: as the paint levels and thins it spreads about the puddle's center c: q' = c + s(t)·(q − c), with s rising from 1.0 to 1.25 by 3.6 s and to 1.75 by 8.2 s on easeInOutSine, so the film covers more of the canvas as it thins; undo by dividing by s.
  - Tilts: each is a shear along its downhill direction m: q' = q + z(t)·φ(q·n)·m, with n perpendicular to m and φ a smooth seeded 1D noise profile (3 octaves, between 0.4 and 1.0) so paint advances in tongues. Because q·n doesn't change, undo it exactly with q ← q − z·φ(q·n)·m. Four tilts in sequence: toward the lower right, the upper right, the upper left and the lower left, each z easing up to 18–26 cm, enough to carry paint off every edge.
  - Cells: about 900, seeded in the poured coordinates (after undoing the tilts and the spread, before undoing the drops) inside the two pearl-with-silicone layers and the copper, radius 0.1–0.6 cm, each opening over 0.6 s from a seeded birth time between 3.2 and 5.6 s: inside, the color of the layer beneath (petrol under the pearl, pearl under the copper); a lacing ring 0.04 cm wide, 18% darker; a few nested two deep. Because they live in poured coordinates, every later tilt stretches them into ellipses and teardrops.
  - Wet surface: a height field from the same structure (ring boundaries and cell rims 0.02 cm proud, level elsewhere) gives the normals; the paint is a glossy dielectric (roughness 0.08), and the copper layer is metallic with an anisotropic streak along the local flow.
- Edges: wherever paint reaches an edge it runs over it and down the canvas side as drips: per 1 cm of edge, a seeded drip that lengthens at 3–8 cm/s while that edge is downhill, colored by the paint at the edge, with a rounded bead at its tip, falling onto the kraft paper as small puddles. The sides use the same undo to find their colors.
- The cup: a clear plastic cup (LatheGeometry, transmission 0.9, roughness 0.05) tipped over the canvas, its layered paint visible through the wall as stacked bands that drain in order; the stream is a falling ribbon 1.2 cm wide whose stripes are the cup's layers, swaying ±0.3 cm, thinning to a thread and breaking off at the end of the pour.
- Light, bright and glossy from the first frame: the paint shader reflects a procedural studio (a broad overhead rounded-rectangle softbox and a warm side strip), so a large soft highlight lies across the wet paint and slides as the canvas tilts; a RectAreaLight softbox for the rest of the scene, with RectAreaLightUniformsLib; a key DirectionalLight #FFF4E6 at 2.2 with soft shadows (PCFSoftShadowMap, 2048) for the cup and canvas edges; a HemisphereLight #FFF8EE / #8C6A4C at 0.9. ACESFilmic, exposure 1.05.
- The canvas tilts in 3D: the board (a box 50 × 50 × 3.5 with wrapped canvas sides) rotates up to 9° about the axis perpendicular to each tilt's direction on easeInOutSine, back to level between tilts, so the paint visibly runs downhill.
- Camera: fov 32. A three-quarter view at 50° pitch during the pour, the cup and stream at the upper right and the puddle at (1060, 600); rising to near top-down (80° pitch) as the tilts begin; at the end the canvas is about 840px across, centered at (1120, 560).
- Type (HTML over the canvas): kicker "PELLMOOR POUR STUDIO" in Syne 700, 20px, tracked 0.16em, accent; title Syne 800, 96px, #2B1D16, top-left at (120, 110); line Epilogue 400, 26px, secondary, beneath. Text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: rings that push each other out, cells with lacing that stretch with the flow, a wet reflection that slides with the tilt, real drips off the edges. Cheap: a swirl filter over random blobs, cells pasted on top as polka dots, a flat matte image.
Banned: noise warps or twirl filters, blur, colors mixing into mud, cells that don't move with the paint, glitter, hands, palette knives or brushes, bloom, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: the primed canvas on kraft paper, the cup tipping into frame at the upper right; the kicker and title rise in.
- 0.6–3.0s: the pour: the striped stream lands and rings bloom off-center, each new color pushing the last outward; the cup's bands drain; the stream thins and breaks off at 3.0 s.
- 3.0–3.6s: the camera rises toward top-down; the first cells open in the pearl rings.
- 3.6–5.8s: the first two tilts, toward the lower right and the upper right: paint runs in tongues to the edges and over them, cells stretch into teardrops, drips run down the sides; the canvas is level again by 5.8 s.
- 5.8–6.2s: a still beat: at 6.0 s the canvas lies level, about 85% covered in stretched rings and lace-edged cells, drips hanging off two sides.
- 6.2–8.2s: the last two tilts carry the paint into the bare corners and off every edge; the softbox highlight slides across the wet paint.
- 8.2–8.8s: the canvas levels and the flow stops; the line rises in at 8.4 s.
- 8.8–10.0s: hold; only the wet highlight shifts a few pixels.
For other lengths, change the number of tilts; keep the pour at 2.4 s and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- The paint is a ShaderMaterial on the canvas's top face that evaluates the operation list per fragment (drops, tilts and cells in uniform arrays or a small float texture), undoing the tilt shears exactly, then the spread, then the drops; the sides' drips use the same undo. All drop, tilt and cell parameters are seeded once at load, and every amount is a closed-form function of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check each new drop pushes the earlier rings outward with no gaps or overlaps, cells open only in the pearl and copper layers and stretch with every tilt, the canvas visibly tilts and the paint runs downhill, drips appear only where paint reached an edge, the softbox highlight slides over the wet paint, nothing smears into mud, the 6.0 s frame is the level, still canvas, and the canvas is fully covered by the end. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
