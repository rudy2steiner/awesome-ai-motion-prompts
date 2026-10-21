# MotionVault: Confetti Burst

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L67) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L67)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React confetti-burst component on Canvas 2D: on click, explode
80-120 confetti pieces from the click point — colored rectangles (palette
#F43F5E #F59E0B #10B981 #3B82F6 #8B5CF6) plus round dots — with an upward
fan of initial velocities (3-9 px/frame, ±50deg), gravity 0.15, air drag
0.98. Rectangles tumble by oscillating scaleX (fake 3D flip). Fade out
before landing and clear the canvas after ~1.2s. Expose an onCelebrate
callback. No external libraries.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
