lines = [line.split() for line in open("input.txt").read().split("\n")]

def how_far(speed, duration, rest, time):
    period = duration + rest
    period_dist = speed * duration
    a = time // period * period_dist
    remainder = time % period
    b = period_dist if remainder >= duration else remainder * speed
    return a + b

furthest = 0
for line in lines:
    speed = int(line[3])
    duration = int(line[6])
    rest = int(line[-2])
    furthest = max(furthest, how_far(speed,duration,rest,2503))

print(furthest)
