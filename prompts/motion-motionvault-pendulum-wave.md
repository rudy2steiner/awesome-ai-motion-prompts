# MotionVault: Pendulum Wave

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L106) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L106)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PendulumWave using React + plain Canvas 2D (no extra libraries). A dark (zinc-950) canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Draw 15 white glowing dots (3.2px radius, shadowBlur 8) in a horizontal row with 30px side padding, each oscillating vertically around the canvas midline with amplitude height/2 - 40. Dot i has period T_i = 60 / (51 + i) seconds, so over each 60-second cycle the row weaves through snake, double-helix and chaos patterns before returning to perfect unison. Connect the dots with a hairline polyline (rgba(255,255,255,0.22)) to reveal the emerging wave. Instead of clearing, fade the previous frame each tick with a translucent rect (rgba(9,9,11,0.08)) so the dots leave smooth motion trails; repaint a solid #09090B base on resize. Drive phases from performance.now() elapsed time. Clean up requestAnimationFrame and the ResizeObserver on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
