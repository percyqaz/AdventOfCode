line = open("input.txt").read()

safe = 0
combos = ["^..", "^^.", "..^", ".^^"]

def next_line(line):
    global safe
    result = ""
    padded = "." + line + "."
    for i in range(len(line)):
        x = padded[i:i+3]
        if line[i] == ".": safe += 1
        if x in combos:
            result += "^"
        else:
            result += "."
    return result

for i in range(40):
    line = next_line(line)
print(safe)
