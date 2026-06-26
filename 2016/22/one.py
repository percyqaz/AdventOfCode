data = open("input.txt").read().split("\n")

nodes = []
for line in data[2:]:
    split = line.split()
    while "" in split:
        split.remove("")
    used = int(split[2][:-1])
    avail = int(split[3][:-1])
    nodes.append((used, avail))

c = 0
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if nodes[i][0] and nodes[i][0] <= nodes[j][1]:
            c += 1
    for j in range(i):
        if nodes[i][0] and nodes[i][0] <= nodes[j][1]:
            c += 1
print(c)
