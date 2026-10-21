# MotionVault: Stateful Button

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L182) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L182)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called StatefulButton using React + Tailwind CSS + Framer Motion (Aceternity Stateful Button). A dark zinc-950 pill (h-11, min-w 104px, rounded-lg, white text). On click run a phase machine idle → loading → done → idle: idle shows the label '部署'; loading (1.2s) swaps to an inline spinning ring (h-4 w-4, border-2 border-white/25 border-t-white, rotate 360 on a 0.8s linear infinite loop); done shows a drawn check (SVG path M 3 8.5 L 6.5 12 L 13 4.5 animated with pathLength 0→1 over 0.5s) plus '完成' for 1.5s, then resets. Swap phases with AnimatePresence mode popLayout (initial/exit opacity + y ±8 / scale 0.6, 0.18s) and put layout on the button with a spring (stiffness 500, damping 32) so its width stretches elastically to fit each content state. Disable the button while busy; store timeouts in a ref array and clear them all on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
