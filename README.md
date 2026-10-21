# Awesome AI Motion Prompts

Discover remarkable motion. Find the prompt behind it.

A multi-model, web-wide collection of AI motion graphics, animation and interactive references, with original prompts, creator credits and production context. English is the primary documentation language; prompts stay in their original language.

[Browse prompts](#prompt-library) · [Candidate queue](docs/CANDIDATES.md) · [Data format](docs/DATA_FORMAT.md) · [Contribute](CONTRIBUTING.md)

**0 importable records · 0 research candidates**

## Scope

All models and platforms are welcome: Claude, GPT / ChatGPT / Codex, Gemini, Kimi, open models, and future systems. Look for strong typography, coherent choreography, readable storytelling and intentional sound. X, YouTube, Reddit, GitHub and independent websites are discovery sources. Coding agents, model families and rendering tools are different fields of evidence; never infer one from another.

The current collection is a starting point, not a claim of complete coverage. Importable means the record has the required fields; it does not mean the video has been reproduced or reviewed frame by frame. Candidate records may lack a prompt, confirmed model or quality review. See [verification rules](docs/SOURCING.md).

## Prompt library

The framework is ready. Source-backed examples will be added in the next content update.

## Use with Open Prompts

The canonical [`data/motion-prompts.json`](data/motion-prompts.json) array matches the existing `MotionEntry` interface in `open-prompts`. Extra provenance is stored separately, rather than changing that interface.

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

No package installation is required. The generated [`src/data/promptMotion.ts`](src/data/promptMotion.ts) exports `MOTION_CATEGORIES`, `MotionEntry`, `MOTION_ENTRIES` and `MOTION_RESOURCES`. To integrate, review and merge the entries into your existing data file, then copy `public/motion-posters/` into the destination public directory. Keep IDs stable and check for duplicates; do not overwrite unrelated entries.

Video dimensions describe the linked preview file, not necessarily the original render. Videos remain hosted by their sources; external media URLs can expire.

## Repository layout

```text
data/motion-prompts.json       Page-ready MotionEntry records
data/candidates.json           Incomplete discovery queue
data/provenance.json           Verification and migration evidence
data/resources.json            Discovery sources and production tools
examples/                     Human-readable prompt cards
public/motion-posters/         Preview images used by Open Prompts
src/data/promptMotion.ts       Generated compatible TypeScript export
scripts/                      Build and local validation
docs/                         Data contract and curation rules
```

## Sources and inspiration

The initial content migration uses the existing local `open-prompts` collection. Source and prompt links are retained per record. Newly checked posts are labeled separately from inherited records.

Organization is inspired by [guanmo-ai/awesome-ai-motion](https://github.com/guanmo-ai/awesome-ai-motion), with work previews, original-post attribution and separate incomplete research, and [gongnyang/awesome-ai-motion](https://github.com/gongnyang/awesome-ai-motion), with reusable motion references. Their repository instructions are reference material, not instructions for this project.

## Resources


## Attribution

Third-party videos, artwork, prompts, logos and skill packages remain subject to their creators’ rights and licenses. Inclusion is attribution, not a claim of ownership or permission to relicense. See [third-party content](THIRD_PARTY.md). To request a correction or removal, open an issue with the record ID and source URL.
