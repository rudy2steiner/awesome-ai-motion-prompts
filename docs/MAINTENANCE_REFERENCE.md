# Maintenance reference: awesome-opus5-5-videos

Inspected through chrome-mcp on 2026-10-21. Source repository: [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos).

## Content organization

The repository uses a [structured JSON array](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/main/data/videos.json) and individual Markdown prompt files. At inspection, the data contained 703 records; the README described 418 live remakes and highlighted 100 works. The main sections are motion graphics, explainers, 3D scenes, and games/interactive work, with implementation tags recorded separately.

Records include creator and source links, a category, technical tags, prompt text, a partial-prompt flag, poster URL, online detail URL, addition date and remake availability. A [prompt card](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/main/prompts/prasenx-693512.md) contains attribution, production tags, the prompt and links to the original and online comparison. Tags labeled as remake technologies should not automatically be treated as the original creator's tools.

## Media and viewing

README preview images are served from `media.skillry.dev`, using per-work preview assets rather than raw X video URLs. The README credits short hosted preview clips. The online gallery carries the richer original/remake comparison experience. This separates a quick look inside GitHub from an optional full viewing page; it does not require opening an external site for every glance.

## Updates and curation

The [commit history](https://github.com/yihui-dev/awesome-opus5-5-videos/commits/main/) shows dated batch additions and removals. Examples include removing five entries whose prompt text was not captured and later removing 150 entries outside its plain-prompt scope. The latest visible commit was on 2026-10-13. The README's update summary does not reflect that later cleanup, illustrating why commit history and data should also be checked.

No collection scripts or `.github/workflows` directory were visible in the public root listing. That is insufficient evidence to describe this as a scheduled, fully automated collector; collection or generation could happen outside the public repository. No dedicated contribution guide or submission form was visible in that listing. The README directs creator corrections/removal requests to Issues.

## Applied here

Keep the README editable by contributors, grouped by creation purpose. Use short inline previews and in-repository prompt cards; keep online viewing optional. Retain structured exports for maintainers, with source and verification metadata. Record preview source ranges so assets can be rebuilt. Review batch imports instead of promoting every discovered item to the public selection.
