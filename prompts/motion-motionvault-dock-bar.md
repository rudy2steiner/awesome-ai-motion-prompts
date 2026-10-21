# MotionVault: Dock Magnification

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L79) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L79)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DockBar using React + Tailwind CSS + Framer Motion + lucide-react, recreating the macOS dock magnification. Render a frosted bar (white/75, backdrop-blur, 1px zinc-200 border, rounded-2xl, soft shadow, px-4 py-3, gap-3) bottom-centered in the preview (items-end, pb-12), holding 7 icon tiles (Home, Search, Compass, Music, Camera, Mail, Settings from lucide-react, white zinc-100 strokes at 50% size) on muted zinc gradient tiles (e.g. zinc-600→zinc-800, zinc-500→zinc-600, zinc-700→zinc-900 variants, rounded-xl, soft inner shadow). Keep a single mouseX useMotionValue on the bar: set it to e.clientX on pointermove and to Infinity on pointerleave — never useState in the pointer path. Each icon is a memoizable child holding a ref to its div: derive distance = useTransform(mouseX, x => x − rect.x − rect.width/2) measured live from getBoundingClientRect, then size = useSpring(useTransform(distance, [−110, 0, 110], [48, 72, 48]), { mass: 0.1, stiffness: 170, damping: 13 }), bound to width/height via style. Because the bar uses items-end alignment, magnified icons grow upward and lift off the baseline automatically — smooth 60fps magnification that ripples to neighbors by distance.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
