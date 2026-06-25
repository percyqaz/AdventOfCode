data = [(int(split[0]), int(split[1])) for split in [line.split("-") for line in open("input.txt").read().split("\n")]]

data = sorted(data)

i = 0
while i + 1 < len(data):
    l1,h1 = data[i]
    l2,h2 = data[i + 1]

    if h1 + 1 >= l2:
        data.pop(i)
        data.pop(i)
        data.insert(i, (l1, max(h1, h2)))
    else:
        i += 1

# two alternatives (second utilises puzzle design)
print(4294967296 - sum([hi - lo + 1 for lo, hi in data]))
print(len(data) - 1)
