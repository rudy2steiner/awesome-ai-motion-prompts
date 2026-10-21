# MotionVault: Swipe Match

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L170) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L170)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SwipeCards using React + Tailwind CSS + Framer Motion. Render an infinite Tinder-style deck of profile cards (216×264px, rounded-xl, 1px zinc-200 border, soft shadow): each card has a soft gradient header (pastel duotone, 120px tall, with a frosted initials avatar) above a name line (15px semibold Chinese name + small mono uppercase tag) and two skeleton text lines. Keep a deck state (array of profile indices); only the front card is draggable — a motion.div with drag="x", dragMomentum false, and its x stored in a useMotionValue (no setState in the pointer path). Derive rotation from drag distance via useTransform (±220px → ±16deg), and two stamp opacities: a '喜欢' stamp (green-600, 3px border, mono bold, rotated -12deg, top-left) fading in as x passes +100px, and a '跳过' stamp (zinc-400, same style, rotated 12deg, top-right) fading in past -100px. On drag end: if |offset| exceeds 100px, tween x off-screen to ±460px (280ms, ease [0.16,1,0.3,1]) then rotate the deck so the swiped card cycles to the back; otherwise spring x back to 0 (stiffness 500, damping 32). The two cards behind sit at y 12/24px with scale 0.95/0.9 and opacity 1/0.6, stepping forward each cycle. Cards remount per cycle keyed by deck order so transitions stay smooth.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
