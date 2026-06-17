lines = open("input.txt").read().split("\n")
l = len(lines[0])
for i in range(l):
    count = {}
    for line in lines:
        if line[i] not in count: count[line[i]] = 0
        count[line[i]] += 1
    print(sorted([(count[c], c) for c in count])[0][1], end="")