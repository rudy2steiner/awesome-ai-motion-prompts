# MotionVault: Scroll Stack

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L100) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L100)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React stacking-cards effect inside a scrollable container (320px,
overflow-y scroll). Four cards are position sticky at top 16px; as scroll
progress pushes a new card up, the covered card scales to 0.94 and dims to
brightness 0.96. Drive progress with GSAP ScrollTrigger using the container
as scroller (or a scroll handler + math). Each card: white, 1px border,
rounded-12, numbered 01-04.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
