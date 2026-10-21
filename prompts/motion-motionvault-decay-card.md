# MotionVault: Pixel Decay

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L230) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L230)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DecayCard using React + Tailwind CSS + Canvas 2D. Render a card (320×200px, rounded-xl, 1px zinc-200 border, white bg) whose entire content is a single canvas (inline-style dimensions, DPR-aware). Pre-render the content into an offscreen canvas: dark zinc-900 face, a soft radial gradient orb with a 1px white/20 ring, a mono uppercase label, a semibold title and two skeleton bars. Slice the offscreen into 10px chunks (~32×20) tracked in Float32Arrays: offset x/y, velocity x/y, alpha and alpha-velocity. On pointermove, chunks within 64px of the cursor get kicked: a radial push (falloff 1 − d/64, magnitude 6–16px plus random jitter) and an alpha impulse (−0.25 to −0.7), so nearby pixels scatter and fade. Each frame integrate a spring back to origin (v += −offset×0.055, v ×= 0.88) and to full opacity (va += (1−a)×0.07, va ×= 0.82), drawing each chunk with drawImage at its displaced position and globalAlpha. When every chunk has settled (|offset| < 0.2, alpha > 0.995) stop the rAF loop and draw the pristine image — the card disintegrates under the cursor and elastically reassembles on release. No React state in the pointer path.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
