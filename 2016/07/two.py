lines = open("input.txt").read().split("\n")
m = 0
for line in lines:
    llc = " "
    lc = " "
    sb = False
    inside = set()
    outside = set()
    for c in line:
        if c == "[":
            sb = True
        elif c == "]":
            sb = False
        elif c == llc and c != lc:
            if sb: inside.add(lc + c)
            else: outside.add(c + lc)
        llc = lc
        lc = c
    for i in inside:
        if i in outside:
            m += 1
            break
print(m)