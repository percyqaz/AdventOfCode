file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

puzzles = []

for line in data.split("\n"):
    parts = line.split()
    puzzle = {"buttons": []}
    for p in parts:
        if p[0] == "[":
            puzzle["target"] = int("".join(["1" if c == "#" else "0" for c in p[1:-1][::-1]]), base=2)
        elif p[0] == "(":
            puzzle["buttons"].append(sum([2 ** n for n in [int(x) for x in p[1:-1].split(",")]]))
        else:
            puzzle["joltages"] = [int(x) for x in p[1:-1].split(",")]
    puzzles.append(puzzle)

def combos(buttons):
    if len(buttons) == 0:
        yield (0, 0)
    else:
        for v, count in combos(buttons[1:]):
            yield (v ^ buttons[0], count + 1)
            yield (v, count)

total = 0
for puzzle in puzzles:
    m = 9999999999
    for v, count in combos(puzzle["buttons"]):
        if v == puzzle["target"]:
            m = min(m, count)
    total += m

print(total)