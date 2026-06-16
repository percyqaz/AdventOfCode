weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]
armors = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]
rings = [
        (0, 0, 0, "A"),
        (0, 0, 0, "B"),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]
def combos():
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring2 == ring1: continue
                    yield (weapon, armor, ring1, ring2)

def win(weapon, armor, ring1, ring2):
    cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
    atk = weapon[1] + armor[1] + ring1[1] + ring2[1]
    df = weapon[2] + armor[2] + ring1[2] + ring2[2]
    php = 100
    bhp = 104
    while bhp > 0 and php > 0:
        bhp -= max(1, atk - 1)
        if bhp <= 0:
            return cost 
        php -= max(1, 8 - df)
    return None 

m =129381038109283091830921 
for weapon, armor, ring1, ring2 in combos():
    outcome = win(weapon, armor, ring1, ring2)
    if outcome != None:
        m = min(m, outcome)
print(m)
