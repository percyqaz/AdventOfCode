# still seems familiar...
key = "ihaygndm"
import hashlib
i = 0
code = ""

chars = list("0123456789abcdef")

holding = {}
for c in chars: holding[c] = []

found = []

def stretch(x):
    for i in range(2017):
        x = hashlib.md5(x.encode()).hexdigest()
    return x

while len(found) < 80:
    digest = stretch(key + str(i))
    
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
print(sorted(found))
print(len(found))