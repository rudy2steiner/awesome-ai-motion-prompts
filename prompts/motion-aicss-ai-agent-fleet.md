---
title: "AI Agent Fleet Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/ai-agent-fleet"
license: "CC0"
collected: "2026-11-03"
---

# AI Agent Fleet Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/ai-agent-fleet](https://www.aicssanimations.com/directory/Motion-Prompts/ai-agent-fleet)  
**License:** CC0

## Prompt

```
Make a 10-second product film of an AI coding-agent fleet: two dozen agent panes write code in parallel, tasks flow from a queue to the agents along drawn routes, finished results flow out into a merge lane, and everything lands in a single green build.

<inputs>
If I don't give you something, use the default and don't ask.
- Orchestrator: Tandemloom (fictional).
- Repository and branch: harborline/api (fictional) · release/4.2
- Goal: "Migrate 48 endpoints to the v2 schema"
- Fleet: 24 agents, A-01 to A-24, two tasks each.
- Tasks: #001 to #048, each "Migrate /<route> to v2", routes drawn from: orders, invoices, refunds, customers, carts, shipments, coupons, payouts, reviews, wishlists, returns, taxes (repeat with suffixes like /orders/items).
- Retry: A-17's second task (#041) fails 2 tests, fixes them and passes.
- Results: 48 pull requests merged, +4,112 −3,086 lines in all; Build #1187: lint, types, tests, bundle; 3,214 tests passed, 0 failed.
- Fleet clock: 00:00:00 to 00:41:08.
- Final line: "48 tasks · 24 agents · one green build"
- Length: 10 seconds.
</inputs>

<direction>
- Look: an orchestration dashboard in a calm, light editorial style: a wall of 24 live agent panes streaming real-looking code and test output, a task queue that drains into them along drawn routes, results that flow out into a merge lane and down into one build card, which turns green. Busy but orderly: everything on a grid, every motion meaning something.
- Palette, light rather than green-on-black: background warm paper #EEE9DF with a 24px dot grid #D9D2C4; panes white #FFFFFF with a 1px #D6CFC1 border, 10px radius and a header strip #F6F2EA; code ink #24272E with keywords ultramarine #3346D3, strings terracotta #C25A34, comments #8C8578, types plum #8A3F93, numbers teal #127C86; status: queued slate #8C93A3, working ultramarine #3346D3, reviewing amber #D99A1E, failed rose #E04B5A, passed green #1F9D55; routes ink #24272E at 30%; build card ink #1C1F26 that fills green #1F9D55; text ink #1C1F26, secondary #6B6658. Green appears only for passes and the build, so the final green is earned.
- Layout on the 1920 × 1080 stage:
  - header: kicker "TANDEMLOOM · ORCHESTRATOR" in Instrument Sans 700, 20px, tracked 0.14em, ultramarine, at (120, 78); the goal in Instrument Sans 700, 48px, ink, on baseline 142; at the right, right-aligned at x 1800, "harborline/api · release/4.2" in Azeret Mono 500, 22px, secondary, and the fleet clock in Azeret Mono 600, 28px, ink;
  - queue, x 120–400, y 190–1000: "Queue 48" in Instrument Sans 700, 24px, then task cards 280 × 40 at 48px pitch, each "#014 /orders → v2" in Azeret Mono 500, 20px, with a slate status dot;
  - pane wall, x 460–1456, y 190–1002: 6 columns × 4 rows of panes 156 × 194 with 12px gutters, A-01 at the top left;
  - merge lane, x 1520–1800, y 190–760: "Merged 0/48" in Instrument Sans 700, 24px, then PR chips 280 × 36 stacking downward, each "PR #2231 · +84 −61" in Azeret Mono 500, 20px, with the additions in green and the deletions in rose; past twelve chips the oldest compress into a stacked "+36 more" card;
  - build card, x 1520–1800, y 800–1000: "Build #1187" in Instrument Sans 700, 26px; four stage ticks "lint · types · tests · bundle" in Azeret Mono 500, 20px; a 248px progress bar; the result line.
- An agent pane: a 30px header strip with the agent id ("A-07", Azeret Mono 600, 20px) at the left, its task number at the right, and a 4px status bar along its left edge in the status color; a body of 12 code lines in Azeret Mono 400 at 10px (13px leading), typing at 40 characters per second per pane with a 1 Hz block caret and scrolling up a line when full, syntax-colored, drawn from about 60 seeded TypeScript-like lines (imports, handler signatures, schema parsing, database queries, a v2 comment, test assertions such as `expect(res.status).toBe(200)`); a 30px footer with a thin progress bar and a test readout in Azeret Mono 500, 20px ("✓ 64" in green, or "✗ 2" in rose). The 10px code is texture in the wide view and readable at the opening zoom.
- Flow:
  - dispatch: a task card leaves the queue as a 64 × 28 chip ("#014", Azeret Mono 500, 20px, white on ultramarine), travels at up to 1,600px/s (eased at both ends) along its route, shrinking to a 10px ultramarine dot where the route enters the 12px gutters, and grows back into the chip as it docks into its pane's header; the pane's status bar turns ultramarine and its typing starts; the queue scrolls up and its count drops;
  - routes: orthogonal paths with 8px corner radii, drawn as 1.5px lines a moment before each chip travels them and fading after: from the queue into a vertical trunk in the gap at x 430, along the row gutters to the pane's column, then into the pane's top edge. Result routes leave each pane's right edge along the row gutters to a trunk at x 1488 and up into the merge lane. Routes run only in gutters, never over a pane;
  - finish: when a task completes, its pane turns amber for 0.3 s (review), then green with a check; a PR chip leaves the pane's right edge as a 10px green dot along its result route, grows into its chip at the trunk and lands at the bottom of the merge lane with a 1.1 to 1 pop; the merged count rolls; the pane takes its next task at once;
  - the retry: A-17's second task turns rose at 5.7 s with "✗ 2 failing: orders.spec.ts" in its footer and two rose lines in its code (a failing assertion); a small circular retry arrow turns once; it types a fix and passes at 6.9 s;
  - the build: when all 48 are merged, the merge lane's chips compress upward into one bar that slides down into the build card; the stages tick on one by one with a check each, the bar fills, and the card fills green with "3,214 passed · 0 failed" in Azeret Mono 600, 22px, white.
- Schedule: tasks #001–#024 dispatch 1.0–2.0 s, 40 ms apart; each task's duration is seeded between 2.2 and 3.4 s, so first finishes arrive from about 3.4 s and second-wave tasks #025–#048 dispatch as panes free up; the last result merges by 7.3 s. Seed the 48 PR sizes so they total exactly +4,112 and −3,086 (draw 47, set the 48th to the remainder within range).
- Fleet clock: maps t onto fleet time through a smooth monotonic curve, 00:00:00 at 0.8 s to 00:41:08 at 8.3 s, ticking seconds, never running backwards.
- Camera: a CSS transform on the dashboard: it opens at 2.6× on pane A-01 (its code readable at about 26px, the first chip arriving), then pulls back to 1.0× by 2.4 s on cubic-bezier(0.45, 0, 0.2, 1); still after that.
- Motion: panels rise 12px and fade over 0.4 s on cubic-bezier(0.22, 1, 0.36, 1); chips pop on a damped spring (ratio 0.6); numbers roll like an odometer over 0.3 s.
- Premium: code that looks like code, with syntax color and believable rhythm, routes that carry real tasks from queue to agent to merge, one honest failure and retry, numbers that add up, a single green that lands last. Cheap: falling green characters on black, glowing robot icons, random blinking boxes, a progress bar with nothing behind it.
Banned: real AI products, companies, model names, logos or editor chrome; robot, brain or sparkle icons; falling-character rain; dark mode; neon glow; routes crossing over panes; any element blinking faster than 1 Hz; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: close on pane A-01 at 2.6×: an empty editor; the header and queue fade in around it.
- 1.0–2.4s: dispatch: the first chip docks into A-01 and it starts typing, readable; the camera pulls back as chips stream along their routes into all 24 panes, 40 ms apart; the queue scrolls down to 24.
- 2.4–3.4s: the whole wall types at once; footers fill; the fleet clock runs.
- 3.4–5.6s: finishes ripple across the wall: amber, green, PR chips flowing into the merge lane; second-wave chips dispatch; the queue empties at about 4.8 s.
- 5.6–6.0s: A-17 turns rose with its failing tests. At 6.0 s: every pane busy, one rose pane, the merge lane half full, the queue empty: a complete composition.
- 6.0–7.3s: A-17 retries and passes (6.9 s); the last results land; "Merged 48/48" and "+4,112 −3,086".
- 7.3–8.3s: the merge lane funnels into the build card; lint, types, tests and bundle tick at 7.5, 7.7, 7.9 and 8.1 s; the card turns green at 8.3 s with "3,214 passed · 0 failed"; the clock stops at 00:41:08.
- 8.3–8.7s: the wall eases to 60% with a green check in every pane; the goal line changes to the final line.
- 8.7–10.0s: hold: only the carets blink.
For other lengths, add or remove tasks per agent; keep the retry, the build beat and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: HTML/CSS: absolutely positioned elements whose transforms, sizes, text and opacity are set from seek, with inline SVG for routes, checks, dots and the retry arrow; no canvas and no other libraries.
- The whole schedule (dispatch, durations, finishes, routes, PR sizes, code lines per pane) is generated once at load from a seeded PRNG; each seek derives every pane's status, its typed text (characters = 40 × time since the task started, wrapped and scrolled), every chip's position along its route and every count from t alone.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check there are exactly 24 panes and 48 tasks, every chip travels a route from the queue to a pane or from a pane to the merge lane and routes stay in the gutters; counts agree (queue + in progress + merged = 48 at every frame); A-17 fails and retries exactly once; the PR totals read +4,112 −3,086; the build turns green only after the 48th merge; header, queue, chips, footers and build text are at least 20px and readable; the 6.0 s and final frames are complete compositions. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
