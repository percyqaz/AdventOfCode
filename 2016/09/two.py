data = open("input.txt").read().strip()
def dlength(data):
    c = 0
    while data:
        if data[0] == "(":
            s = data[1:].split(")")
            a, b = [int (x) for x in s[0].split("x")]
            c += dlength(")".join(s[1:])[:a]) * b
            data = ")".join(s[1:])[a:]
        else:
            c += 1
            data = data[1:]
    return c
print(dlength(data))
