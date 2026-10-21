#!/usr/bin/env python3
"""Build structured exports and the candidate index; preserve the community-edited README."""
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def main():
 entries=read('data/motion-prompts.json');candidates=read('data/candidates.json')['cases'];resources=read('data/resources.json')
 ts=ROOT/'src/data/promptMotion.ts';text=ts.read_text();header=text[text.index('export const MOTION_CATEGORIES'):text.index('export const MOTION_ENTRIES')]
 ts.write_text('/** Generated from data/motion-prompts.json. Run python3 scripts/build.py. */\n'+header+'export const MOTION_ENTRIES: MotionEntry[] = '+json.dumps(entries,ensure_ascii=False,indent=2)+';\nexport const MOTION_RESOURCES = '+json.dumps(resources,ensure_ascii=False,indent=2)+';\n')
 lines=['# Research candidates','','Discovery leads are not recommendations or verified full prompts. Existing X metadata checks are preserved separately from model, prompt and playback review.','','| Work | Reported model | Platform | Prompt status |','| --- | --- | --- | --- |']
 for e in candidates:lines.append(f'| [{e["title"].replace("|","/").replace(chr(10)," ")}]({e["sourceUrl"]}) | {e["model"]} | {e.get("platform","X")} | {e.get("promptStatus","not_collected")} |')
 (ROOT/'docs/CANDIDATES.md').write_text('\n'.join(lines)+'\n')
 playback=read('data/playback.json');categories=read('data/categories.json');by_id={e['id']:e for e in entries}
 lines=['# Full list','','[▶ Play online](https://www.open-prompts.com/motion-prompts) · [Featured motions](../README.md#prompt-library) · [Submit a PR](../CONTRIBUTING.md)','','## Contents','']
 for c in categories:lines.append(f'- [{c["title"]}](#{c["id"]})')
 lines+=['- [Research candidates](#research-candidates)','']
 for c in categories:
  lines += [f'<a id="{c["id"]}"></a>','',f'## {c["title"]}','']
  for key in c['entryIds']:
   e=by_id[key];watch=playback.get(key,e['sourceUrl'])
   lines.append(f'- [{e["title"]}](../examples/{key}.md) — @{e["author"]} · {e["model"]} · [Watch]({watch}) · [Prompt](../examples/{key}.md#prompt)')
  if not c['entryIds']:lines.append('No collected prompts yet.')
  lines.append('')
 lines+=['## Research candidates','','Discovery leads; prompts, attribution and viewing quality may still need review.','']
 for e in candidates:
  title=e['title'].replace(chr(10),' ')
  prompt=f' · [Prompt source]({e["promptSourceUrl"]})' if e.get('promptSourceUrl') else ''
  lines.append(f'- [{title}]({e["sourceUrl"]}) — @{e["author"]} · {e["model"]}'+prompt)
 (ROOT/'docs/FULL_LIST.md').write_text('\n'.join(lines)+'\n')
 print(f'Built {len(entries)} records and {len(candidates)} candidates. README.md left unchanged.')
if __name__=='__main__':main()
