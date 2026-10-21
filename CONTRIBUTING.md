# Submissions welcome!

Made something worth moving? **[Submit your motion prompt](https://github.com/rudy2steiner/awesome-ai-motion-prompts/issues/new?template=submit-motion.yml)**.

Your own work and recommendations are both welcome, from any model or public platform. New creators are welcome: there is no follower, view or star threshold. Use one submission per work. Keep descriptions in English and published prompts in their original language.

## Submit without editing code

Open the submission form and share:

- A short title and primary [category](docs/CATEGORIES.md).
- Creator credit, the original source and a playable video or GIF. You can attach a preview in the GitHub editor.
- The model and working environment, if known.
- The prompt you used, or a published prompt/skill link. State clearly when the full prompt is unavailable.

References, required assets, dependencies, follow-up prompts and manual edits help others reproduce the result. Include them when applicable. Sharing a work does not promise identical output from the same prompt.

Choose the closest category, or suggest a new one in the form. The existing effect tags are separate from the main category. Models and platforms are metadata, not the main browsing hierarchy.

## Prefer a pull request?

Add complete records to `data/motion-prompts.json`, a prompt card to `examples/`, and evidence to `data/provenance.json`. Add the entry ID to the appropriate group in `data/categories.json`. Use existing entries as examples. Do not edit generated indexes directly.

Incomplete but useful research belongs in `data/candidates.json`. Never invent missing prompts or model claims. See the [data contract](docs/DATA_FORMAT.md) and [verification rules](docs/SOURCING.md).

Run:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

## How review works

A maintainer checks for duplicates, a working preview, clear creator credit, traceable instructions and motion quality. We look for composition, readable typography, coherent choreography, storytelling or a useful technique. Popularity is not an admission requirement.

Submitting is open; publication is reviewed. Maintainers may request missing details, place an incomplete record in the research queue, or decline work outside the collection's scope. Continue in the same issue when revising a submission. A new category can be discussed before changing the taxonomy.

For corrections or removals, open a regular issue with the record ID, original source and requested change. Third-party works retain their creators' rights; see [third-party content](THIRD_PARTY.md).
