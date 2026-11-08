# API Request and Response

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/api-request-response](https://www.aicssanimations.com/directory/Motion-Prompts/api-request-response)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second API demo in the style of a polished docs page: one request shown in curl, JavaScript and Python tabs, a cursor sends it, a 200 OK lands in 184 ms and the JSON response streams in, then the shipping label it created slides out.

<inputs>
If I don't give you something, use the default and don't ask.
- Company: Larkpost (fictional), a shipping label API. Wordmark "larkpost" beside an original mark: two overlapping triangles forming a small folded-paper dart.
- Eyebrow: "LARKPOST API · V2". Headline: "Create a shipping label in one request."
- Endpoint: POST /v2/labels on https://api.larkpost.dev.
- cURL tab, exactly:
  curl https://api.larkpost.dev/v2/labels \
    -H "Authorization: Bearer lp_test_4f9a…c21e" \
    -H "Content-Type: application/json" \
    -d '{
      "from":   { "zip": "94107", "country": "US" },
      "to":     { "zip": "10013", "country": "US" },
      "parcel": { "weight_oz": 22, "length_in": 10,
                  "width_in": 8, "height_in": 4 },
      "service": "ground_saver"
    }'
- JavaScript tab, exactly:
  import Larkpost from "@larkpost/node";

  const lark = new Larkpost(process.env.LARKPOST_KEY);

  const label = await lark.labels.create({
    from:   { zip: "94107", country: "US" },
    to:     { zip: "10013", country: "US" },
    parcel: { weightOz: 22, lengthIn: 10,
              widthIn: 8, heightIn: 4 },
    service: "ground_saver",
  });

  console.log(label.trackingNumber);
- Python tab, exactly:
  import os
  import larkpost

  lark = larkpost.Client(os.environ["LARKPOST_KEY"])

  label = lark.labels.create(
      from_={"zip": "94107", "country": "US"},
      to={"zip": "10013", "country": "US"},
      parcel={"weight_oz": 22, "length_in": 10,
              "width_in": 8, "height_in": 4},
      service="ground_saver",
  )

  print(label.tracking_number)
- Install line per tab: "No SDK needed" for cURL, "npm i @larkpost/node" for JavaScript, "pip install larkpost" for Python.
- Response: status "200 OK", time "184 ms", body exactly:
  {
    "id": "lbl_8Hq2mZ4rT1",
    "object": "label",
    "status": "purchased",
    "service": "ground_saver",
    "rate": {
      "amount": 7.42,
      "currency": "USD"
    },
    "parcel_weight_oz": 22,
    "estimated_delivery": "2026-10-22",
    "tracking_number": "LP773044219083",
    "label_url": "https://files.larkpost.dev/8Hq2mZ4rT1.pdf",
    "livemode": false,
    "created": 1792411532
  }
- The label: service "GROUND SAVER"; from "JUNIPER & MOSS · 600 BRANNAN ST · SAN FRANCISCO CA 94107"; to "PRIYA RAMAN" / "48 LISPENARD ST" / "NEW YORK NY 10013"; tracking "LP 7730 4421 9083"; footer "22 OZ · 10 × 8 × 4 IN · USD 7.42 · SHIP 2026-10-19".
- Closing line: "Get a test key · 500 free labels a month".
- Length: 10 seconds.
</inputs>

<direction>
- Look: a quiet, well-set docs page filmed straight on. The request lives on light paper and the response on a dark ink panel, so the eye reads question, then answer. Motion is quick and mechanical, like a good editor: things snap into place, nothing floats.
- Palette: page #FBF8F3; request card #FFFFFF with a 1px #E7E1D6 border; ink #1E1C19; muted #77706A; rules #EDE7DC; line numbers #C9C1B4; brand brick #B8432F for the active tab, the Send button, the POST chip and click rings, with #F6E3DE as its tint. Light syntax: property names #2F5F8A, strings #A0441B, numbers #8A6A00, keywords, the curl command and its flags #B8432F, punctuation #8B8479. Response panel #1F1D1A, its header #2A2724, rules #3A3632; dark syntax: keys #E9D8C2, strings #9FD3B0, numbers and booleans #F2B880, punctuation #8F877C; status pill fill #1E3A29 with text #8FE0A9. The label is black #111111 on white #FFFFFF. No gradients anywhere.
- Type: Source Sans 3 600 for the headline at 56px (tracking −0.01em); Source Sans 3 500 16px for tabs; Source Sans 3 600 15px for buttons; Source Code Pro 400 20px on a 34px line for all code; Source Code Pro 500 13px tracked 0.12em for the eyebrow and panel labels; Source Code Pro 500 15px for the install line.
- Layout:
  - Eyebrow at x 120, baseline y 104, in brick; headline at x 120, baseline y 176, on one line.
  - Request card x 120–940, y 250–950, radius 14, shadows 0 1px 0 #E7E1D6 and 0 24px 48px rgba(60,40,20,0.08). Its top bar y 250–314 holds the tabs "cURL", "JavaScript" and "Python" from x 152 with 32px between them (inactive in muted, active in ink with a 2px brick underline 10px below the baseline that slides and resizes between tabs), and the Send button at x 812–916, y 266–298 (radius 8, brick fill, white "Send"). A 1px rule at y 314. A method line at baseline y 352: a "POST" chip (brick text on the tint, Source Code Pro 500 14px, radius 6) and "/v2/labels" in Source Code Pro 400 17px ink. Code from baseline y 412: line numbers right-aligned at x 172, code from x 196, never more than 57 characters a line (Python, the longest tab, ends at baseline y 854). The install line at x 152, baseline y 912, in muted, with a small copy glyph at x 900.
  - Response panel x 980–1800, y 250–950, radius 14. Header y 250–314: "RESPONSE" at x 1012; at the right the status pill (x 1584–1680, "200 OK" in Source Code Pro 500 15px, radius 13) and "184 ms" in muted mono at x 1700. Before the request the header reads "Waiting for request" in #8F877C. JSON from x 1012, first baseline y 372, 16 lines at 34px (the last at y 882); the longest line is 60 characters and must end before x 1772.
  - The cursor: a crisp black arrow with a 1.5px white outline, 26px tall, drawn in SVG.
- Tab switch: the underline slides to the new tab and takes its width (easeInOutCubic 0.3 s); the outgoing code fades out in 0.12 s; the incoming lines rise 6px and fade in, 18 ms apart; the card never changes size. The install line crossfades with the code.
- Sending: the Send button presses (scale 0.96 for 0.1 s) and a brick click ring expands once (0 → 28px, fading over 0.3 s); a 2px brick progress line runs along the bottom edge of the response header from left to right over 0.2 s; the header reads "Sending" with three dots appearing one at a time, 0.06 s apart. Then the pill scales in from 0.85 (easeOutBack, 0.35 s) and "184 ms" counts up from 0 over 0.25 s.
- Streaming: the JSON appears character by character at 420 characters per second, top to bottom, with a steady 10×22px #E9D8C2 block caret at the front; indentation appears instantly; each token takes its syntax color as it completes and is never recolored.
- The label: a 4 × 6 inch thermal shipping label at 360×540px, white with a 2px black border and 2px black rules between its sections, built in HTML/CSS: a top band with "GROUND SAVER" in Source Sans 3 700 26px and a 64px black square holding a white "G"; the from block in Source Code Pro 500 13px; the to block in Source Sans 3 700 22px on three lines; a 300×90 barcode of seeded black bars 1–4px wide with 1–3px gaps; the tracking number under it in Source Code Pro 500 17px; the footer line in Source Code Pro 500 12px. Black and white only.
- Click feedback everywhere is the same brick ring; there is no other click effect.
- Premium: code that would really run, every column aligned on the monospace grid, an honest status and timing, fast but readable streaming, a label that looks like a real thermal print. Cheap: random symbols posing as code, neon terminals, rainbow syntax, bouncing panels, a giant 3D "200", confetti.
- Banned: real company names, logos and UI copied from existing products, including real carriers and real API docs layouts; lorem ipsum; gradients, glow and glassmorphism; emoji; code that wouldn't parse; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.7s: the eyebrow and headline rise 16px and fade in (easeOutQuart 0.6 s, 0.08 s apart); the request card and the response panel rise 24px and fade in, starting at 0.2 s and 0.3 s.
- 0.7–1.6s: the cURL code reveals line by line, 40 ms apart; the cursor glides in from the lower right and parks near the tabs.
- 1.6–2.0s: the cursor moves to "JavaScript" on a gentle curve (easeInOutCubic) and clicks at 1.9 s; the tab switches.
- 2.6–3.0s: the cursor moves to "Python" and clicks at 2.9 s; the tab switches.
- 3.3–3.8s: the cursor travels to Send and clicks at 3.8 s.
- 3.8–4.1s: sending; the 200 OK pill lands at 4.05 s.
- 4.15–5.3s: the JSON streams in; the caret disappears at 5.3 s.
- 5.3–6.2s: rest. The 6.0 s frame is the poster: the eyebrow and headline, the Python tab with all 14 lines and its install line, the response header with 200 OK and 184 ms, and the complete JSON response.
- 6.3–7.4s: the cursor moves to the label_url value, which underlines on hover at 6.6 s; click at 6.8 s; a #FBF8F3 scrim at 40% settles over both panels in 0.3 s and the label rises from below the frame to rest centered on x 960, y 290–830, rotated −2°, with a 0 30px 60px rgba(0,0,0,0.18) shadow (easeOutQuint, 0.7 s).
- 7.6–8.0s: the closing line fades in centered on x 960 at baseline y 1010, in Source Sans 3 500 20px muted, with "Get a test key" in brick.
- 8.0–10.0s: hold.
For other lengths, stretch the time on each tab and the rest after streaming; keep the streaming speed and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape, the cursor, the icons and the barcode are drawn in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG (the barcode bars and the cursor's curve). Typed and streamed text is sliced from the full strings by t. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: HTML and CSS, every element absolutely positioned on the 1920×1080 stage; seek writes transforms, opacities, widths and text content directly as inline styles. Code and JSON are real text spans, so they stay crisp at any scale.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that all three tabs match the given code exactly, character for character, with their indentation; no code line runs past its card; the tab underline sits under the active tab every time; the pill reads 200 OK and the time 184 ms; the JSON is valid and complete at 6.0 s, with no caret left behind; the cursor's clicks land exactly on the tabs, Send and the label_url value; the label reads cleanly, black on white, with a believable barcode; nothing flashes; and the final frame shows the label over the dimmed panels with the closing line. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
