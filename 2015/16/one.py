lines = [": ".join(line.split(": ")[1:]) for line in open("input.txt").read().split("\n")]
sues = []
for line in lines:
    sue = {}
    props = line.split(", ")
    for p in props:
        key, value = p.split(": ")
        sue[key] = int(value)
    sues.append(sue)

target = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for i in range(len(sues)):
    sue = sues[i]
    for prop in sue:
        if sue[prop] != target[prop]: break
    else: print(i + 1)
