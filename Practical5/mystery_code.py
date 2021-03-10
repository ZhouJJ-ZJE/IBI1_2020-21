# What does this piece of code do?
# Answer:Randomly generate numbers that greater than 1 and no larger than 50.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4rm -rf.2)=5
from math import ceil

# randomly generarte numbers from 1 to 100 and only numbers no larger than 50 can be printed.
p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
