# equivalent python code to my puzzle input, obtained by hand-decompilation and simplifying

a = 158 # solution

d = a
c = 4
b = 643
d += b * c
while True:
	a, b = a // 2, a % 2
	print(b)
	if not a: a = d
	
# from the code, we want d to have a binary form of 1010101010.....
# d = <solution we seek> + 2572
# smallest binary number satisfying this is 2730 = 1010 1010 1010
# so if a = 158 then d = 158 + 2572 = 0b101010101010
# causing algorithm to output that pattern as desired