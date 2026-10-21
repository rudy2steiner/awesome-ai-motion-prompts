#!/usr/bin/env python3
"""Validate local data, assets, references and generated exports without network calls."""
import json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def require(ok,message):
 if not ok:raise ValueError(message)
def main():
 entries=read('data/motion-prompts.json'); candidates=read('data/candidates.json');evidence=read('data/provenance.json')['entries'];seen=set();posts=set()
 cats={'Product UI','Phone','Charts','Diagrams','Kinetic type','Shapes','Particles','Characters','Photos','Music','Code'}
 required={'id','title','author','type','model','categories','prompt','sourceUrl','promptSourceUrl','collectionUrl','poster','width','height'}
 allowed=required|{'video','skillUrl','requiresReference'}
 for e in entries:
  key=e['id'];require(required<=e.keys(),f'{key}: missing fields');require(e.keys()<=allowed,f'{key}: incompatible fields');require(key not in seen,f'duplicate id: {key}');seen.add(key)
  require(e['sourceUrl'] not in posts,f'duplicate source: {key}');posts.add(e['sourceUrl'])
  require(e['type'] in ('Prompt','Skill'),f'{key}: invalid type');require(bool(e['prompt'].strip()),f'{key}: empty prompt');require(set(e['categories'])<=cats,f'{key}: invalid category')
  require(all(isinstance(e[k],int) and e[k]>0 for k in ('width','height')),f'{key}: dimensions')
  for k in ['sourceUrl','promptSourceUrl','collectionUrl']+(['video'] if e.get('video') else []):require(e[k].startswith('https://'),f'{key}: invalid {k}')
  require((ROOT/'examples'/f'{key}.md').exists(),f'{key}: missing card');require(key in evidence,f'{key}: missing provenance')
  if e['poster'].startswith('/'):require((ROOT/'public'/e['poster'].lstrip('/')).is_file(),f'{key}: missing poster')
 for e in candidates['cases']:
  require(e['sourceUrl'] not in posts,f'duplicate candidate source: {e["sourceUrl"]}');posts.add(e['sourceUrl'])
 require(candidates['count']==len(candidates['cases']),'candidate count mismatch')
 categories=read('data/categories.json'); assigned=[];category_ids=set()
 for c in categories:
  require(c['id'] not in category_ids,'duplicate category ID');category_ids.add(c['id'])
  for key in c['entryIds']:require(key in seen,f'unknown category entry: {key}');assigned.append(key)
 require(len(assigned)==len(set(assigned)),'entries assigned to multiple primary categories')
 require(set(assigned)==seen,'every importable record needs a primary category')
 ts=(ROOT/'src/data/promptMotion.ts').read_text();mark='export const MOTION_ENTRIES: MotionEntry[] = ';encoded=ts.split(mark,1)[1].split(';\nexport const MOTION_RESOURCES',1)[0];require(json.loads(encoded)==entries,'TypeScript export is stale')
 # Check Markdown file references, excluding remote URLs, fragments and root-level asset paths.
 for path in [ROOT/'README.md',*list((ROOT/'examples').glob('*.md')),*list((ROOT/'docs').glob('*.md'))]:
  for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   if target.startswith(('http:','https:','#','/')):continue
   require((path.parent/target.split('#')[0]).exists(),f'{path.name}: broken local link {target}')
 print(f'PASS: {len(entries)} MotionEntry records, {len(candidates["cases"])} unique candidates, assets, cards, local links and TypeScript export.')
if __name__=='__main__':main()
