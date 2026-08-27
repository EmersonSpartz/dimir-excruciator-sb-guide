import json, html as H, re, os
D='data/'
g=json.load(open(D+'grids.json'))
A,B=g['gridA'],g['gridB']
ext=json.load(open(D+'extracted.json')) if os.path.exists(D+'extracted.json') else {'sources':[]}
def esc(s): return H.escape(str(s),quote=False)
def tot(p,k): return sum(q for q,_ in p[k])

# ---- matchup ordering: current-meta first, then Grid-B-only (pre-ban) ----
ORDER=["Izzet Prowess","Jeskai Lessons Control","4c Control","Izzet Spellementals","Izzet Lessons",
"Mono-Green Landfall","Selesnya Landfall","Selesnya Practiced Offense","Dimir Excruciator (mirror)",
"Azorius Momo","Azorius Tempo","Golgari Midrange","Mardu Discard","Kona Combo","4c/5c Elementals","Bant Rhythm","WBR","Boros Aggro"]
# Grid B matchup -> Grid A section it belongs under (pre-ban plans shown as historical context)
BMAP={"Izzet Lessons":"Izzet Lessons","Jeskai Control":"Jeskai Lessons Control","Landfall":"Mono-Green Landfall",
"Mono Red":None,"Dimir Midrange":"Dimir Excruciator (mirror)","Izzet Spellementals":"Izzet Spellementals",
"Mirror":"Dimir Excruciator (mirror)","UW Tempo":"Azorius Tempo","Badgermole Cub":None,
"Bant Airbender":None,"Reanimator":None}
# extracted sources: matchup -> section (fuzzy, by keyword)
def sect_for(name):
    n=name.lower()
    if 'mirror' in n or 'excruciator' in n: return "Dimir Excruciator (mirror)"
    if 'jeskai' in n: return "Jeskai Lessons Control"
    if 'spellemental' in n: return "Izzet Spellementals"
    if 'lesson' in n: return "Izzet Lessons"
    if 'prowess' in n or 'ur aggro' in n or 'izzet aggro' in n: return "Izzet Prowess"
    if 'mono-green' in n or 'mono green' in n: return "Mono-Green Landfall"
    if 'selesnya landfall' in n or n.strip().startswith('landfall'): return "Selesnya Landfall"
    if 'dimir midrange' in n: return "Dimir Excruciator (mirror)"
    if 'azorius tempo' in n or 'uw tempo' in n: return "Azorius Tempo"
    if '4c control' in n or 'four-color control' in n: return "4c Control"
    if 'momo' in n: return "Azorius Momo"
    if 'kona' in n: return "Kona Combo"
    if 'golgari' in n: return "Golgari Midrange"
    if n.strip().startswith('wbr') or 'mardu' in n: return "WBR"
    if 'boros' in n: return "Boros Aggro"
    if 'bant rhythm' in n: return "Bant Rhythm"
    return None

AUTH={'you-a':('#6ab0d4','Your grid &mdash; current'),
      'you-b':('#8a7fc0','Your grid &mdash; pre-ban (historical)'),
      'cardsrealm':('#e07040','Cardsrealm / Romeu'),
      'postboard':('#9a9a9a','postboard.gg (auto-generated)')}

def rows(items,c,qc):
    if not items: return f'          <div class="c {c}" style="font-style:italic;color:#888;">(nothing)</div>'
    return '\n'.join(f'          <div class="c {c}"><span class="{qc}">{q}</span>{esc(n)}</div>' for q,n in items)

def block(key,plan,extra_note=None,meta=None):
    color,label=AUTH[key]
    ti,to=tot(plan,'in'),tot(plan,'out')
    warn='' if ti==to else f'<span class="warn">published as {ti} in / {to} out &mdash; off by {abs(ti-to)}</span>'
    notes=[]
    if plan.get('note'): notes.append(plan['note'])
    if plan.get('reasoning') and plan['reasoning'].lower()!='none given': notes.append(plan['reasoning'])
    if extra_note: notes.append(extra_note)
    nh=f'\n      <div class="gc-note">{esc(" &middot; ".join(notes))}</div>'.replace('&amp;middot;','&middot;') if notes else ''
    m=f'<span class="mshare">{esc(meta)}</span>' if meta else ''
    return f'''<div class="gc {key}">
      <div class="gc-head"><span class="gc-author" style="color:{color}">{label}</span>{m}{warn}</div>
      <div class="gc-cols">
        <div class="col-in"><div class="col-head">IN</div>
{rows(plan['in'],"in","qi")}
        </div>
        <div class="col-out"><div class="col-head">OUT</div>
{rows(plan['out'],"out","q")}
        </div>
      </div>{nh}
    </div>'''

# assemble per-section blocks
secs={m:[] for m in ORDER}
for mu in ORDER:
    if mu in A: secs[mu].append(block('you-a',A[mu]))
for bmu,plan in B.items():
    tgt=BMAP.get(bmu)
    if tgt and tgt in secs:
        secs[tgt].append(block('you-b',plan,f'Your pre-ban grid labelled this "{bmu}".'))
for s in ext.get('sources',[]):
    key='cardsrealm' if 'cardsrealm' in s['source'].lower() else 'postboard'
    for m in s.get('matchups',[]):
        tgt=sect_for(m['matchup'])
        if tgt and tgt in secs:
            meta=re.search(r'\(([\d.]+%)\)',m['matchup'])
            secs[tgt].append(block(key,{'in':[[x['q'],x['card']] for x in m['in']],
                'out':[[x['q'],x['card']] for x in m['out']],'reasoning':m.get('reasoning','')},
                f'Their label: "{m["matchup"]}".', meta.group(1) if meta else None))

# orphans: Grid B + extracted matchups with no home section
orphans=[]
for bmu,plan in B.items():
    if BMAP.get(bmu) is None:
        orphans.append(('you-b',bmu,plan,'Pre-ban only &mdash; no current section for this archetype.'))
for s in ext.get('sources',[]):
    key='cardsrealm' if 'cardsrealm' in s['source'].lower() else 'postboard'
    for m in s.get('matchups',[]):
        if sect_for(m['matchup']) is None:
            orphans.append((key,m['matchup'],{'in':[[x['q'],x['card']] for x in m['in']],
                'out':[[x['q'],x['card']] for x in m['out']],'reasoning':m.get('reasoning','')},None))

body=''
for i,mu in enumerate(ORDER):
    if not secs[mu]: continue
    body+=f'''<div class="mu{' open' if i==0 else ''}">
  <div class="mu-head" onclick="this.parentElement.classList.toggle('open')">
    <span class="mu-name">vs. {esc(mu)}</span><span class="cnt">{len(secs[mu])}</span><span class="chev">&#9660;</span>
  </div>
  <div class="mu-body">
{chr(10).join(secs[mu])}
  </div>
</div>
'''
if orphans:
    ob=''.join(block(k,p,n) if n else block(k,p) for k,_,p,n in orphans)
    labels=', '.join(esc(nm) for _,nm,_,_ in orphans)
    body+=f'''<div class="mu">
  <div class="mu-head" onclick="this.parentElement.classList.toggle('open')">
    <span class="mu-name">Other / retired matchups</span><span class="cnt">{len(orphans)}</span><span class="chev">&#9660;</span>
  </div>
  <div class="mu-body">
    <div class="why">Plans whose archetype has no section in the current list: {labels}. Badgermole Cub was banned 2026-08-10, so that one is dead.</div>
{ob}
  </div>
</div>
'''
open('body.html','w').write(body)
print(f'sections={sum(1 for m in ORDER if secs[m])} blocks={sum(len(v) for v in secs.values())} orphans={len(orphans)}')
