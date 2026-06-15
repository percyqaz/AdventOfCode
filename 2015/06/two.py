lines = [line.split() for line in open("input.txt").read().split("\n")]
lights = [[0] * 1000 for i in range(1000)]
for line in lines:
    if line[0] == "toggle":
        mode = lambda l: l + 2
    elif line[1] == "on":
        mode = lambda l: l + 1
    else:
        mode = lambda l: max(0, l - 1)
    startx, starty = [int(x) for x in line[-3].split(",")]
    endx, endy = [int(x) for x in line[-1].split(",")]
    
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            lights[x][y] = mode(lights[x][y])
            
count = 0
for x in range(1000):
    for y in range(1000):
        count += lights[x][y]
print(count)