REAL = True
seed = 1352 if REAL else 10

def is_free(x, y):
    p = x*x + 3*x + 2*x*y + y + y*y
    p += seed

    bits = 0
    while p:
        bits += p % 2
        p //= 2
    return bits % 2 == 0

wall_cache = {}
def is_free_cached(x, y):
    if x < 0 or y < 0: return False

    if (x, y) not in wall_cache:
        wall_cache[(x, y)] = is_free(x, y)
    return wall_cache[(x, y)]

target = (31, 39) if REAL else (7,4)
heads = [(1, 1)]

already_seen = set()
next_heads = []

def explore(x, y):
    if (x, y) in already_seen: return

    if is_free_cached(x, y):
        already_seen.add((x, y))
        next_heads.append((x, y))

for gen in range(50):
    for x, y in heads:
        explore(x + 1, y)
        explore(x, y + 1)
        explore(x - 1, y)
        explore(x, y - 1)
    heads = next_heads
    next_heads = []
    print(len(already_seen))
