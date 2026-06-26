maze = open("input.txt").read().split("\n")

def find(char):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == char:
                return (x, y)

def path(source, target):
    target_x, target_y = find(target)
    source_x, source_y = find(source)

    seen = set()
    heads = [(source_x, source_y)]
    depth = 0
    while (target_x, target_y) not in heads:
        new_heads = []
        def explore(x, y):
            if (x, y) in seen:
                return
            if maze[y][x] != "#":
                seen.add((x, y))
                new_heads.append((x, y))

        for x, y in heads:
            explore(x + 1, y)
            explore(x - 1, y)
            explore(x, y + 1)
            explore(x, y - 1)

        heads = new_heads
        depth += 1
    return depth

output = open("graph.txt", "w+")
for a in range(0, 8):
    for b in range(a + 1, 8):
        sa = str(a)
        sb = str(b)
        dist = path(sa, sb)
        output.write(sa + " <-> " + sb + " = " + str(dist) + "\n")
output.close()
