data = input(); i = 1; l = 0
for c in data:
    if c == ')': 
        l = l - 1
        if l < 0:
            print(i); break
    else: l = l + 1
    i = i + 1