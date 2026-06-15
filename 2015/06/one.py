lines = [line.split() for line in open("input.txt").read().split("\n")]
lights = [[False] * 1000 for i in range(1000)]
for line in lines:
    if line[0] == "toggle":
        mode = lambda l: not l
    elif line[1] == "on":
        mode = lambda l: True
    else:
        mode = lambda l: False
    startx, starty = [int(x) for x in line[-3].split(",")]
    endx, endy = [int(x) for x in line[-1].split(",")]
    
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            lights[x][y] = mode(lights[x][y])
            
count = 0
for x in range(1000):
    for y in range(1000):
        if lights[x][y]: count += 1
print(count)