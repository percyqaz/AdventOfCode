data = [(int(split[0]), int(split[1])) for split in [line.split("-") for line in open("input.txt").read().split("\n")]]

data = sorted(data)

c = 0
for lo, hi in data:
    if lo <= c and hi >= c:
        c = hi + 1
print(c)
