# MotionVault: Magnet Lines

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L107) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L107)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called MagnetLines using React + Tailwind CSS + Framer Motion, running entirely on MotionValues (zero setState). Render a 9×5 grid (gap 30px, fixed pixel size ~270×150) of short 12px lines (h-[2px], rounded-full, zinc-400). onPointerMove on the grid wrapper writes pointer coords (relative to the wrapper rect) into mx/my MotionValues and sets an 'active' MotionValue to 1; onPointerLeave sets active to 0. Each line is a child component receiving mx/my/active plus its cell center (cx, cy): compute the target angle with useTransform([mx, my, active]) — atan2(y-cy, x-cx) in degrees while active, 0 when idle — then smooth it through useSpring(angle, { stiffness: 180, damping: 16 }) bound to the line's rotate style, so lines swivel toward the cursor and ease back upright on leave. Distance effects come from a second useTransform producing the pointer distance (9999 when idle): scaleX = useTransform(dist, [40, 220], [1.7, 1]) softened by another spring (stiffness 200, damping 20), and backgroundColor = useTransform(dist, [40, 220], ['#09090B', '#A1A1AA']) so nearby lines stretch longer and darken to zinc-950. Position each line absolutely at its cell center, cursor-crosshair on the wrapper, light background, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
