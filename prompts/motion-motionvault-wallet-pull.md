# MotionVault: Wallet Pull

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L200) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L200)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called WalletPull using React + Tailwind CSS + Framer Motion. Render three bank cards (300×176px, rounded-xl, muted gradients — charcoal zinc-700→zinc-900, slate-400→slate-600, sand #CDBD9E→#A89472 — each with a tiny gradient chip graphic, mono card number, holder name, expiry and balance) stacked inside a wallet pocket (a wider rounded-2xl zinc-100 panel behind the bottom of the stack). Each card peeks 28px above the one in front of it: card i sits at y = 36 + (2 - i) * 28 with zIndex 10/20/30 so all three tops are visible and clickable. Track which card is out with a single useState (number | null) — only one card out at a time. Every card is a motion.div with initial={false} and a spring transition (stiffness 320, damping 26): clicking a peeking edge springs that card up to y 0 with scale 1.03 and zIndex 40, fully revealed, while the other cards sink 10px, scale to 0.97 and dim to 0.55 opacity; clicking the out card again (or another card) slots it back. The card's detail row (holder / expiry / balance) fades from 0.35 to full opacity only while the card is out.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
