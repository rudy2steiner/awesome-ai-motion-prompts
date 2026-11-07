# Cloud Inversion

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/cloud-inversion-timelapse) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/cloud-inversion-timelapse)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second sunrise time-lapse from a mountain summit above a cloud inversion: a sea of cloud fills the far valley and pours over a saddle in the ridge like a slow waterfall as the light turns from blue to gold.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Cloudfall"
- Line: "Skelmir Ridge · sunrise" (fictional)
- Time-lapse clock: 05:52 to 06:52
- Length: 10 seconds.
</inputs>

<direction>
- Look: a locked-off time-lapse, one hour in 10 seconds. Beyond the main ridge a flat sea of cloud fills the basin to the horizon, held down by the warm air above it; it overflows a low saddle in the ridge and cascades down the near side, thinning and vanishing partway down as the sinking air warms. The near valley stays clear. The high peaks catch pink light first, then gold light sweeps down to the cloud.
- Palette: sky before dawn #1F2A4D at the top, #5B5F8C, #C98A9B low down; after sunrise #6F8FC4 at the top and #F4B183 to #FFD7A0 low on the right, toward the sun; cloud in shade #6B7398, lit tops #FFE6CF, alpenglow #F2A9A6; rock in shade #2C2A33, lit faces #B07A5E to #D9A27A; snow #E9E4EC; foreground rock #26242B with lichen #6E7A4E and a lit rim #E7B98E; title #FFF4EA, line #F1D9C9.
- Terrain, as meshes (512 segments each, seeded ridged multifractal, MeshStandardMaterial roughness 0.9 with a procedural rock normal and faint strata, snow where the slope is under 35° above 2,500 m): a far range of peaks from 2,600 to 3,200 m rising out of the cloud sea; the main ridge across the middle of the frame 4 km away, with a saddle at 1,650 m around x 760; and the foreground summit rocks in the lower-right corner, where the camera stands at 2,400 m.
- Clouds: a raymarched volume in a full-screen pass after the terrain, which renders to a render target with a DepthTexture so rays stop at the rock. Density is the inversion layer (below a top at 1,760 m with a 30 m soft boundary, displaced ±20 m by billows) times domain-warped fBm (5 octaves), moved by a flow field: a slow drift across the basin toward the saddle, then down the near slope's gradient, speeding up as it falls. Past the saddle, density fades by e^(−drop ÷ 150 m), so the cascade evaporates within about 300 m of descent. Use two-phase flow noise (sample at p − v(p)·τ for τ = fract(t ÷ 3 s) and fract(t ÷ 3 s + 0.5), crossfaded with a triangle weight) so the cloud streams without smearing. Lighting: 48 primary steps; 6 steps toward the sun with Beer–Lambert extinction; a Henyey–Greenstein phase (g 0.6) for bright edges toward the sun; an ambient term from the sky color, so shaded cloud is lilac-blue, never grey or black; and peak shadows, by checking a heightfield texture of the terrain along each light ray, so the peaks throw long shadows across the cloud top. A fixed per-pixel jitter, the same on every frame, hides banding without boiling.
- Light over time: before sunrise, sky light only (HemisphereLight at 1.0), with everything readable. From 2.8 s, alpenglow: direct pink light #FF9C9C falls only on terrain above an altitude that drops from 3,300 m to 2,400 m by 4.2 s. At 4.2 s the sun clears the horizon out of frame to the right (about 60° right of the view): a DirectionalLight #FFC48A, warming to #FFE7C8 by the end, its lit line continuing down the slopes and reaching the cloud tops by 5.0 s, raking from the right so every peak's shadow falls left across the cloud sea. ACESFilmic, with exposure rising smoothly with the light and never jumping between frames.
- Camera: fov 45 on a tripod at the summit, looking across the near valley at the main ridge, the horizon at y 380, with a motorized slider move of 2% to the left across the piece on easeInOutSine. Nothing shakes.
- Type (HTML over the canvas): title in Marcellus 400, 104px, uppercase, tracked 0.08em, #FFF4EA, baseline at (120, 200) on the darker upper-left sky; line in Plus Jakarta Sans 500, 24px, uppercase, tracked 0.2em, #F1D9C9, beneath; the clock in Plus Jakarta Sans 500, 22px, tabular figures, right-aligned at (1800, 1010), counting from 05:52 to 06:52. Title and line rise 10px as they fade in over 1.0 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: cloud that behaves like air: a level top held down by the inversion, a spill over the saddle that speeds up and burns off as it falls, peaks turning pink before the valley, peak shadows across the cloud sea. Cheap: fog sprites sliding sideways, a gradient sunrise, cotton-ball clouds.
Banned: cotton-ball or sprite clouds, a cloud top that isn't level, birds, people, the sun disc or lens flares in frame, rainbows, camera shake, exposure jumps (time-lapse flicker), noise that boils, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: blue hour: the cloud sea lies lilac-blue in the basin and already spills over the saddle; the clock reads 05:52.
- 1.2–2.8s: the title and line fade in; the sky warms on the right; the cloud top flows toward the saddle and the cascade pours down the near slope, fading as it falls.
- 2.8–4.2s: alpenglow: the highest far peaks turn pink, and the pink line slides down them.
- 4.2–6.0s: sunrise: gold light breaks across the cloud tops from the right, the peaks cast long blue shadows across the cloud sea, and the main ridge's faces light up.
- 6.0–8.8s: the light shifts from gold toward warm white; the cascade keeps pouring, lit along its edges; the slider move eases to rest.
- 8.8–10.0s: hold: camera still, the clock at 06:52, only the cloud flowing.
For other lengths, stretch the blue hour and the sunrise, keeping one hour of clock per 10 s; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Each seek renders the terrain to its render target, then the cloud pass over it. Flow, light, sun angle and the clock are closed-form functions of t, passed to the shaders as uniforms.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the cloud top is level except where it spills, the cascade thins as it falls and is gone within about 300 m, shaded cloud is lilac-blue rather than grey, the first frame is already clearly readable, the peaks' shadows fall across the cloud after sunrise, nothing boils or bands, and average brightness never jumps by more than 3% between consecutive frames. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
