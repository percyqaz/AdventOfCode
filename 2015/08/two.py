data = open("input.txt").read()

quot = data.count("\"")
slash = data.count("\\")
linequot = len(data.split("\n")) * 2
print(sum([quot, slash, linequot]))