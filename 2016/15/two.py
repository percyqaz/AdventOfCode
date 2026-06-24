discs = open("input.txt").read().split("\n")

disc_n = 0

current = 0
step = 1

def handle_disc(count, rem):
    global current
    global step
    
    while current % count != rem:
        current += step
    
    step *= count

for disc in discs:
    disc_n += 1
    split = disc.strip(".").split()
    count = int(split[3])
    init = int(split[-1])
    
    rem = -(init + disc_n) % count
    
    print("i mod %s = %s" % (count, rem))
    
    handle_disc(count, rem)
    
handle_disc(11, -(disc_n + 1) % 11)
    
print(current)