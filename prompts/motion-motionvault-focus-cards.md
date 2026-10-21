# MotionVault: Focus Cards

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L304) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L304)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called FocusCards using React + Tailwind CSS + Framer Motion, recreating the Aceternity Focus Cards. Render three small cards (112×160px, rounded-xl, 1px zinc-200 border) in a horizontal row with 16px gaps; each card is a muted zinc gradient panel (light zinc-300 to darker zinc-500/600, all low-saturation) with a small white mono uppercase label and a short title. Track the hovered index in useState (null when none) on the row container's onPointerLeave / each card's onPointerEnter. Animate with Framer Motion's animate prop and a spring transition (type spring, stiffness 260, damping 22): the hovered card scales to 1.05 at full opacity with blur(0px); its siblings scale to 0.96, dim to opacity 0.5 and blur(4px) so they recede; with no hover all cards rest at scale 1, opacity 1, blur 0. Keep the row layout static (transforms only, no layout shift) and wrap the hover zone in a flex container so leaving the row resets every card together.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
