lines = open("input.txt").read().split("\n")
m = 0
for line in lines:

    lllc = " "
    llc = " "
    lc = " "
    sb = False
    babba = False
    gabba = False
    for c in line:
        if c == "[":
            sb = True
        elif c == "]":
            sb = False
        elif c == lllc and lc == llc and c != lc:
            if sb: babba = True 
            else: gabba = True
        lllc = llc
        llc = lc
        lc = c
    m += 1 if gabba and not babba else 0
print(m)