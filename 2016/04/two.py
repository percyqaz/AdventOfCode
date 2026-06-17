lines = open("input.txt").read().split("\n")
m = 0
for line in lines:
    shift = int(line[-10:-7])
    o = ""
    for c in line[:-10]:
        if c.islower():
            o += chr((((ord(c) - ord('a')) + shift) % 26) + ord('a'))
    print(o, shift)

# python two.py | grep north