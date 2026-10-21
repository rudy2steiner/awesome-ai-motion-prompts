# MotionVault: Skeleton

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L78) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L78)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SkeletonCard using React + Tailwind CSS + Framer Motion. A mock content card (~256px wide, white bg, 1px zinc-200 border, rounded-xl, p-4, overflow-hidden) rendered as skeleton shapes: a 40px avatar circle, two text bars beside it, one full-width text bar, and a 96px image block — all zinc-200 with rounded corners. A shimmer band (a half-width absolutely positioned motion.div with background linear-gradient(100deg, transparent, rgba(255,255,255,0.75), transparent)) sweeps left → right across the whole card (translateX -160% → 320%, 1.6s, linear, infinite). After 4s, crossfade to the real content (a black avatar with initials, a name line, a caption line and a black image block with a small white wave SVG) for 1.5s, then back to the skeleton — looping forever to show the before/after. Drive the 4s/1.5s timer with useEffect + setTimeout gated by an IntersectionObserver in-view flag so it only runs while visible, and reset to skeleton when scrolled out. Respect prefers-reduced-motion by disabling the shimmer band.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
