# MotionVault: Infinite Moving Cards

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L119) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L119)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called InfiniteMoving using React + Tailwind CSS + Framer Motion, recreating the Aceternity "Infinite Moving Cards". Render 6 abstract cards (200×130px, rounded-xl, hairline zinc-950/10 border, soft shadow, muted low-saturation gradients — mist/sand/sage/clay/ink/dawn variants — each with a mono uppercase tag like "TAPE · 01", a 13px semibold title and one skeleton bar) on a horizontal flex track with 16px gaps, duplicated once so two identical copies sit back to back (one copy = 6 × 216px = 1296px wide). Drive the loop with Framer Motion's useAnimationFrame on an x MotionValue: advance x leftward at 1296px per 30s (≈43.2px/s... i.e. COPY_W / 30000 px per ms × delta), and when x passes -COPY_W add COPY_W back so the tape wraps seamlessly — never use setState in the frame loop. Keep a speed factor in a ref that eases (lerp 0.06 per frame) toward 0.2 while the wrapper is hovered and back to 1 on leave, multiplying the per-frame delta so the tape smoothly decelerates to a crawl instead of snapping. Gate the frame loop with an IntersectionObserver in-view flag. Overlay both ends with pointer-events-none gradient masks (64px wide, from the preview background #FAFAFA to transparent) so cards fade in and out at the edges. Isolate the perpetual animation in a React.memo'd micro-component so parent re-renders never reset it.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
