numbers = sorted([int(x) for x in open("input.txt").read().split("\n")])[::-1]
target = sum(numbers) // 3

def greedy(numbers, current, p, target):
    if target == 0:
        yield p, current
        return

    ncopy = list(numbers)
    for n in numbers:
        ncopy.remove(n)
        if n <= target:
            for o in greedy(ncopy, current + [n], p * n, target - n):
                yield o

group_ones = sorted(list(greedy(numbers, [], 1, target)))
for w, group in group_ones:
    ncopy = list(numbers)
    for n in group: ncopy.remove(n)
    for o in greedy(ncopy, [], 1, target):
        print(w)
        exit()
