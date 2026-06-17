# GENERAL RULE FOR COLUMN C and ROW R: (R^2 - 3R + 2CR + C^2 - C + 2) / 2
# Derived in a notepad from GCSE mathematics and sequences

# need (20151125 * 252533 ^ 18168397) % 33554393
#  252533 ^ n % 33554393 = ((252533 % 33554393) ^ n) % 33554393 for simpler calculation

row = 3010
col = 3019
code = (row * row - row*3 + 2*col*row + col * col - col + 2) // 2

# you can do a trick where you actually square c to double the power it's been raised to
# this was fast enough that I didn't bother
c = 20151125
b = 252533
m = 33554393
for i in range(code - 1):
	c *= b
	c %= m
print(c)
