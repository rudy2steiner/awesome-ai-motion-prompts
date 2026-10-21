# MotionVault: Ring Progress

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L40) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L40)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** explainers-data
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called RingProgress using React + Tailwind CSS + Framer Motion. It renders a 160x160 SVG containing: a ring of 24 subtle tick marks (1px zinc-300 lines at radius 60-66, every 15deg, every 6th tick slightly longer), a track circle (radius 52, 6px stroke, zinc-200, no fill), and a progress arc — a motion.circle with the same radius, 6px zinc-950 stroke, round line cap, rotated -90deg around the center, animating pathLength 0 to 0.78 over 1.6s ease-out on mount. In the center, absolutely positioned, a mono-font number counts 0% to 78% in sync: drive a useMotionValue with animate() using a spring (stiffness 60, damping 16), round it via useTransform, and render it as the text content of a motion.span. Stop the animation controls on unmount. Light background, monochrome zinc only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
