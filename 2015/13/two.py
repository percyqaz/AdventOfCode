lines = [line.split() for line in open("input.txt").read().split("\n")]
guests = {}
for line in lines:
    person = line[0]
    modifier = -1 if line[2] == "lose" else 1
    amount = int(line[3])
    neighbor = line[-1][:-1]
    if person not in guests:
        guests[person] = {}
    guests[person][neighbor] = amount * modifier

guests["Yourself"] = {}
for g in guests:
    guests[g]["Yourself"] = 0
    guests["Yourself"][g] = 0

def arrangements(current):
    if len(current) == len(guests):
        yield current
        return

    for g in guests:
        if g not in current:
            for a in arrangements(current + [g]):
                yield a

def happiness(arrangement):
    l = len(arrangement)
    happiness = 0
    for i in range(0, l):
        happiness += guests[arrangement[i]][arrangement[i - 1]]
        happiness += guests[arrangement[i]][arrangement[(i + 1) % l]]
    return happiness

print(max([happiness(arrangement) for arrangement in arrangements(["Alice"])]))
