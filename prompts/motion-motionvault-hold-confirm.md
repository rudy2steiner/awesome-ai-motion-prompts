# MotionVault: Hold To Confirm

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L152) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L152)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React HoldConfirm button (danger-action pattern) using React + Tailwind CSS + Framer Motion. An outlined button (1px rose-600 border, rose-600 text, Trash2 icon + label '长按删除', w-40 h-11, rounded-lg, select-none). On pointerdown, a translucent rose fill (bg-rose-600/15, origin-left, transform scaleX bound to a MotionValue) sweeps left → right across the button over 1.2s, linear — progress MUST be driven by requestAnimationFrame, not a CSS animation, so early release works. Completing the hold flips the button to filled rose-600 with white text, a Check icon and '已删除' (spring scale pop), then it resets to idle after 1.5s. Releasing early (pointerup or pointerleave) cancels the hold and drains the fill back to 0 over 200ms — no partial credit. Cancel the rAF loop and timers on unmount, prevent the context menu, and use touch-action none so mobile holds aren't interrupted. Center on a light preview.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
