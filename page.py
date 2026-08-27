import json, os
body=open('body.html').read()
ext=json.load(open('data/extracted.json')) if os.path.exists('data/extracted.json') else {'sources':[]}
nsrc=2+len(ext.get('sources',[]))
extra_note=''
if not ext.get('sources'):
    extra_note=' <b style="color:#c99a7a;">Cardsrealm and postboard.gg extraction is still running &mdash; their blocks will appear on the next refresh.</b>'

MAIN=[(4,"Deceit"),(4,"Superior Spider-Man"),(4,"Requiting Hex"),(3,"Doomsday Excruciator"),
(4,"Duress"),(3,"Stock Up"),(3,"Bitter Triumph"),(2,"Emeritus of Ideation"),(2,"Day of Black Sun"),
(2,"Winternight Stories"),(2,"Hidden Lair"),(1,"Deadly Cover-Up"),(1,"M.O.D.O.K."),
(1,"Strategic Betrayal"),(4,"Restless Reef"),(4,"Watery Grave"),(4,"Gloomlake Verge"),
(2,"Undercity Sewers"),(1,"Cavern of Souls"),(9,"Swamp")]
def dl(l): return '\n'.join(f'<div class="dlc"><span>{q}</span>{n}</div>' for q,n in l)

page=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>Dimir Excruciator &mdash; SB Guide</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d0d0d;color:#e0e0e0;font-size:14px;line-height:1.5}}
.top-bar{{background:#111;padding:14px 16px 10px;border-bottom:1px solid #222;position:sticky;top:0;z-index:20}}
.top-bar h1{{font-size:16px;font-weight:700;color:#8a9ad8}}
.top-bar .subtitle{{font-size:11px;color:#555;margin-top:2px}}
.banner{{padding:11px 16px;background:#0f1118;border-bottom:1px solid #1a1e2a;font-size:11.5px;color:#8592a8;line-height:1.65}}
.mu{{border-bottom:1px solid #181818}}
.mu-head{{display:flex;align-items:center;gap:10px;padding:13px 16px;cursor:pointer;user-select:none;-webkit-tap-highlight-color:transparent}}
.mu-head:active{{background:#161616}}
.mu-name{{flex:1;font-size:15px;font-weight:600;color:#e8e8e8}}
.cnt{{font-size:10px;font-weight:700;background:#1e2634;color:#9ab0cc;border-radius:10px;padding:2px 8px}}
.chev{{color:#333;font-size:11px;transition:transform .18s}}
.mu.open .chev{{transform:rotate(180deg)}}
.mu-body{{display:none;padding:0 12px 14px}}
.mu.open .mu-body{{display:block}}
.why{{font-size:11.5px;color:#8a8a8a;font-style:italic;padding:0 4px 10px;line-height:1.6}}
.gc{{background:#141414;border:1px solid #1f1f1f;border-radius:7px;margin-bottom:8px;overflow:hidden}}
.gc.you-a{{border-color:#22384a;background:#101619}}
.gc.you-b{{border-left:3px solid #6a5faa}}
.gc-head{{background:#191919;padding:7px 11px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.gc.you-a .gc-head{{background:#141d24}}
.gc-author{{font-size:12px;font-weight:600}}
.mshare{{font-size:9px;font-weight:700;background:#22303c;color:#8fb0c8;border-radius:3px;padding:2px 6px}}
.warn{{font-size:9.5px;font-weight:700;background:#3a2a1a;color:#e0a878;border-radius:3px;padding:2px 7px;margin-left:auto}}
.gc-cols{{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:9px 11px}}
.col-head{{font-size:10px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;margin-bottom:5px}}
.col-in .col-head{{color:#4caf6b}} .col-out .col-head{{color:#e05a5a}}
.c{{font-size:12px;padding:2px 0;line-height:1.45}}
.c.in{{color:#b8e8c8}} .c.out{{color:#f5b8b8}}
.c .q{{font-weight:700;font-size:11px;color:#e05a5a;margin-right:3px}}
.c .qi{{font-weight:700;font-size:11px;color:#4caf6b;margin-right:3px}}
.gc-note{{padding:6px 11px 8px;border-top:1px solid #1a1a1a;font-size:11px;color:#999;font-style:italic;line-height:1.55}}
.dl{{background:#141414;border:1px solid #1f1f1f;border-radius:7px;margin:10px 12px;overflow:hidden}}
.dl>summary{{list-style:none;cursor:pointer;padding:9px 12px;font-size:12px;font-weight:700;color:#8a9ad8}}
.dl>summary::-webkit-details-marker{{display:none}}
.dl>summary::after{{content:' \\25BC';font-size:9px;color:#555}}
.dl[open]>summary::after{{content:' \\25B2'}}
.dlg{{padding:2px 12px 12px}}
.dlg h4{{font-size:10px;letter-spacing:.7px;text-transform:uppercase;color:#5f7085;margin-bottom:4px}}
.dlc{{font-size:12px;color:#ddd;line-height:1.55}}
.dlc span{{color:#4caf6b;font-weight:700;margin-right:4px}}
.sect{{padding:16px;border-top:2px solid #222}}
.sect h2{{font-size:14px;color:#8a9ad8;margin-bottom:9px}}
.sect p{{font-size:12.5px;color:#c0c0c0;line-height:1.75;margin-bottom:9px}}
.sect a{{color:#9ab8e8;text-decoration:none;font-weight:600}}
.flagbox{{background:#161009;border:1px solid #2e2213;border-radius:7px;padding:11px 13px;margin:10px 12px;font-size:12px;color:#d8b48c;line-height:1.7}}
.flagbox b{{color:#e0a878}}
@media (max-width:520px){{.gc-cols{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="top-bar">
  <h1>Dimir Excruciator &mdash; Sideboard Guide</h1>
  <div class="subtitle">Standard &middot; your two grids + every other guide that has real IN/OUT plans</div>
</div>
<div class="banner"><b style="color:#8a9ad8;">Reading this:</b> your <b style="color:#6ab0d4">current grid</b> is the primary plan in each matchup. Your <b style="color:#8a7fc0">pre-ban grid</b> sits underneath as historical context &mdash; it predates the 2026-08-10 bans and runs Harvester of Misery, Insatiable Avarice, Wan Shi Tong and Superior Spider-Man in roles the current list fills differently. Published guides are shown for comparison, not as equals: their 75s differ from yours.{extra_note} Every plan's IN/OUT totals were recomputed; mismatches are labelled rather than silently corrected.</div>

<div class="flagbox">
  <b>Two things I could not resolve &mdash; worth a look before you trust those cells:</b><br>
  1. <b>"Kavaero"</b> appears in five of your current grid's OUT columns (Prowess, Selesnya Practiced Offense, Selesnya Landfall, Azorius Momo, Bant Rhythm). No card by that name exists on Scryfall under any spelling I could find, and it is not in the MTGGoldfish stock list. An April MTG Arena Zone primer independently lists "4 Kavaero, Mind-Bitten", so it is probably a real card I am failing to match &mdash; tell me the right name and I will correct all five.<br>
  2. <b>Two of your current plans are off by one card:</b> Izzet Lessons is published 6 in / 7 out, and Azorius Tempo 7 in / 8 out. Both are labelled in place. Your pre-ban grid balances perfectly across all 11 matchups, so this looks like transcription drift in the newer sheet rather than a habit.
</div>

<details class="dl" id="deck75">
  <summary>Reference list &mdash; MTGGoldfish stock build (yours may differ)</summary>
  <div class="dlg">
    <h4>Maindeck (60)</h4>
{dl(MAIN)}
    <h4 style="margin-top:10px">Sideboard</h4>
    <div class="dlc" style="color:#9a9a9a;font-style:italic">Your grids reference: Quantum Riddler, Qarsi Revenant, Nowhere to Run, Ghost Vacuum, Flashfreeze, Deathmark, Emeritus of Ideation, Doomsday Excruciator, Strategic Betrayal, Intimidation Tactics, Duress, Day of Black Sun. Send me your exact 15 and I will pin it here.</div>
  </div>
</details>

{body}
<div class="sect">
  <h2>&#128218; The other guides</h2>
  <p>Full verified library with caveats: <a href="https://emersonspartz.github.io/excruciator-guide-library/">excruciator-guide-library</a> &mdash; 22 guides from 130 candidates.</p>
  <p>Only three sources anywhere have per-matchup IN/OUT plans, and all three are compromised:
  <a href="https://mtg.cardsrealm.com/en-us/articles/standard-dimir-excruciator-deck-tech-sideboard-guide">Cardsrealm</a> explains the reasoning best but is a pre-ban March list;
  <a href="https://postboard.gg/archetype/standard/dimir-excruciator">postboard.gg</a> is current but auto-generated and explains only 3 of its 10 matchups;
  <a href="https://metafy.gg/guides/view/dimir-excrutiator-7vDhtdQQnJb">Metafy (OafMcNamara)</a> is human and matchup-deep but video-only and paywalled.
  Your two grids together cover more matchups than any of them.</p>
</div>
</body></html>'''
open('index.html','w').write(page)
import re
print('page KB:',len(page)//1024,'| sections:',len(re.findall(r'<div class="mu(?: open)?">',page)),'| blocks:',page.count('<div class="gc '))
