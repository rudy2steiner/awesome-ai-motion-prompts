# MotionVault: Grid Expand

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L39) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L39)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called GridExpand using React + Tailwind CSS + Framer Motion. Render a 2×2 CSS grid (height 240px, max-width 520px, gap 12px) of cards, each a soft low-saturation gradient (sand #F0EAE0→#E7E0D3, sage #E8EDE3→#DDE5D8, sky #E4EBF2→#D8E2EA, clay #F1E6DE→#E8DAD2, all 135deg) with rounded-xl corners, a hairline border (black 5%) and a small mono label like "A · 01" (11px, zinc-500) anchored bottom-left. Wrap everything in a Framer Motion LayoutGroup and give each grid card a layoutId like grid-expand-{i}. When a card is clicked (index in useState), swap its grid cell for an empty placeholder div and mount an absolutely positioned overlay (inset 16px, z-10) with the SAME layoutId so it FLIP-morphs from the grid cell to fill the preview area over 500ms with ease-in-out cubic-bezier(0.42, 0, 0.58, 1); the unopened grid cards fade to 30% opacity. The expanded overlay reveals, with a 200ms delayed fade + 10px rise, the mono label, an 18px semibold title (zinc-800) and a 13px two-sentence description (zinc-600, line-height 1.7), plus a circular close button (28px, white/70 with backdrop-blur, hairline border, an X icon from lucide-react) at the top-right. Clicking the X — or anywhere on the expanded card — unmounts the overlay inside AnimatePresence so it morphs back into its grid cell.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
