# MotionVault: Depth Carousel

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L89) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L89)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DepthCarousel using React + Tailwind CSS + Framer Motion. Render 4 abstract cards (280px wide, 170px tall, rounded-xl, hairline zinc-950/10 border, soft shadow, muted low-saturation gradient faces — mist #E4EBF2→#D8E2EA, sand #F0EAE0→#E7E0D3, sage #E8EDE3→#DDE5D8, clay #F1E6DE→#E8DAD2, each with a mono uppercase tag like "FRAME · 01", a semibold title and two rounded skeleton bars) absolutely stacked in a 280×210px relative wrapper, queued along the z axis: front slot y 0 / scale 1 / opacity 1, then y 16 / scale 0.93 / opacity 0.8, y 32 / scale 0.89 / opacity 0.62, and the rearmost y 48 / scale 0.85 / opacity 0.45, zIndex decreasing with depth. Drive the queue with an order array in useState. A pill button below the stack reads "下一张 →" (mono 11px, white bg, zinc-200 border, rounded-full). On click, render the front card as a separate flying element animating from its rest pose to x -230 / y -90 / rotate -14deg / opacity 0 / scale 0.96 over 420ms ease-in, while the order array rotates (front id moved to the back) so the remaining cards spring forward through their slots with a spring of stiffness 220 and damping 20; after ~420ms clear the flying state so the card remounts at the very back fading in from opacity 0 — an endless loop. Ignore clicks while a card is mid-flight. Transform and opacity only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
