---
title: "Code Editor Ghost Text Animation Prompt for Claude"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/code-editor-ghost-text"
license: "CC0"
collected: "2026-11-03"
---

# Code Editor Ghost Text Animation Prompt for Claude

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/code-editor-ghost-text](https://www.aicssanimations.com/directory/Motion-Prompts/code-editor-ghost-text)  
**License:** CC0

## Prompt

```
Make a 10-second code editor demo: ghost-text completions are accepted with Tab, the diff gutter marks the new lines, and the failing tests turn green.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Quoin, a code editor. Tagline: "Press Tab. Keep going."
- File tidepool/src/duration.ts, finished exactly as:
```ts
const UNITS: Record<string, number> = { h: 3600, m: 60, s: 1 };

// Turns "1h 30m" into seconds.
export function parseDuration(input: string): number {
  let total = 0;
  for (const [, n, unit] of input.matchAll(/(\d+)\s*([hms])/g)) {
    total += Number(n) * UNITS[unit];
  }
  return total;
}
```
- Tests: "1h 30m" → 5400; "45s" → 45; "1h 1m 1s" → 3661; "2 h" → 7200; "" → 0
- Accent: #C3A6FF. Length: 10 seconds
</inputs>

<direction>
Palette, an original dark theme: stage #0C0B11, editor #17161D, panels #121117, text #E6E3EE, line numbers #4D4A5C. Syntax: keywords #FF7EB6, functions #7CC4FF, types #C3A6FF, numbers #FFB26B, regex #F7D774, comments #6F6B80 italic. Ghost text #6E6A82 italic. Added and passing #4ADE9A, modified #6CA8FF, failing #FF6B6B.
Type: JetBrains Mono 400 and italic, 26px on 42px lines, no ligatures; chrome in Hanken Grotesk 500, 20–22px; the wordmark in 700, 64px.
Layout: a 1680×840 window at (120, 56): file tree, tabs ("duration.ts" unsaved), a gutter ending in a 4px diff column, a 250px test panel, a status bar. Below it, a keystroke HUD of 64px dark keycaps that sink 2px with an accent border when pressed.
Ghost text stays plainly a suggestion: dim italic, uncolored, its extra lines unnumbered, the code below sliding down to make room, a small "Tab Accept" chip above it. Accepting recolors it in a 160ms left-to-right sweep; numbers fade in and green diff bars grow down the new lines. Line 3 already has a blue modified bar. The caret blinks on a 1.06s period when idle; typing runs 9–14 characters a second.
Test panel: five rows (icon, name, input → expected), opening on the last run, all failed ("expected 5400, received undefined"). On re-run each icon spins, then draws a check, 180ms apart, and the summary flips "5 failed" → "5 passed · 38 ms".
Motion is crisp: 120–200ms on cubic-bezier(0.2, 0, 0, 1), with a 3% push across the piece.
Premium is an editor a developer would believe: code that compiles and passes, ghost text that stays a suggestion until Tab. Cheap is green code raining down a black screen.
Banned: a mouse cursor, code that wouldn't compile or pass, real editor or framework names, glow, glitch effects, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.8s: the window rises 20px and fades in: lines 1–4, the caret on an empty line 5, "}" on line 6; the panel reads 5 failed.
0.8–1.2s: "let" is typed.
1.2–1.6s: a pause, then the ghost text fades in: " total = 0;" and the three loop lines.
1.6–2.4s: hold so it can be read.
2.4s: Tab; accepted; bars grow on lines 5–8.
2.6–3.0s: Enter opens line 9; ghost "return total;" appears.
3.3s: Tab; line 9 gets its bar.
3.7–4.2s: ⌘S; the unsaved dot clears; "Saved" shows in the status bar.
4.2–6.0s: tests re-run; checks land from 4.6s; the summary flips at 5.6s.
6.0–7.4s: the HUD fades; the editor loses focus and the caret hides.
7.4–8.6s: "Quoin" and the tagline rise out of a mask below the window.
8.6–10.0s: hold, perfectly still.
For other lengths, keep typing and acceptance timing fixed and stretch the pauses and hold.
</structure>

<build>
One self-contained index.html, CSS and JS inline; Google Fonts via <link>, awaited with document.fonts.load() before window.seek is defined; no other libraries. Use HTML/CSS with inline SVG icons, laying code on a monospace grid. The stage is 1920×1080 (16:9), scaled to fit the window; design for 60fps. window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, randomness only from a seeded PRNG. Without ?render in the URL, drive seek from requestAnimationFrame (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text and anything off-style or Banned. Check the final code matches the input exactly, ghost lines carry no numbers or colors, diff bars sit only on lines 5–9 plus line 3, and no code runs under the panel. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
