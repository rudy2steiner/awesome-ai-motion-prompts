# MotionVault: Electric Arc

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L222) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L222)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ElectricArc using React + plain Canvas 2D (no extra libraries). A dark (zinc-950 #09090B) canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Two fixed electrodes (small 5px ring terminals, zinc-400) sit at 22% and 78% of the width, vertically centered. Between them grow lightning bolts via recursive midpoint displacement: start with the segment A->B, subdivide 6 times, offsetting each midpoint perpendicular to the segment by gaussian random * 0.28 * remaining segment length; keep the polyline (~65 points). Every 90-160ms retire the current bolt (fade it out over 140ms while a fresh one generates); while a bolt is alive, redraw it each frame with a per-frame jitter (regenerate with the same seed offset scaled down 30% at 12Hz) so it crackles. Render: outer stroke 3.5px rgba(125,211,252,0.18), core stroke 1.4px rgba(224,242,254,0.9), plus a soft glow dot at each electrode (radial gradient, sky-300, 0.35 alpha). With ~22% probability a bolt also spawns 1-2 branches from a random midpoint (same algorithm toward a random direction at 40% length, thinner, lower alpha). Pointer interaction: while the pointer is inside, electrode B tracks the smoothed cursor position (lerp 0.18) so the arc chases the fingertip; on pointerleave it eases back home. Pure rAF loop; clean up the loop, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
