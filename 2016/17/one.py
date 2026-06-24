import hashlib
seed = "lpvhkcbi"
path = (0, 0, "")
paths = [path]
open_chars = "bcdef"
# UDLR

while True:
    new_paths = []

    def add_route(x, y, path):
        if x == 3 and y == 3:
            print(path)
            exit()
        new_paths.append((x, y, path))

    for x, y, route in paths:
        digest = hashlib.md5((seed + route).encode()).hexdigest()

        if y > 0 and digest[0] in open_chars:
            add_route(x, y - 1, route + "U")

        if y < 3 and digest[1] in open_chars:
            add_route(x, y + 1, route + "D")

        if x > 0 and digest[2] in open_chars:
            add_route(x - 1, y, route + "L")

        if x < 3 and digest[3] in open_chars:
            add_route(x + 1, y, route + "R")

    paths = new_paths
