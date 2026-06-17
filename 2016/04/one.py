lines = open("input.txt").read().split("\n")
m = 0
for line in lines:
    count = {}
    for c in line[:-10]:
        if c.islower():
            if c not in count: count[c] = 0
            count[c] += 1
    m += int(line[-10:-7]) if line[-6:-1] == ("".join([c for _, c in sorted([(-count[c], c) for c in count])][0:5])) else 0
print(m)
