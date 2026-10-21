# MotionVault: Morph Slider

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L99) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L99)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called MorphSlider using React + Tailwind CSS + Framer Motion + lucide-react. Render a single 300×180px card centered in the preview (absolute inset-0 inside a fixed-size relative wrapper), each slide a muted low-saturation gradient (mist #E4EBF2→#D8E2EA, sand #F0EAE0→#E7E0D3, sage #E8EDE3→#DDE5D8, clay #F1E6DE→#E8DAD2, all 135deg) with a mono uppercase tag ("SLIDE · 01"), a 15px semibold zinc-800 title and a one-line 12px zinc-600 description. Track the slide index in useState and wrap the card in AnimatePresence with mode="popLayout" and initial={false}: on every switch the whole card morphs — exit to scale 0.9 / borderRadius 24px / opacity 0 while the incoming slide mounts from that exact morphed state and expands to scale 1 / borderRadius 16px / opacity 1, all over 450ms with cubic-bezier(0.22, 1, 0.36, 1), so the transition reads as the card itself deforming rather than two cards crossfading. Below the card render a control row: two 28px circular arrow buttons (ChevronLeft / ChevronRight from lucide-react, white bg, zinc-200 border, active:scale-95) flanking 4 indicator dots — the active dot stretches to a 16px-wide zinc-800 pill, inactive dots are 6px zinc-300 circles, morphing with a 300ms width transition; dots are clickable to jump directly. Wrap the index modulo the slide count for both directions.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
