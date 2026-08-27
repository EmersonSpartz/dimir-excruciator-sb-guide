import json
# ---- GRID A: Emerson's current (post-ban) grid, 17 matchups ----
A = {
"Izzet Prowess":{"in":[[1,"Emeritus of Ideation"],[2,"Qarsi Revenant"],[1,"Nowhere to Run"],[1,"Day of Black Sun"],[1,"Quantum Riddler"],[1,"Strategic Betrayal"],[1,"Ghost Vacuum"],[1,"Duress"]],
                 "out":[[2,"Doomsday Excruciator"],[2,"Deadly Cover-Up"],[1,"Intimidation Tactics"],[1,"Kavaero"],[1,"Deceit"],[2,"Winternight Stories"]]},
"Selesnya Practiced Offense":{"in":[[1,"Nowhere to Run"],[1,"Day of Black Sun"],[2,"Flashfreeze"],[1,"Intimidation Tactics"],[1,"Strategic Betrayal"],[2,"Deathmark"],[1,"Quantum Riddler"],[1,"Emeritus of Ideation"]],
                 "out":[[2,"Kavaero"],[3,"Duress"],[1,"Qarsi Revenant"],[2,"Doomsday Excruciator"],[2,"Winternight Stories"]]},
"Jeskai Lessons Control":{"in":[[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"],[1,"Strategic Betrayal"],[1,"Ghost Vacuum"],[1,"Duress"],[2,"Flashfreeze"]],
                 "out":[[1,"Qarsi Revenant"],[2,"Bitter Triumph"],[2,"Day of Black Sun"],[1,"Intimidation Tactics"],[1,"Shoot the Sheriff"],[1,"Requiting Hex"]]},
"Selesnya Landfall":{"in":[[2,"Flashfreeze"],[1,"Intimidation Tactics"],[2,"Deathmark"],[1,"Doomsday Excruciator"],[1,"Nowhere to Run"],[1,"Day of Black Sun"]],
                 "out":[[1,"Quantum Riddler"],[1,"Qarsi Revenant"],[1,"Strategic Betrayal"],[3,"Duress"],[1,"Kavaero"],[1,"Winternight Stories"]]},
"Mono-Green Landfall":{"in":[[2,"Flashfreeze"],[1,"Day of Black Sun"],[2,"Deathmark"],[1,"Doomsday Excruciator"],[1,"Ghost Vacuum"]],
                 "out":[[1,"Quantum Riddler"],[1,"Qarsi Revenant"],[1,"Strategic Betrayal"],[3,"Duress"],[1,"Intimidation Tactics"]]},
"Izzet Spellementals":{"in":[[1,"Ghost Vacuum"],[1,"Duress"],[1,"Emeritus of Ideation"],[1,"Intimidation Tactics"],[1,"Strategic Betrayal"],[1,"Nowhere to Run"],[2,"Flashfreeze"],[1,"Quantum Riddler"]],
                 "out":[[2,"Day of Black Sun"],[4,"Requiting Hex"],[2,"Doomsday Excruciator"],[1,"Qarsi Revenant"]]},
"Izzet Lessons":{"in":[[1,"Ghost Vacuum"],[1,"Duress"],[1,"Flashfreeze"],[1,"Strategic Betrayal"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"]],
                 "out":[[2,"Deadly Cover-Up"],[2,"Day of Black Sun"],[1,"Intimidation Tactics"],[1,"Qarsi Revenant"],[1,"Shoot the Sheriff"]]},
"Dimir Excruciator (mirror)":{"in":[[1,"Ghost Vacuum"],[1,"Intimidation Tactics"],[1,"Strategic Betrayal"],[1,"Emeritus of Ideation"],[1,"Quantum Riddler"],[2,"Qarsi Revenant"],[1,"Duress"]],
                 "out":[[2,"Day of Black Sun"],[4,"Requiting Hex"],[2,"Doomsday Excruciator"]]},
"Golgari Midrange":{"in":[[2,"Deathmark"],[1,"Day of Black Sun"],[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"]],
                 "out":[[1,"Qarsi Revenant"],[1,"Strategic Betrayal"],[3,"Duress"],[1,"Intimidation Tactics"]]},
"Azorius Momo":{"in":[[1,"Nowhere to Run"],[1,"Day of Black Sun"],[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"],[2,"Deathmark"],[1,"Intimidation Tactics"]],
                 "out":[[1,"Qarsi Revenant"],[1,"Strategic Betrayal"],[3,"Duress"],[2,"Requiting Hex"],[1,"Kavaero"]]},
"4c Control":{"in":[[1,"Duress"],[2,"Flashfreeze"],[1,"Strategic Betrayal"],[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"],[2,"Qarsi Revenant"]],
                 "out":[[1,"Bitter Triumph"],[2,"Day of Black Sun"],[1,"Intimidation Tactics"],[1,"Shoot the Sheriff"],[4,"Requiting Hex"]]},
"Azorius Tempo":{"in":[[1,"Emeritus of Ideation"],[1,"Quantum Riddler"],[1,"Deathmark"],[2,"Qarsi Revenant"],[1,"Nowhere to Run"],[1,"Intimidation Tactics"]],
                 "out":[[2,"Day of Black Sun"],[2,"Doomsday Excruciator"],[3,"Duress"],[1,"Strategic Betrayal"]]},
"Kona Combo":{"in":[[1,"Duress"],[2,"Flashfreeze"],[1,"Intimidation Tactics"],[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"],[1,"Nowhere to Run"]],
                 "out":[[4,"Requiting Hex"],[2,"Day of Black Sun"],[1,"Strategic Betrayal"],[1,"Qarsi Revenant"]]},
"Mardu Discard":{"in":[[1,"Strategic Betrayal"],[1,"Qarsi Revenant"],[1,"Nowhere to Run"],[1,"Day of Black Sun"],[1,"Quantum Riddler"],[1,"Intimidation Tactics"]],
                 "out":[[2,"Doomsday Excruciator"],[3,"Duress"],[1,"Winternight Stories"]]},
"4c/5c Elementals":{"in":[[1,"Intimidation Tactics"],[1,"Strategic Betrayal"],[1,"Nowhere to Run"],[1,"Quantum Riddler"],[1,"Doomsday Excruciator"],[1,"Emeritus of Ideation"]],
                 "out":[[3,"Duress"],[2,"Day of Black Sun"],[1,"Qarsi Revenant"]]},
"Bant Rhythm":{"in":[[2,"Intimidation Tactics"],[1,"Doomsday Excruciator"],[2,"Flashfreeze"],[1,"Nowhere to Run"],[1,"Day of Black Sun"],[2,"Deathmark"]],
                 "out":[[1,"Quantum Riddler"],[1,"Qarsi Revenant"],[3,"Duress"],[1,"Strategic Betrayal"],[1,"Kavaero"],[2,"Winternight Stories"]]},
}
# ---- GRID B: Emerson's PRE-BAN grid (shorthand expanded), 11 matchups ----
SH={"Shoot":"Shoot the Sheriff","Flashfreeze":"Flashfreeze","Excruciator":"Doomsday Excruciator",
"Duress":"Duress","Hesit":"Cruelclaw's Heist","Heist":"Cruelclaw's Heist","Riddlers":"Quantum Riddler",
"Riddler":"Quantum Riddler","Lantern":"Soul-Guide Lantern","Annul":"Annul","Hex":"Requiting Hex",
"Harvester":"Harvester of Misery","Deadly":"Deadly Cover-Up","Tactics":"Intimidation Tactics",
"Bitter":"Bitter Triumph","Wan Shi":"Wan Shi Tong, Librarian","Wanshi":"Wan Shi Tong, Librarian",
"Spiderman":"Superior Spider-Man","Avarice":"Insatiable Avarice","Winternight":"Winternight Stories",
"Robbery":"Outrageous Robbery"}
Braw = {
"Badgermole Cub":("+1 Shoot +2 Flashfreeze","-3 Excruciator","If they play a couple of counters and Oko you can side in Duress"),
"Izzet Lessons":("+4 Duress +1 Hesit +3 Riddlers +2 Lantern +1 Annul","-4 Hex -1 Harvester -3 Deadly -2 Tactics -1 Bitter","If they play a big-creatures plan post-side, leave Bitter in"),
"Bant Airbender":("+2 Flashfreeze +1 Heist +1 Shoot","-1 Harvester -1 Wan Shi -1 Excruciator -1 Spiderman",""),
"Jeskai Control":("+4 Duress +1 Heist +3 Riddler +1 Robbery","-4 Hex -3 Deadly -1 Harvester -1 Excruciator",""),
"Landfall":("+2 Flashfreeze +1 Annul +1 Shoot +1 Heist","-1 Harvester -2 Hex -2 Winternight",""),
"Reanimator":("+2 Lantern +1 Heist +1 Shoot +1 Robbery +1 Riddler","-4 Hex -1 Harvester -1 Wan Shi",""),
"Mono Red":("+2 Flashfreeze +1 Shoot +1 Heist +1 Duress","-3 Excruciator -2 Avarice",""),
"Dimir Midrange":("+3 Riddler +1 Shoot +4 Duress +1 Robbery","-3 Excruciator -3 Deadly -2 Winternight -1 Spiderman",""),
"Izzet Spellementals":("+4 Duress +2 Lantern +1 Shoot +1 Heist +3 Riddler","-4 Hex -1 Harvester -3 Excruciator -2 Winternight -1 Wanshi",""),
"Mirror":("+3 Riddler +1 Robbery +1 Heist +1 Shoot +4 Duress","-4 Hex -3 Excruciator -1 Harvester -1 Wan Shi -1 Deadly",""),
"UW Tempo":("+4 Duress +1 Heist +1 Shoot +3 Riddler","-1 Harvester -4 Hex -3 Excruciator -1 Winternight",""),
}
import re
def parse(s, sign):
    out=[]
    for m in re.finditer(rf'\{sign}(\d+)\s+([A-Za-z][A-Za-z\s\'\-\.]*?)(?=\s[+\-]\d|\s*$)', s):
        q=int(m.group(1)); nm=m.group(2).strip()
        out.append([q, SH.get(nm, nm)])
    return out
B={}
for mu,(i,o,note) in Braw.items():
    B[mu]={"in":parse(i,'+'),"out":parse(o,'-'),"note":note}

def audit(name, g):
    print(f'--- {name} ---')
    bad=0
    for mu,p in g.items():
        ti=sum(q for q,_ in p['in']); to=sum(q for q,_ in p['out'])
        flag='' if ti==to else f'  <-- UNBALANCED ({ti} vs {to})'
        if ti!=to: bad+=1
        print(f'  {mu:<30} IN {ti:>2} / OUT {to:<2}{flag}')
    print(f'  -> {len(g)} matchups, {bad} unbalanced\n')
    return bad
ba=audit('GRID A (current / post-ban)',A)
bb=audit('GRID B (pre-ban)',B)
json.dump({'gridA':A,'gridB':B},open('grids.json','w'),indent=1)
print(f'saved. unresolved card name: "Kavaero" appears in Grid A OUT lists (5 matchups) - no Scryfall match')
