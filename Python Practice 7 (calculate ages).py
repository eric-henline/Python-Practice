years_of_birth = [1990, 1991, 1990, 1990, 1992, 1996]
ages = [2021 - year for year in years_of_birth]
print(ages)


squares = []
squares = [x**2 for x in range(11)]
print(squares)


evens = [n for n in squares if n%2 == 0]
print(evens)


import random
numlist = []
list_length = random.randint(5,15)
while len(numlist) < list_length:
    numlist.append(random.randint(1,75))

evenlist = [n for n in numlist if n % 2 == 0]
print(numlist)
print(evenlist)
