# Changelog Release Notes

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/changelog-release-notes) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/changelog-release-notes)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** product-brand
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second release-notes sequence in SVG: a changelog page steps up its version timeline from older releases to the newest, and as each entry settles into focus its tiny UI vignette plays a before-and-after, ending at the top of the page on the latest version.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Paperwing (fictional), a team wiki and docs tool. Page title: "Changelog". Header button: "Subscribe to updates".
- Entries, newest first (version · date · title · line · vignette before → after):
  4.8.0 · Oct 14, 2026 · "Resolve comments in one click" · "A check button on every thread. Resolved threads fold away." · a comment thread whose Resolve option hides in a ⋯ menu → a check button, and the thread folds into a "Resolved" chip.
  4.7.0 · Sep 30, 2026 · "Sort tables by any column" · "Click a header to sort. Click again to reverse." · a table with Budget 12k, 4k, 30k → sorted 30k, 12k, 4k with a down arrow on the header.
  4.6.2 · Sep 18, 2026 · "Search opens 4× faster" · "Results now appear while you type." · a search box with a spinner and "1.2 s" → three results and "0.3 s".
  4.6.0 · Sep 9, 2026 · "Page covers follow dark mode" · "Covers dim with your theme instead of glaring." · a bright white cover on a dark page → the cover dimmed to match.
  4.5.1 · Aug 27, 2026 · "@mentions suggest teammates" · "Type @ and pick from people on the page." · "@" alone → a list of three teammates.
  4.5.0 · Aug 12, 2026 · "Checklists remember who checked" · "Every checked item shows who and when." · a checked box → the same box with "AR · Aug 12".
- Page footer: "Older releases · 214 in total"
- Length: 10 seconds.
</inputs>

<direction>
- Look: an editorial changelog for people who actually read release notes. A dark, ink-green page, a serif for the story and a monospace for the facts, a thin vertical timeline with version nodes, and beside each entry a small framed vignette of the real UI change. The page moves in calm steps, stopping on each release just long enough to show its before and after.
- Palette: page #101512; vignette panels #171C18 with a 1px #2A322D border; UI surfaces inside the vignettes #1F2621 and #252D27; text #ECEFE8; secondary #A6AFA7; tertiary #6F7A72; timeline #2A322D; lime #B8F25B (the latest node, the "after" divider and tag, success states, the subscribe button); coral #FF8066 (the "before" tag and slow states); mention blue #7FC4FF (only in the @mention vignette); cover white #F4F3EE (the glaring cover).
- Type: Newsreader 500 for entry titles (40px) and the page title (96px); Newsreader 400 italic for entry lines (24px); Martian Mono 500 for versions (26px), 400 for dates (16px), and 500 11px uppercase with 0.12em tracking for the "BEFORE", "AFTER" and "LATEST" tags; inside the vignettes, Martian Mono 400 14px for UI text.
- The page, in page coordinates (the frame is a 1920×1080 window onto it): the header, y 0–320: an original mark at (120, 96), two overlapping triangles like a folded paper wing in #ECEFE8 and lime, and "Paperwing" in Newsreader 600 32px; "Changelog" on a baseline at (120, 230); at the right, the "Subscribe to updates" button (1.5px lime outline, Martian Mono 500 16px lime, 48px tall, right edge at x 1800, centered on y 200). Six entries, 280px tall each from y 320, newest first: entry k's top is 320 + 280 × (k − 1). The footer, y 2000–2240, its line centered on y 2080 in tertiary.
- Each entry, relative to its top y: the version right-aligned to x 330 on a baseline at y + 76, its date under it at y + 104 in tertiary; a 14px node on the timeline at (360, y + 68), outlined in tertiary for older entries and filled lime for 4.8.0, which also gets a "LATEST" tag in lime above its version; the title at (400, y + 80); the line at (400, y + 120), wrapped to 640px. The vignette panel at x 1140–1800, from y + 24 to y + 244 (660 × 220, radius 14). The timeline is a 2px line at x 360 from the first node to the last.
- Vignettes: each panel holds a small drawn UI (rects, text and paths at the 14px UI scale) in its before state, with a coral "BEFORE" tag at its top left. The change plays as a wipe: a 2px lime vertical divider sweeps left to right across the panel in 0.45 s on easeInOutCubic, revealing the after state behind it through a clip path, a lime "AFTER" tag riding the top of the divider and parking at the top left when it finishes while the "BEFORE" tag slides out ahead of it. Inside the after state, one small motion finishes the story within 0.3 s: the thread folds into its chip, the sort arrow rotates into place, the three results drop in 40 ms apart, the cover dims, the mention list unfolds, the "AR · Aug 12" avatar pops. Draw the arrows, the spinner and the ⋯ menu as paths, not glyphs.
- The scroll: the window's top edge in page coordinates, y_s, steps from 1320 (4.5.0 centered, 4.5.1 above it) up to 0 (the header at the top) through rests at 1320, 1040, 760, 480, 200 and 0. Each step is 0.35 s on easeInOutCubic and each rest 0.55 s. At each rest, the entry nearest the frame's center plays its vignette, oldest first; 4.8.0 plays at the final rest. Entries entering from the top edge fade from 0 to 100% over their first 120px in view.
- Focus: the entry playing is at full strength; the others sit at 55% opacity, easing between in 0.25 s. A 12px lime tick beside the timeline marks the focused node.
- Premium: a page worth reading, a strict grid, calm stepped scrolling with the content always aligned, vignettes drawn with real UI detail, wipes that make each change obvious in half a second. Cheap: a continuous blurry scroll, emoji bullets, party-popper "New!" badges, rainbow tags, confetti, neon version numbers, vignettes that are just colored boxes.
- Banned: emoji, confetti, glow, neon, gradients on text, motion blur, purple gradients on dark navy, real company names, logos and UI copied from existing products, anything flashing more than 3 times a second.
</direction>

<structure>
- 0.0–0.3s: the page fades up at y_s 1320: 4.5.0 centered and in focus, 4.5.1 above it, the footer below.
- 0.3–0.9s: 4.5.0's vignette plays (0.35–0.8 s).
- 0.9–1.8s: step to 4.5.1 (0.9–1.25 s); its vignette plays (1.3–1.75 s).
- 1.8–2.7s: step to 4.6.0; its vignette plays (2.2–2.65 s).
- 2.7–3.6s: step to 4.6.2; its vignette plays (3.1–3.55 s).
- 3.6–4.5s: step to 4.7.0; its vignette plays (4.0–4.45 s).
- 4.5–5.4s: the last step, to the top (4.5–4.85 s); 4.8.0's vignette plays (4.9–5.35 s).
- 5.4–5.8s: the 4.8.0 node fills lime from its center and "LATEST" types on.
- 6.0s: the hero frame: the header with "Changelog" and the subscribe button, 4.8.0 in focus in its after state, 4.7.0 below it in its after state, 4.6.2 cut by the bottom edge.
- 6.4–6.8s: the focus dimming lifts and every entry in view returns to full strength.
- 6.8–10.0s: hold.
For other lengths, change the rest time (0.45–0.8 s) and the hold; keep the 0.35 s steps, the 0.45 s wipes and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face, weight and style before defining window.seek.
- Engine: one inline SVG with viewBox 0 0 1920 1080; the page is a group translated by −y_s, which seek computes from the rest table. Each vignette is a group with its before state, its after state under a clipPath rectangle whose width follows the divider, and its tags; once a vignette has played it stays in its after state.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10) plus 0.6, 2.4 and 5.1: screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the page is always at a rest or mid-step, never drifting; each vignette plays while its entry is in focus, never off-screen; mid-wipe at 0.6 s the panel shows before on the right, after on the left and the lime divider between; every vignette reads as a real UI with legible 14px text; versions, dates and nodes line up on the timeline; dates run newest first. At 6.0 s the header, 4.8.0 with its lime node and "LATEST" tag, and 4.7.0 are fully readable. The final frame shows every entry in view at full strength. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
