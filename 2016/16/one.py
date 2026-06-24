seed = "01110110101001000"
length = 272

def dragon(s):
    return s + "0" + "".join(["0" if c == "1" else "1" for c in s[::-1]])

def halve(s):
    result = ""
    for i in range(0, len(s), 2):
        if s[i] == s[i + 1]: result += "1"
        else: result += "0"
    return result

while len(seed) < length:
    seed = dragon(seed)
seed = seed[0:length]

while len(seed) % 2 == 0:
    seed = halve(seed)
print(seed)
