lines = [line.split() for line in open("input.txt").read().split("\n")]
pointer = 0
reg = { "a": 1, "b": 0 }

while pointer < len(lines):

    instruction = lines[pointer]
    if instruction[0] == "inc":
        reg[instruction[1]] += 1
        pointer += 1
    elif instruction[0] == "hlf":
        reg[instruction[1]] //= 2
        pointer += 1
    elif instruction[0] == "tpl":
        reg[instruction[1]] *= 3
        pointer += 1
    elif instruction[0] == "jmp":
        pointer += int(instruction[1])
    elif instruction[0] == "jio":
        if reg[instruction[1][0]] == 1:
            pointer += int(instruction[2])
        else:
            pointer += 1
    elif instruction[0] == "jie":
        if reg[instruction[1][0]] & 1 == 0:
            pointer += int(instruction[2])
        else:
            pointer += 1
    else:
        raise Exception("Don't recognise " + " ".join(instruction))

print(reg)
