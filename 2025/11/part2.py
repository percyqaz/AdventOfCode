file = open("input.txt", encoding="utf-8")
data = file.read()
file.close()

devices = {}

for line in data.split("\n"):
    left, right = line.split(":")
    devices[left] = right.strip().split()

memo = {}

def explore_until_out(here, dac, fft):
    if "out" in devices[here]:
        return 1 if dac and fft else 0
    else:
        dac |= here == "dac"
        fft |= here == "fft"
        
        if (here, dac, fft) in memo:
            return memo[(here, dac, fft)]
        
        result = sum([explore_until_out(n, dac, fft) for n in devices[here]])
        memo[(here, dac, fft)] = result
        return result
    
print(explore_until_out("svr", False, False))