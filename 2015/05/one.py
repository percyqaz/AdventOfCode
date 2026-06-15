lines = open("input.txt").read().split("\n")
def is_nice(word):
    last_c = ' '
    v = 0
    rep = False
    for c in word:
        if c in "aeiou":
            v += 1
        if c == "b" and last_c == "a": return False
        if c == "d" and last_c == "c": return False
        if c == "q" and last_c == "p": return False
        if c == "y" and last_c == "x": return False

        if c == last_c: rep = True

        last_c = c
    return rep and v >= 3
print(len(list(filter(is_nice, lines))))
