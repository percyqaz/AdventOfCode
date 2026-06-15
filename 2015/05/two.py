lines = open("input.txt").read().split("\n")
def is_nice(word):
    lc = ' '
    llc = ' '
    p = 0
    ehe = False
    xxyy = False
    seen_digrams = {}
    for c in word:
        if c == llc: ehe = True
        if (lc + c) in seen_digrams:
            if p - seen_digrams[lc + c]  > 1:
                xxyy = True
        else:
            seen_digrams[lc + c] = p
        llc = lc
        lc = c
        p += 1
    return xxyy and ehe
print(len(list(filter(is_nice, lines))))
