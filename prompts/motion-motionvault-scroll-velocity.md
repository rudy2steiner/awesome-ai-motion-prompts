# MotionVault: Scroll Velocity

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L72) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L72)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ScrollVelocity using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern: a 320px overflow-y auto viewport (overscroll-contain, thin custom scrollbar — never hijack page scroll) containing a 1000px track with a sticky full-viewport white panel. Inside the panel render a big-type marquee: a w-max flex strip holding TWO identical copies of the phrase '滚动越快 · 我越快 · ' repeated 4× at 28px font-semibold tracking-tight, alternating solid zinc-950 and zinc-300 spans. Drive it with a baseX MotionValue advanced in useAnimationFrame at a constant 0.0125 percent/ms, wrapped into [-50%, 0%) via a local wrap helper so the two copies loop seamlessly. Multiply the frame step by a velocity boost: useVelocity(useScroll({ container }).scrollYProgress) → useSpring({ damping: 50, stiffness: 400 }) → useTransform(v => 1 + min(|v| * 6, 14)), so flicking the scroller instantly accelerates the marquee up to 15× and it springs back to cruise speed when you stop. Also derive skewX from the smoothed velocity over [-2, 0, 2] → [-8deg, 0, 8deg] (clamp) and a small velocity meter bar (w-16 h-0.5 zinc-200 track, zinc-950 fill scaleX = min(|v|/1.5, 1), origin-left) in the top-right corner next to a mono uppercase 'SCROLL VELOCITY' label. Add a bottom caption '在容器内快速滑动 —— 我会跟着加速并倾斜', the sticky top progress hairline and the fading "向下滚动" hint pill. Transform/opacity only, 60fps.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
