# MotionVault: Ripple Circles

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L226) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L226)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called RippleCircles using React + Tailwind CSS + Framer Motion (Magic UI Ripple, click-triggered). The stage is an absolute inset-0 white container with cursor-pointer and role button. On pointerdown compute click coordinates via getBoundingClientRect and push a ripple {id, x, y} into state (cap at ~8 concurrent, slice off the oldest). Each ripple renders 3 thin concentric rings — motion.span h-24 w-24 rounded-full border border-zinc-400 positioned at left/top x/y — animating scale 0 → 3 with opacity 0.4 → 0 over 1.15s easeOut, staggered 150ms per ring (delay i*0.15). Center each ring with Framer Motion style x/y '-50%' (kept constant in both initial and animate) so centering never fights the scale. Prune the ripple from state in onAnimationComplete of the last ring. Rapid clicks stack freely. Add a centered pointer-events-none hint (zinc-900 title + mono 'CLICK TO RIPPLE' caption).
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
