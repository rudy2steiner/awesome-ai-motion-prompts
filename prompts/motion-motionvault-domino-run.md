# MotionVault: Domino Run

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L172) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L172)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DominoRun using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern (320px overflow-y viewport, thin custom scrollbar, progress hairline + fading scroll hint) with a 1000px track and a sticky 320px stage. Nine dominoes stand on a 1px zinc-200 baseline (bottom-16, px-4 stage): each is 14×64px, rounded-[3px], zinc-900 with a single white pip dot at center, spaced 30px apart starting at left 20px, z-index increasing left→right so each fallen domino lies on the next. Tipping: domino i maps scrollYProgress [0.05 + i·0.082, +0.075] → rotate 0 → 66° (transformOrigin '100% 100%', pivoting on its bottom-right edge), smoothed by useSpring (stiffness 420, damping 13) so it overshoots and wobbles as it slaps down; overlapping windows make the chain continuous. A live counter pill (top-left, mono uppercase, tabular-nums) reads 已倾倒 n / 9, derived via useMotionValueEvent (a domino counts fallen at 40% through its window; setState on change only). At the end of the run (62px past the last domino): a 36px circle button with a Bell icon — past progress 0.82 it turns amber (amber-50 bg, amber-500 icon) and swings rotate keyframes [-22,15,-9,5,0] over 900ms pivoting from its top, two expanding amber sound-ripple rings (scale 0.5→1.9 fade, 180ms apart), and a '叮!' zinc-950 pill pops above it with a spring. Scrolling back below 0.5 resets the bell. Bottom-left phase chip: 滚动 · 推倒第一块 → 连锁反应进行中… → 势不可挡 → 全部倒下 — 铃声为证.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
