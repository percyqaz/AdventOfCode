start = 1
end = 3012210
step = 1

def count():
    return (end - start) // step + 1

while start != end:
    is_even = count() % 2 == 0
    if is_even:
        end -= step
        step *= 2
    else:
        step *= 2
        start += step
print(start)
