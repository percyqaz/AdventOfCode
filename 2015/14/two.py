lines = [line.split() for line in open("input.txt").read().split("\n")]

def how_far(speed, duration, rest, time):
    period = duration + rest
    period_dist = speed * duration
    a = time // period * period_dist
    remainder = time % period
    b = period_dist if remainder >= duration else remainder * speed
    return a + b

reindeer = []
points = {}
for line in lines:
    name = line[0]
    speed = int(line[3])
    duration = int(line[6])
    rest = int(line[-2])
    reindeer.append([name, speed, duration, rest])
for t in range(2503):
    furthest = [] 
    furthest_dist = 0
    for r in reindeer:
        d = how_far(r[1],r[2],r[3],t + 1)
        if d > furthest_dist:
            furthest = [r[0]]
            furthest_dist = d
        elif d == furthest_dist:
            furthest.append(r[0])
    for f in furthest:
        if f not in points: points[f] = 0
        points[f] += 1

print(max([points[k] for k in points]))
