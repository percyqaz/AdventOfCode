containers = [int(i) for i in open("input.txt").read().split("\n")]

def combinations(i, accum):
    if i == len(containers):
        yield accum
        return

    for c in combinations(i + 1, accum + containers[i]):
        yield c
    for c in combinations(i + 1, accum):
        yield c

count = 0
for c in combinations(0, 0):
    if c == 150:
        count += 1
print(count)
