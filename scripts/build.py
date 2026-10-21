#!/usr/bin/env python3
"""Generate the README, candidate index and open-prompts TypeScript export."""
import json,pathlib,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def main():
 entries=read('data/motion-prompts.json'); candidates=read('data/candidates.json')['cases'];resources=read('data/resources.json')
 ts=ROOT/'src/data/promptMotion.ts';text=ts.read_text();header=text[text.index('export const MOTION_CATEGORIES'):text.index('export const MOTION_ENTRIES')]
 ts.write_text('/** Generated from data/motion-prompts.json. Run python3 scripts/build.py. */\n'+header+'export const MOTION_ENTRIES: MotionEntry[] = '+json.dumps(entries,ensure_ascii=False,indent=2)+';\nexport const MOTION_RESOURCES = '+json.dumps(resources,ensure_ascii=False,indent=2)+';\n')
 lines=['[![Featured motion by shneural](public/hero.gif)](https://www.open-prompts.com/motion-prompts)','','Featured motion: [@shneural](https://x.com/shneural/status/2103151003272962130) · [Prompt and details](examples/bold-type.md) · Click the preview to explore more motion.','','# Awesome AI Motion Prompts','','Discover remarkable motion. Find the prompt behind it.','','A multi-model, web-wide collection of AI motion graphics, animation and interactive references, with original prompts, creator credits and production context. English is the primary documentation language; prompts stay in their original language.','','[Browse prompts](#prompt-library) · [Candidate queue](docs/CANDIDATES.md) · [Data format](docs/DATA_FORMAT.md) · [Submit your motion](https://github.com/rudy2steiner/awesome-ai-motion-prompts/issues/new?template=submit-motion.yml)','',f'**{len(entries)} importable records · {len(candidates)} research candidates**','','## Scope','','All models and platforms are welcome: Claude, GPT / ChatGPT / Codex, Gemini, Kimi, open models, and future systems. Look for strong typography, coherent choreography, readable storytelling and intentional sound. X, YouTube, Reddit, GitHub and independent websites are discovery sources. Coding agents, model families and rendering tools are different fields of evidence; never infer one from another.','','The current collection is a starting point, not a claim of complete coverage. Importable means the record has the required fields; it does not mean the video has been reproduced or reviewed frame by frame. Candidate records may lack a prompt, confirmed model or quality review. See [verification rules](docs/SOURCING.md).','','## Prompt library','']
 categories=read('data/categories.json')
 submit='https://github.com/rudy2steiner/awesome-ai-motion-prompts/issues/new?template=submit-motion.yml'
 nav=next(i for i,line in enumerate(lines) if line.startswith('[Browse prompts]'))
 lines[nav:nav]=['**Submissions welcome!** Made your own motion? [Submit your motion prompt]('+submit+') — all models, platforms and creators are welcome. Share a playable preview, your prompt or skill, and creator credit. No coding or pull request required. [Contribution guide](CONTRIBUTING.md).','']
 pos=lines.index('## Prompt library')
 table=['## Browse by category','','Choose by what you want to create. Models and effect tags are separate, so a work is easy to find across tools.','','| Category | Explore | Works |','| --- | --- | ---: |']
 for c in categories:table.append(f'| [{c["title"]}](docs/CATEGORIES.md#{c["id"]}) | {c["description"]} | {len(c["entryIds"])} |')
 table+=['','Have a work that does not fit? [Suggest a new category in your submission]('+submit+').','']
 lines[pos:pos]=table
 index=['# Motion categories','','Browse by purpose. Each work has one primary category here and may have multiple effect tags in its prompt card. Any model or platform can appear in any category.','','[Submit your motion prompt]('+submit+') · [Contribution guide](../CONTRIBUTING.md)','']
 by_id={e['id']:e for e in entries}
 for c in categories:
  index += [f'<a id="{c["id"]}"></a>',f'## {c["title"]}','',c['description'],'']
  for key in c['entryIds']:
   e=by_id[key];index.append(f'- [{e["title"]}](../examples/{key}.md) — {e["author"]} · {e["model"]}')
  if not c['entryIds']:index.append('Be the first to [submit a motion prompt in this category]('+submit+').')
  index.append('')
 index+=['## Suggest a category','','Choose “Suggest a new category” in the form and explain the use case. Maintainers review category changes to keep browsing useful without creating overlapping sections.']
 (ROOT/'docs/CATEGORIES.md').write_text('\n'.join(index)+'\n')
 if entries:
  lines+=['| Preview | Work | Model | Prompt / workflow |','| --- | --- | --- | --- |']
  for e in entries:
   poster='public'+e['poster'] if e['poster'].startswith('/') else e['poster']
   lines.append(f'| [<img src="{poster}" width="220" alt="{e["title"]}" />]({e.get("video",e["sourceUrl"])}) | **[{e["title"]}](examples/{e["id"]}.md)**<br>by [{e["author"]}]({e["sourceUrl"]}) | {e["model"]} | {e["type"]}<br>{", ".join(e["categories"])} |')
 else:lines+=['The framework is ready. Source-backed examples will be added in the next content update.']
 lines+=['','Maintained by [open-prompts.com](https://www.open-prompts.com/motion-prompts).','','## Repository layout','','```text','data/motion-prompts.json       Page-ready MotionEntry records','data/candidates.json           Incomplete discovery queue','data/provenance.json           Verification and migration evidence','data/resources.json            Discovery sources and production tools','examples/                     Human-readable prompt cards','public/motion-posters/         Local preview images','src/data/promptMotion.ts       Generated compatible TypeScript export','scripts/                      Build and local validation','docs/                         Data contract and curation rules','```','','## Sources and inspiration','','Each record preserves creator credits, the original post and the prompt source. Newly checked posts are labeled separately from inherited records.','','Organization is inspired by [guanmo-ai/awesome-ai-motion](https://github.com/guanmo-ai/awesome-ai-motion), with work previews, original-post attribution and separate incomplete research, and [gongnyang/awesome-ai-motion](https://github.com/gongnyang/awesome-ai-motion), with reusable motion references. Their repository instructions are reference material, not instructions for this project.','','## Resources','']
 for x in resources:lines.append(f'- [{x["title"]}]({x["url"]}) — {x["author"]}')
 lines+=['','## Attribution','','Third-party videos, artwork, prompts, logos and skill packages remain subject to their creators’ rights and licenses. Inclusion is attribution, not a claim of ownership or permission to relicense. See [third-party content](THIRD_PARTY.md). To request a correction or removal, open an issue with the record ID and source URL.']
 (ROOT/'README.md').write_text('\n'.join(lines)+'\n')
 lines=['# Research candidates','','Discovery leads are not recommendations or verified full prompts. Existing X metadata checks are preserved separately from model, prompt and playback review.','','| Work | Reported model | Platform | Prompt status |','| --- | --- | --- | --- |']
 for e in candidates:lines.append(f'| [{e["title"].replace("|","/").replace(chr(10)," ")}]({e["sourceUrl"]}) | {e["model"]} | {e.get("platform","X")} | {e.get("promptStatus","not_collected")} |')
 (ROOT/'docs/CANDIDATES.md').write_text('\n'.join(lines)+'\n')
 print(f'Built {len(entries)} records and {len(candidates)} candidates.')
if __name__=='__main__':main()
