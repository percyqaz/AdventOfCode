data = open("graph.txt").read().strip().split("\n")

dist = {}
for line in data:
    split = line.split()
    a = int(split[0])
    b = int(split[2])
    d = int(split[4])
    if a not in dist: dist[a] = {}
    dist[a][b] = d
    if b not in dist: dist[b] = {}
    dist[b][a] = d

import itertools

mind = 999999999999999
for p in itertools.permutations([1,2,3,4,5,6,7]):
    d = 0
    p = [0] + list(p) + [0]
    for i in range(len(p) - 1):
        d += dist[p[i]][p[i+1]]
    mind = min(d, mind)
print(mind)
