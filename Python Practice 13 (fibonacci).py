fib_num = int(input("Please enter how many fibonacci numbers to generate: "))
print("Okay, here are the first", fib_num,
    "numbers in the fibonacci sequence:")


def fib_seq(x):
    fib_list = []
    a = 0
    b = 1
    while x != 0:
        c = a + b
        fib_list.append(c)
        b = a
        a = c
        x -= 1
    print(fib_list)


fib_seq(fib_num)
