# MotionVault: Share Expand

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L222) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L222)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ShareExpand using React + Tailwind CSS + Framer Motion + lucide-react. A single spring (type spring, stiffness 500, damping 25) drives everything. Collapsed: a dark zinc-950 pill (h-11, rounded-full) with a Share2 icon and the label '分享'. On click the wrapper (motion.div with layout, overflow-hidden, h-11 rounded-full) morphs elastically into an open tray — bg-zinc-100 with a 1px zinc-200 border and p-1 — containing four channel icon buttons (Link2, Send, MessageCircle, Mail; h-9 w-9 rounded-full, zinc-600 icons, hover bg-white) that pop in with scale 0→1 + opacity on a 60ms stagger, followed by a trailing X close button at 4×60ms. Swap the two states with AnimatePresence mode popLayout; clicking any icon or the X springs the pill back closed. Keep the whole interaction keyboard-focusable with aria-labels on icon buttons.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
