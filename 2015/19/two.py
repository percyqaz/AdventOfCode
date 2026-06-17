_, target_molecule = open("input.txt").read().split("\n\n")

target_molecule = target_molecule.replace("Y", ",").replace("Rn", "(").replace("Ar", ")")
print(target_molecule)

# idea: using HINT: What if Rn = '(', Y = ',', Ar = ')'
# EVERY RULE can be treated as taking 1 element and generating 2, as long as we stop counting brackets as elements
# Hence if we count the elements in the string and subtract 1, that = steps (we started with 1 e)
# One catch: Some rules look like i.e C(F,F,F) which is 3 or 4 elements instead of 2!
# But if you count commas (Ys originally) as -1, then these rules also "count" like they make 2 elements from 1

# Code below: Count capital letters (number of elements)
# Ar and Rn do not count as they are ( )
# Subract count of Y as they are ,
# Count starts at -1 to compensate for starting with 1 element already
# End of loop: Count is number of steps we have to have taken to generate the molecule

count = -1
for c in target_molecule:
    if c.isupper():
        count += 1
    if c == "(" or c == ")": continue
    if c == ",":
        count -= 1
print(count)