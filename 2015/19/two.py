data, target_molecule = open("input.txt").read().split("\n\n")
replacements = []

def string_to_elements(s):
    output = '' 
    for c in s:
        if c.isupper():
            output += " "
        output += c
    return output.strip().split()

for line in data.split("\n"):
    split = line.split()
    replacements.append((split[0], string_to_elements(split[2])))

reachable = {}
for r in replacements:
    for c in r[1]:
        if r[0] not in reachable: reachable[r[0]] = set()
        reachable[r[0]].add(c)
#print(reachable)

for x in reachable:
    for y in list(reachable[x]):
        if y == x or y not in reachable: continue
        for z in reachable[y]:
            if z == x: continue
            reachable[x].add(z)
#print(reachable)

#target_molecule = "HCaCaSiThSiThSiThCaCaF"
target_molecule = string_to_elements(target_molecule)

def find(current, steps, remaining):

    if len(current) > len(remaining):
        return

    if remaining == []:
        print(steps)
        exit()

    if current[0] == remaining[0]:
        find(current[1:], steps, remaining[1:])
        return

    for rep, rep_with in replacements:
        if current[0] == rep:
            new_current = rep_with + current[1:]
            find(new_current, steps + 1, remaining)

find(["e"], 0, target_molecule)