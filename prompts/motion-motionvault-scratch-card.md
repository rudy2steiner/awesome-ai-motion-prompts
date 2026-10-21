# MotionVault: Scratch Card

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L210) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L210)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ScratchCard using React + Tailwind CSS + Canvas 2D. Render a prize card (320×200px, rounded-xl, 1px zinc-200 border) whose prize layer (warm amber-to-rose gradient, small mono uppercase 'YOU WIN' label, big bold '再来一瓶 🎉', and a mono serial line) sits under a scratch-off foil. Implement the foil as an absolutely positioned canvas (dimensions set via inline style, DPR-aware): paint a zinc metallic linear-gradient (#d4d4d8 → #e4e4e7 → #f4f4f5 → #d4d4d8 → #a1a1aa), sprinkle ~1400 1px noise specks, and draw a centered '刮 开 惊 喜' hint plus 'SCRATCH HERE' in mono. On pointerdown capture the pointer and start erasing: set globalCompositeOperation to 'destination-out' and fill 28px-radius circles at the pointer; on pointermove interpolate circles along the drag segment (step = radius/2) so fast strokes erase continuously. Track progress with a coarse 24×15 boolean grid whose cells within the erase circle get marked; when over 45% of cells are scratched, set state once to fade the whole canvas to opacity 0 (700ms CSS transition) and disable pointer events. Show a small '再来一次' reset button (RotateCcw icon, mono uppercase, frosted white) once finished, which repaints the foil and re-arms scratching. No setState in the pointermove path besides the one-time completion flag.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
