# MotionVault: Particle Text

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L50) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L50)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React particle-text component on Canvas 2D. Render a word
(e.g. "MOTION", 120px bold) to an offscreen canvas, sample pixels to get
~1500 target points. Particles start at random positions and spring toward
their targets (attraction 0.06, damping 0.86). Within 60px of the cursor,
apply a repulsion force (up to 8, distance-falloff) so particles scatter,
then spring back. White 1.2px dots on a dark background. rAF loop, pause
offscreen, rebuild on resize.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
