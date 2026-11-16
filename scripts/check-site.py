"""Dependency-free route, asset, fragment and disclosure regression checks."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True);self.ids=[];self.links=[];self.h1=0;self.stack=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  for key in ('href','src'):
   if key in a:self.links.append(a[key])
  if tag=='img':assert a.get('alt') and a.get('width') and a.get('height'),a
pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html') if p.name!='googlea0d4dbabbdad46aa.html'}
for path,page in pages.items():
 assert page.h1==1,(path,'one h1 required')
 assert len(page.ids)==len(set(page.ids)),(path,'duplicate IDs')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=ROOT/unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path)
  if not u.path:target=path
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(path,link)
  if u.fragment and target in pages:assert u.fragment in pages[target].ids,(path,link,'missing fragment')
privacy=(ROOT/'privacy/index.html').read_text()
assert 'tab-btn' not in privacy and 'Details awaiting confirmation' not in privacy
royal=(ROOT/'apps/royal-blackjack/index.html').read_text()
for phrase in ['18 or older','whichever is higher','no real-world monetary value','cannot be redeemed','Success in social casino','optional in-app purchases','com.haller.royalcardclub']:
 assert phrase in royal,phrase
assert 'More Apps by' not in royal
assert len(json.loads((ROOT/'data/apps.json').read_text()))==7
print(f'PASS: {len(pages)} pages; local routes, fragments, image attributes, headings, privacy separation and game disclosures')
