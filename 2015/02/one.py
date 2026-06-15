lines = open("input.txt").read().split("\n")
print(sum([min(b) + 2*sum(b) for b in [[b[0] * b[1],b[1] * b[2],b[2] * b[0]] for b in [[int(x) for x in s.split("x")] for s in lines]]]))
