data = open("input.txt").read()

l = len(data)
data = data.replace("\\\\", "*")
dslash = l - len(data)
data = data.replace("\\\"", "*")
quot = l - len(data) - dslash
linequot = len(data.split("\n")) * 2
xslash = data.count("\\x") * 3
print(sum([dslash, quot, linequot, xslash]))