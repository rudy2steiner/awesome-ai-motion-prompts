# MotionVault: Electric Border

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L241) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L241)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ElectricBorder using React + Tailwind CSS + SVG filters. Render a dark card (288×176px, zinc-900, rounded-xl) on a zinc-950 backdrop with minimal white content (mono uppercase label, title, two-line muted description). Overlay an absolutely positioned SVG (viewBox matching the card, inset-0, pointer-events-none) containing three rects (2px inset, rx 12, fill none): a faint white/8 base outline, a crisp traveling arc (stroke zinc-200 #E4E4E7, strokeWidth 1.4, strokeLinecap round, pathLength 260, strokeDasharray "46 214"), and a blurred glow copy (stroke #F4F4F5, strokeWidth 3.5, 3px blur, same dash, opacity 0.55 → 1 on card hover via CSS transition). Wrap the arcs in a group with filter url(#eb-distort): feTurbulence (fractalNoise, numOctaves 2, seed 4, filter region −20%/140% so displacement is not clipped) whose baseFrequency is SMIL-animated between "0.012 0.05" and "0.02 0.085" over 5s, feeding an feDisplacementMap (scale 7) — the border warps like a live current. Animate stroke-dashoffset 0 → −260 in a 3.2s linear infinite CSS keyframes loop so the arc flows around the border; pause with animation-play-state when the card is off-screen (IntersectionObserver). Isolate the SVG in a memoized micro-component.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
