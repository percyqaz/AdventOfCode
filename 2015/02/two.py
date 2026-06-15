lines = open("input.txt").read().split("\n")
print(sum([min(b["f"])*2 + b["v"] for b in [{"f": [b[0] + b[1], b[1] + b[2], b[2] + b[0]], "v": b[0] * b[1] * b[2]} for b in [[int(x) for x in s.split("x")] for s in lines ]]]))
