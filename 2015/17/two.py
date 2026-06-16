containers = [int(i) for i in open("input.txt").read().split("\n")]

def combinations(i, count, accum):
    if i == len(containers):
        yield (count, accum)
        return

    for c in combinations(i + 1, count + 1, accum + containers[i]):
        yield c
    for c in combinations(i + 1, count, accum):
        yield c

count = 0
min_containers = len(containers) + 1
for cc, c in combinations(0, 0, 0):
    if c == 150:
        if cc < min_containers:
            min_containers = cc
            count = 1
        elif cc == min_containers:
            count += 1
print(count)
