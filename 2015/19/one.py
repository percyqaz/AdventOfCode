data, molecule = open("input.txt").read().split("\n\n")
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

molecule = string_to_elements(molecule)

def replace(s):
    for i in range(len(s)):
        e = s[i]
        for r in replacements:
            if r[0] == e:
                yield s[0:i] + r[1] + s[i+1:]
seen = {}
for rep in replace(molecule):
    v = "".join(rep)
    if v not in seen: seen[v] = 0
    seen[v] += 1
print(len(seen))
