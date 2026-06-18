data = open("input.txt").read().split("\n")
screen = [[False] * 50 for i in range(6)]
for line in data:
    s = line.split()
    if s[0] == "rect":
        w,h = [int(x) for x in s[1].split("x")]
        for y in range(h):
            for x in range(w):
                screen[y][x] = True
    elif s[1] == "column":
        col = int(s[2][2:])
        by = int(s[-1])
        new_column = [screen[(i - by) % 6][col] for i in range(6)]
        for i in range(6):
            screen[i][col] = new_column[i]
    elif s[1] == "row":
        row = int(s[2][2:])
        by = len(screen[0]) - int(s[-1])
        screen[row] = screen[row][by:] + screen[row][:by]
print("\n".join(["".join(["#" if s else "." for s in line]) for line in screen])) # debugging revealed part 2
print(sum([sum([1 if s else 0 for s in line]) for line in screen])))
