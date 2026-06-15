data = open("input.txt").read() + "\n"
negative = False
total = 0
num = 0
for c in data:
    d = ord(c) - ord('0')
    if c == "-":
        negative = True
    elif d >= 0 and d < 10:
        num *= 10
        num += d
    else:
        total += num * (-1 if negative else 1)
        num = 0
        negative = False
print(total)
