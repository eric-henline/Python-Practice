x = range(2, 9)
for n in x:
    print(n)


num = int(input("Please enter a number greater than 10: "))
x = range(1, num + 1)
list = []
for i in x:
    if num % i == 0:
        list.append(i)
print("The divisors of your number are:", list)
