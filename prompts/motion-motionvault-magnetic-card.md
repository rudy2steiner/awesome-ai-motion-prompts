# MotionVault: Magnetic

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L71) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L71)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React magnetic card with Framer Motion: while the cursor is inside
the container, translate the card toward the cursor with distance-based
falloff (max 24px) using useMotionValue + useSpring (stiffness 200,
damping 18). On mouse leave, spring back to origin with a satisfying
overshoot. Apply the same magnetic effect at 0.5x strength to the card's
inner content for parallax depth.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
