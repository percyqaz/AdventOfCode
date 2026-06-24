# still seems familiar...
key = "ihaygndm"
import hashlib
i = 0
code = ""

chars = list("0123456789abcdef")

holding = {}
for c in chars: holding[c] = []

found = []

while len(found) < 64:
    digest = hashlib.md5((key + str(i)).encode()).hexdigest()
    
    for char in chars:
        if char * 5 in digest:
            for w in holding[char]: 
                if w not in found: 
                    found.append(w)
            holding[char] = [i]
        else:
            if char * 3 in digest:
                holding[char].append(i)
            while holding[char] and holding[char][0] + 1000 < i:
                holding[char] = holding[char][1:]
            
    i += 1
print(sorted(found)[-1])
