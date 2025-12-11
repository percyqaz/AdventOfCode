file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

devices = {}

for line in data.split("\n"):
    left, right = line.split(":")
    devices[left] = right.strip().split()

def explore_until_out(here):
    if "out" in devices[here]:
        return 1
    else:
        return sum([explore_until_out(n) for n in devices[here]])
    
print(explore_until_out("you"))