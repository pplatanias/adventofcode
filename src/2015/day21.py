from collections import namedtuple
from itertools import product
from math import ceil

item = namedtuple('Item', ['cost', 'dmg', 'ar'])

weapons = [
    item(8, 4, 0),
    item(10, 5, 0),
    item(25, 6, 0),
    item(40, 7, 0),
    item(74, 8, 0),
]

armors = [
    item(13, 0, 1),
    item(31, 0, 2),
    item(53, 0, 3),
    item(75, 0, 4),
    item(102, 0, 5),
    item(0, 0, 0),  # no armor
]

rings = [
    item(25, 1, 0),
    item(50, 2, 0),
    item(100, 3, 0),
    item(20, 0, 1),
    item(40, 0, 2),
    item(80, 0, 3),
    item(0, 0, 0),  # no ring
]

hp = 100
boss_hp = 104
boss_ar = 1
boss_dmg = 8

itemcombos = product(range(len(weapons)), range(len(armors)), range(len(rings)), range(len(rings)))

costs_win = []
costs_lose = []
for combo in itemcombos:
    cost = weapons[combo[0]].cost
    cost += armors[combo[1]].cost
    dmg = weapons[combo[0]].dmg
    ar = armors[combo[1]].ar

    prev_ring = None
    for ring in combo[2:]:
        if prev_ring != 6:
            if ring == prev_ring:
                continue
        dmg += rings[ring].dmg
        ar += rings[ring].ar
        cost += rings[ring].cost
        prev_ring = ring

    ttk_boss = ceil(boss_hp / max(dmg - boss_ar, 1))
    ttk_player = ceil(hp / max(boss_dmg - ar, 1))

    if ttk_player >= ttk_boss:
        costs_win.append((cost, combo))
    else:
        costs_lose.append((cost, combo))

print(min(costs_win))
print(max(costs_lose))
