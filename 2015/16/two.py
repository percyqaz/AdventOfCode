lines = [": ".join(line.split(": ")[1:]) for line in open("input.txt").read().split("\n")]
sues = []
for line in lines:
    sue = {}
    props = line.split(", ")
    for p in props:
        key, value = p.split(": ")
        sue[key] = int(value)
    sues.append(sue)

target = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1}

for i in range(len(sues)):
    sue = sues[i]
    for prop in sue:
        if not target[prop](sue[prop]): break
    else: print(i + 1)
