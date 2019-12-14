#!/usr/bin/env python3

import math

puzzle_input = """180 ORE => 9 DQFL
3 HGCR, 9 TKRT => 8 ZBLC
1 MZQLG, 12 RPLCK, 8 PDTP => 8 VCFX
3 ZBLC, 19 VFZX => 1 SJQL
1 CRPGK => 4 TPRT
7 HGCR, 4 TGCW, 1 VFZX => 9 JBPHS
8 GJHX => 4 NSDBV
1 VFTG => 2 QNWD
1 WDKW, 2 DWRH, 6 VNMV, 2 HFHL, 55 GJHX, 4 NSDBV, 15 KLJMS, 17 KZDJ => 1 FUEL
2 JHSJ, 15 JNWJ, 1 ZMFXQ => 4 GVRK
1 PJFBD => 3 MZQLG
1 SJQL, 11 LPVWN => 9 DLZS
3 PRMJ, 2 XNWV => 6 JHSJ
4 SJQL => 8 PJFBD
14 QNWD => 6 STHQ
5 CNLFV, 2 VFTG => 9 XNWV
17 LWNKB, 6 KBWF, 3 PLSCB => 8 KZDJ
6 LHWZQ, 5 LWNKB => 3 ZDWX
5 RPLCK, 2 LPVWN => 8 ZMFXQ
1 QNWD, 2 TKRT => 3 CRPGK
1 JBPHS, 1 XNWV => 6 TLRST
21 ZDWX, 3 FZDP, 4 CRPGK => 6 PDTP
1 JCVP => 1 WXDVT
2 CRPGK => 9 FGVL
4 DQFL, 2 VNMV => 1 HGCR
2 GVRK, 2 VCFX, 3 PJFBD, 1 PLSCB, 23 FZDP, 22 PCSM, 1 JLVQ => 6 HFHL
1 CRPGK, 5 PJFBD, 4 XTCP => 8 PLSCB
1 HTZW, 17 FGVL => 3 LHWZQ
2 KBWF => 4 DQKLC
2 LHWZQ => 2 PRMJ
2 DLZS, 2 VCFX, 15 PDTP, 14 ZDWX, 35 NBZC, 20 JVMF, 1 BGWMS => 3 DWRH
2 TKVCX, 6 RPLCK, 2 HTZW => 4 XTCP
8 CNLFV, 1 NRSD, 1 VFTG => 9 VFZX
1 TLRST => 4 WDKW
9 VFCZG => 7 GJHX
4 FZDP => 8 JLVQ
2 ZMFXQ, 2 STHQ => 6 QDZB
2 SJQL, 8 ZDWX, 6 LPRL, 6 WXDVT, 1 TPRT, 1 JNWJ => 8 KLJMS
6 JBPHS, 2 ZBLC => 6 HTZW
1 PDTP, 2 LHWZQ => 8 JNWJ
8 ZBLC => 7 TKVCX
2 WDKW, 31 QDZB => 4 PCSM
15 GJHX, 5 TKVCX => 7 FZDP
15 SJQL, 3 PRMJ => 4 JCVP
31 CNLFV => 1 TGCW
1 TLRST, 2 WDKW => 9 KBWF
102 ORE => 7 VNMV
103 ORE => 5 CNLFV
163 ORE => 2 VFTG
5 NRSD, 1 STHQ => 3 VFCZG
16 LPVWN, 13 KBWF => 2 BGWMS
5 BGWMS, 11 SJQL, 9 FZDP => 6 NBZC
175 ORE => 7 NRSD
5 HTZW => 4 LPVWN
4 PRMJ => 7 JVMF
6 PCSM, 8 DQKLC => 7 LPRL
2 CNLFV => 7 TKRT
3 FZDP => 3 LWNKB
1 HTZW => 4 RPLCK"""

class Nanofactory:
    def __init__(self, reactions):
        self.reactions = reactions
        self.surplus_material = {}
        
    # Wie viel ORE benötige ich, um amount "material" herzustellen
    def get_required_ore(self, material, amount):
        
        # ORE: 1:1
        if material == "ORE":
            return amount
        
        #print("Requested:", amount, "x", material)
        
        # Genug Materialreste
        if material in self.surplus_material:
            # Rest reicht
            if amount <= self.surplus_material[material]:
                self.surplus_material[material] -= amount
                return 0
            
            # Rest aufbrauchen
            amount -= self.surplus_material[material]
        
        # Materialrest setzen
        self.surplus_material[material] = 0
        
        reaction = self.reactions[material]
        #print(" Need", amount, "x", material, ":", reaction['inp'], "=>", reaction["out"])
        
        multiplicator = 1 if reaction["out"] > amount else math.ceil(amount/reaction["out"])
        out_amount = multiplicator * reaction["out"]
        
        ore = 0
        for in_element, process_in_amount in reaction['inp'].items():
            #print(material, ":", multiplicator, "*", process_in_amount, in_element)
            ore += self.get_required_ore(in_element, multiplicator * process_in_amount)
        
        # Rest aufbewahren
        if out_amount > amount:
            self.surplus_material[material] += out_amount - amount
        
        return ore


puzzle_input = puzzle_input.split("\n")
reactions = {}
for reaction in puzzle_input:
    in_out = reaction.split(" => ") # ["1 A, 2 B", "1 C"]
    inp = {}
    for obj in in_out[0].split(", "):
        obj = obj.split(" ")
        inp[obj[1]] = int(obj[0])
    
    out = in_out[1].split(" ")
    # {"A": {"inp": [{"ORE": 10, "B": 2, ...], "out": 10}, "B": ...}
    reactions[out[1]] = {"inp": inp, "out": int(out[0])}


fab = Nanofactory(reactions)

# Teil 1
# 399063
print("Part 1:", fab.get_required_ore("FUEL", 1))


# Teil 2: Brute Force mittels Bisektion
# 4215654
available_ore = 1000000000000

upper_limit = available_ore
lower_limit = 1

step = upper_limit - lower_limit
num = lower_limit

while True:
    
    req_for_this_num = fab.get_required_ore("FUEL", num)
    print("Required ORE for", int(num), "FUEL:", req_for_this_num)
    
    # Ziel erreicht
    step = math.floor(step / 2)
    if step < 1:
        break
    
    if req_for_this_num > available_ore:
        num -= step
    else:
        num += step
