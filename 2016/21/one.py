lines = open("input.txt").read().split("\n")

word = list("abcdefgh")

for line in lines:
    split = line.split()

    if split[1] == "position" and split[0] == "swap":
        a = int(split[2])
        b = int(split[-1])
        swap = word[a]
        word[a] = word[b]
        word[b] = swap

    elif split[1] == "letter":
        a = split[2]
        b = split[-1]
        index_a = word.index(a)
        index_b = word.index(b)
        word[index_a] = b
        word[index_b] = a

    elif split[1] == "positions":
        a = int(split[2])
        b = int(split[-1]) + 1
        word = word[0:a] + word[a:b][::-1] + word[b:]

    elif split[1] == "left":
        by = int(split[2]) % len(word)
        word = word[by:] + word[0:by]

    elif split[1] == "right":
        by = (len(word) - int(split[2])) % len(word)
        word = word[by:] + word[0:by]

    elif split[1] == "position" and split[0] == "move":
        a = int(split[2])
        b = int(split[-1])
        x = word.pop(a)
        word.insert(b, x)

    elif split[1] == "based":
        based_on = split[-1]
        index = word.index(based_on)
        by = (-1 - index - (1 if index >= 4 else 0)) % len(word)
        word = word[by:] + word[0:by]

    else:
        print("unrecognised", line)

print("".join(word))
