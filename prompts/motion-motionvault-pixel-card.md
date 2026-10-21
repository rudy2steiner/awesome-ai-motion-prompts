# MotionVault: Pixel Surge

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L220) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L220)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PixelCard using React + Tailwind CSS + Canvas 2D. Render a white card (288×176px, rounded-xl, 1px zinc-200 border) with minimal content (mono uppercase label, title, two-line muted description). Overlay it with an absolutely positioned canvas (pointer-events-none, dimensions set via inline style, DPR-aware) divided into an 8px pixel grid (~36×22 cells). On pointerenter/pointermove track the cursor in card coordinates and run a requestAnimationFrame loop: each frame every cell computes phase = (t/1500ms + per-cell random seed*0.9 − distance-to-cursor/110) mod 1.1; cells with phase < 1 draw a zinc-900 square (inset 0.5px) whose opacity follows sin(phase × π) — a 0→1→0 pulse — so pixels ripple outward from the hovered point with random delays like a digital tide. Multiply by a global intensity that lerps toward 1 while hovering and 0 on leave; when intensity falls below 0.01 stop the rAF loop and clear the canvas. No React state in the pointer path — keep cursor position in refs.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
