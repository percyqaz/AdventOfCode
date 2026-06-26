data = open("input.txt").read().split("\n")

nodes = {}
grid_size_x = 0
grid_size_y = 0
for line in data[2:]:
    split = line.split()
    while "" in split:
        split.remove("")
    used = int(split[2][:-1])
    avail = int(split[3][:-1])
    x, y = [int(z[1:]) for z in split[0].split("-")[-2:]]
    grid_size_x = max(x + 1, grid_size_x)
    grid_size_y = max(y + 1, grid_size_y)
    nodes[x,y] = { "used": used, "available": avail, "goal": False }

def can_move(x1,y1,x2,y2):
    source = nodes[(x1,y1)]
    if (x2, y2) in nodes:
        target = nodes[(x2,y2)]
        if target["available"] >= source["used"]:
            return True
        return False
    return False

def move(x1,y1,x2,y2):
    source = nodes[(x1,y1)]
    target = nodes[(x2,y2)]
    target["available"] -= source["used"]
    target["used"] += source["used"]
    source["available"] += source["used"]
    source["used"] = 0
    target["goal"] = source["goal"]
    source["goal"] = False

nodes[(grid_size_x - 1, 0)]["goal"] = True
sel_x = grid_size_x - 1
sel_y = 0

# exploratory code to view the board
# reveals that the puzzle is much simpler than it could be depending on numbers
while True:
    for y in range(grid_size_y):
        line = ""
        for x in range(grid_size_x):
            node = nodes[(x, y)]
            state = "G" if node["goal"] else ("#" if node["used"] else ".")
            if node["used"] > 100: state = "X"
            if (x, y) == (sel_x, sel_y):
                line += "{" + state + "}"
            else:
                line += " " + state + " "
        print(line)

    if can_move(sel_x, sel_y, sel_x - 1, sel_y):
        print("left ", end="")
    if can_move(sel_x, sel_y, sel_x, sel_y + 1):
        print("down ", end="")
    if can_move(sel_x, sel_y, sel_x, sel_y - 1):
        print("up ", end="")
    if can_move(sel_x, sel_y, sel_x + 1, sel_y):
        print("right ", end="")
    print()
    c = input()
    if c == "k" and sel_y > 0:
        sel_y -= 1
    elif c == "j" and sel_y + 1 < grid_size_y:
        sel_y += 1
    elif c == "h" and sel_x > 0:
        sel_x -= 1
    elif c == "l" and sel_x + 1 < grid_size_x:
        sel_x += 1
    elif c == "b":
        break

# 34 to get . in position ...
# then 1 to move G for the first time
# then 4 to reposition
# then 1 to move G for the second time
# then 4 to reposition
# then 1 to move G for the third time
# how many times must G move?
# TOTAL: 30 + 5*sel_x
print(30 + 5 * sel_x)
