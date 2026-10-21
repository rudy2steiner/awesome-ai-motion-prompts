# MotionVault: Smoke Flow

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L200) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L200)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SmokeFlow using React + plain Canvas 2D (no extra libraries). A dark (zinc-950 #09090B) canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Spawn 380 motes advected by a smooth analytic flow field approximating curl noise: angle(x,y,t) = (sin(x*s*1.7 + t*0.31) + cos(y*s*2.3 - t*0.23) + sin((x+y)*s*0.9 + t*0.12) + cos((x-y)*s*1.3 - t*0.17)) * PI/2.2 with s = 0.0021 and t in seconds; each mote moves along the field at 0.35-1.1 px/frame. NEVER clearRect: each frame paint a translucent veil rgba(9,9,11,0.055) so motion leaves dissolving smoke trails. Draw each mote as a short round-capped line segment (1.1px) from its previous to current position in muted slate tones (148,163,184 / 113,125,150 / 100,116,139 / 203,213,225) at ~0.34 alpha scaled by a lifetime envelope (fade in over 40 frames, out over the last 60 of a 260-580 frame life), then respawn at a random position. While the pointer is inside, stir a local vortex: motes within 130px get a tangential push (2.4 px/frame with linear falloff). Repaint a solid #09090B base on resize. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
