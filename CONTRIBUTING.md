# Submissions welcome!

**Share your motion prompt by opening a pull request.** Your own work and recommendations are welcome, from any model or platform.

## Add your motion

1. Fork this repository and copy [`examples/_template.md`](examples/_template.md) to `examples/your-motion-name.md`.
2. Add a preview, your prompt, the model you used and creator credit. Pick a [category](docs/CATEGORIES.md), or suggest a new one.
3. Open a pull request with a short note about what you made and why it is worth sharing.

You can do this entirely in GitHub's web editor. One work per PR keeps discussion focused. Keep descriptions in English and prompts in their original language. There is no follower, view or star threshold.

Include required references, skills, tools and important follow-up prompts when relevant. For someone else's work, credit the original creator and link their published prompt. Say clearly if the full prompt is unavailable.

A Markdown card is enough to start a PR. Maintainers will help with category placement, structured metadata and preview assets during review. Respond and update the same PR if changes are requested.

## Updating structured data

If you want to include the complete importable record too:

- Add it to `data/motion-prompts.json` and record its sources in `data/provenance.json`.
- Add the entry ID to its primary category in `data/categories.json`.
- Put incomplete research in `data/candidates.json`; do not invent missing details.
- Run `python3 scripts/build.py` and `python3 scripts/validate.py`.

See the [data contract](docs/DATA_FORMAT.md) and [verification rules](docs/SOURCING.md). Generated indexes are rebuilt from data; edit the source records rather than those indexes.

For corrections or removals, open an issue or PR identifying the work and requested change. Third-party works retain their creators' rights; see [third-party content](THIRD_PARTY.md).
