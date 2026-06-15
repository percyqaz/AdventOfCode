lines = [line.split() for line in open("input.txt").read().split("\n")]
ingredients = [] 
for line in lines:
    ingredient = line[0][:-1]
    capacity = int(line[2][:-1])
    durability = int(line[4][:-1])
    flavor = int(line[6][:-1])
    texture = int(line[8][:-1])
    calories = int(line[10])
    ingredients.append({"c": capacity, "d": durability, "f": flavor, "t": texture, "cal": calories})

def split(n, remaining, current):
    if n == 1:
        yield current + [remaining]
        return

    for i in range(0, remaining + 1):
        for s in split(n - 1, remaining - i, current + [i]):
            yield s
            
def eval_split(s):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i in range(len(s)):
        capacity += s[i] * ingredients[i]["c"]
        durability += s[i] * ingredients[i]["d"]
        flavor += s[i] * ingredients[i]["f"]
        texture += s[i] * ingredients[i]["t"]
        calories += s[i] * ingredients[i]["cal"]
    if calories != 500: return -1
    return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

print(max([eval_split(s) for s in split(len(ingredients), 100, [])]))
