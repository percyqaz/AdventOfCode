data = open("input.txt").read()
visited = {(0,0): 1}
x = 0
y = 0
for c in data:
    if c == ">":
        x += 1
    elif c == "<":
        x -= 1
    elif c == "v":
        y += 1
    elif c == "^":
        y -= 1

    if (x, y) not in visited:
        visited[(x, y)] = 0
    
    visited[(x, y)] += 1

print(len(visited))
