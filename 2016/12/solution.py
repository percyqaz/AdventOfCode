# equivalent python code to the assembunny I was given, by reasoning

a = 1
b = 1
c = 1 # if in part 1 set to 0
d = 26

if c:
	c = 7
	d += c
	
# calculates fibonacci, reason it yourself
while d:
	c = a
	a += b
	b = c
	d -= 1
	
# after d steps...
# a started as f(2) and b as f(1)
# a is now f(2 + d) https://planetmath.org/listoffibonaccinumbers

# a is 317811 from link

c = 16
d = 12
a += d * c

print(a)