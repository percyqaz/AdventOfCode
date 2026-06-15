pwd = [ord(c) - ord('a') for c in "hxbxxyzz"]

def inc(i):
    if pwd[i] == 25:
        pwd[i] = 0
        inc(i - 1)
    else:
        pwd[i] += 1

def has_evil_letter():
    for c in pwd:
        if c == 8 or c == 14 or c == 11:
            return True
            
def has_straight():
    lc = -1
    llc = -1
    for c in pwd:
        if c == lc + 1 and c == llc + 2:
            return True
        llc = lc
        lc = c
    return False
    
def has_double_pair():
    seen_pair = 0
    lc = -1
    p = 0
    for c in pwd:
        if c == lc:
            if seen_pair and p - seen_pair > 1: 
                return True
            elif not seen_pair:
                seen_pair = p
        lc = c
        p += 1
        
while True:
    inc(-1)
    if has_evil_letter():
        continue
        
    if not has_straight():
        continue
        
    if not has_double_pair():
        continue
    
    print("".join([chr(c + ord('a')) for c in pwd]))
    break
# boring day, I didn't even get to try my optimisations for evil letters