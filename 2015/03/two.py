data = open("input.txt").read()
visited = {(0,0): 2}
x = [0,0]
y = [0,0]
who = 0
for c in data:
    if c == ">":
        x[who] += 1
    elif c == "<":
        x[who] -= 1
    elif c == "v":
        y[who] += 1
    elif c == "^":
        y[who] -= 1

    if (x[who], y[who]) not in visited:
        visited[(x[who], y[who])] = 0
    
    visited[(x[who], y[who])] += 1
    who = 1 - who
print(len(visited))
