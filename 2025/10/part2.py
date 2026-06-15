import numpy
file = open("example.txt", encoding="utf-8")
data = file.read()
file.close()

puzzles = []

for line in data.split("\n"):
    parts = line.split()
    puzzle = {"buttons": []}
    for p in parts:
        if p[0] == "[":
            continue
        elif p[0] == "(":
            puzzle["buttons"].append([int(x) for x in p[1:-1].split(",")])
        else:
            puzzle["joltages"] = [int(x) for x in p[1:-1].split(",")]
    puzzles.append(puzzle)

total = 0
for puzzle in puzzles:
    matrix = [[1 if n in button else 0 for button in puzzle["buttons"]] for n in range(len(puzzle["joltages"]))]
    inverse = numpy.linalg.pinv(matrix)
    j = [[x] for x in puzzle["joltages"]]
    origin = numpy.matmul(inverse, j)
    gradient = numpy.identity(len(puzzle["buttons"])) - numpy.matmul(inverse, matrix)
    print(origin)
    for n in range(len(puzzle["buttons"])):
        one = [[0]] * len(puzzle["buttons"])
        one[n][0] = 1
        print(numpy.matmul(gradient, one))
        print(origin + numpy.matmul(gradient, one))
    print()

print(total)

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [0 0 0 0 1 1] [a] = [3]
# [0 1 0 0 0 1] [b]   [4]
# [0 0 1 1 1 0] [c]   [5]
# [1 1 0 1 0 0] [d]   [7]
#               [e]
#               [f]