target = 3012210

current = [i + 1 for i in range(target)]

def step(current):
    index = len(current) // 2
    current.pop(index)
    current.append(current.pop(0))

while len(current) > 1:
    step(current)
print(current)

# tried writing a linked-list approach but it took longer to write and debug than for this to run

# concept: make a linked list of 1-TARGET
# track the "midpoint" (number to be deleted next), head and tail
# track the length
# each iteration move the head onto the tail
# each iteration delete the midpoint, then update to a new midpoint
# length is 1 less than before
# when the length is NOW even, new midpoint is old_midpoint.next.next
# otherwise it's old_midpoint.next
# repeat this O(1) step 3 million times until there is one number left
