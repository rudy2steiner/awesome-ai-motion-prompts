---
title: "Underwater Caustics Animation Prompt for Claude"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/underwater-caustics"
license: "CC0"
collected: "2026-11-03"
---

# Underwater Caustics Animation Prompt for Claude

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/underwater-caustics](https://www.aicssanimations.com/directory/Motion-Prompts/underwater-caustics)  
**License:** CC0

## Prompt

```
Make a 10-second underwater shot over a shallow sandy seabed: sunlight caustics ripple across the sand, light shafts sway through the water, and a school of fish passes as silhouettes.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Light on Sand"
- Line: "Pellam Cay · 6 m · 11:20" (fictional)
- School: 260 small silver fish.
- Length: 10 seconds.
</inputs>

<direction>
- Palette: open water #5CCFD6 high in the frame, #1C8FA6 at mid distance, #0B4F6B far; sand lit #F1DFB0, base #CDB27C, shaded #8F7A5A turning bluer with distance; caustic light #FFF7DC; rocks #5E6E6A with algae #6F8F5A; seagrass #3F7F4E to #8DBB5A at the tips; fish backs #0E3A4C shading to silvery bellies #7FA9B5; title #063447, line #0E5A70.
- Scene: a 60 × 60 m seabed 6 m under the surface at noon. The sand carries wave ripple marks (crests 25 cm apart, slightly sharp, sinuous, with a few forks where one crest splits in two) over broad undulations, fine grain from a procedural normal map, scattered shells, three rocks with algae tufts and three clumps of seagrass (instanced curved blades that lean with a 6 s surge, each on its own phase). The surface itself is never seen.
- Caustics, computed like the real thing: the surface is a sum of five waves whose speeds follow deep-water dispersion (ω = √(gk)), wavelengths 0.6–3 m, so periods run 0.6–1.4 s, each wave vector a whole number of cycles across a 12 m tile. Refract the sun (12° from vertical) through a 512 × 512 grid of surface points with Snell's law (n = 1.33) down 6 m to the seabed, and render that grid as a mesh into a 1024 × 1024 half-float caustics texture covering the tile: each vertex sits where its ray lands, and brightness is the cell's original area divided by its landed area (from dFdx and dFdy of both positions), blended additively. Draw it nine times, offset by ±1 tile, so the wrap has no seams. The result is a net of thin, bright, curving filaments around darker cells that drifts and reforms continuously, the filaments reaching 2.4× the plain sunlit sand. A faint color split (red and blue landing 1% apart) fringes the brightest lines.
- Light: a DirectionalLight sun 12° off vertical (soft shadows, PCFSoftShadowMap, 2048 map), with the caustics texture multiplied into its direct term on the sand, rocks, grass and fish (via onBeforeCompile), so the fish's shadows cut holes in the caustics too. HemisphereLight #8EE6F0 above and #C8B07A below at 0.8. Water fog by distance toward the palette's water colors (fully water-colored by about 22 m). ACESFilmic, exposure 1.0. The sand is bright and clearly lit from the first frame.
- Light shafts: 18 long, soft additive beams along the refracted sun direction, 0.2–0.8 m wide, at different depths, each fading downward and with distance, their brightness taken from the caustics texture at their entry point, so they brighten, break and sway as the waves focus the light; together they never add more than 25% to any pixel. 1,200 suspended particles (1–2px) drift slowly and catch light inside the shafts.
- Fish: 260 sardine-like fish, 14 cm long: a laterally flattened spindle body, a forked tail and a small dorsal fin, as instanced meshes whose bodies bend in a tail-beat wave at 2.5–3 Hz. The school is precomputed at load at a fixed 1/60 s step with boids rules (separation inside one body length, alignment and cohesion with the 7 nearest fish, 0.9–1.3 m/s), steered by one invisible leader target: it enters from the left at 2.4 s, 1–2.4 m above the sand, streams across the upper half of the frame, and from 6.8 s curves back so the school settles into a slow, loose mill centered at about (1280, 420). Against the open water the fish read as dark silhouettes.
- Camera: fov 50, 1.6 m above the sand, pitched down 18° so open water fills the top and sand the lower 60%; it drifts forward at 0.25 m/s and sways ±3 cm on a 4 s sine, like a diver holding position, easing to rest by 8.6 s.
- Type (HTML over the canvas): title in Sora 600, 88px, #063447, baseline at (120, 190) over the bright open water; line in Sora 400, 24px, tracked 0.08em, #0E5A70, beneath. Each rises 12px as it fades in over 0.8 s on cubic-bezier(0.22, 1, 0.36, 1). The fish stay below y 300.
- Premium: filaments that truly come from the waves, sharp and always reforming, shafts that brighten where the light focuses, ripple-marked sand, fish shadows breaking the light. Cheap: a scrolling caustic texture, blue fog, cartoon fish.
Banned: cartoon fish or faces, divers or bubbles, a tiled texture sliding over the sand, a flicker over the whole frame, lens flares, colors beyond the palette, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the seabed in bright noon light, caustics already crawling over the ripples; shafts sway; particles drift.
- 1.2–2.4s: the camera drifts forward; the seagrass leans with the surge; the title and line rise in.
- 2.4–4.4s: the school streams in from the left, a dark ribbon of fish against the open water, its shadows sliding over the caustics.
- 4.4–6.8s: the school crosses the frame and turns as one, thickening where it banks.
- 6.8–8.6s: the lead fish curve back and the school settles into a loose mill right of center; the camera drift eases to rest.
- 8.6–10.0s: hold: camera and type still; the caustics, shafts, grass and milling school keep moving.
For other lengths, stretch the crossing; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- In every seek, render the caustics mesh into its render target first, then the scene. Waves, caustics, shafts and camera are closed-form functions of t; the school is read from the precomputed arrays.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the caustics are thin filaments rather than blobs and that they reshape rather than slide, nothing pulses over the whole frame, fish shadows darken the caustics under them, each fish reads as a fish at 1280×720, and the title stays clear of the school and reads against the water. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
