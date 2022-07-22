# this is an example of reusable functions, where the text is changed
"""
def get_integer(new_text):
    return int(input(new_text))


age_integer = get_integer("Give a number: ")
# see here that the "new_text" is now "Give a number"
print(age_integer + 1)

# the "new_text" is the functions "argument"
# functions can also have a default argument while being open to custom ones


def get_integer(new_text="Please type a random number: "):
    return int(input(new_text))
# now the function will by default say "Please type a random number"


lucky_number = get_integer()
print("Your lucky number is ", lucky_number)

"""

# 11 is to ask a user for a number and determine if it is prime or not


def get_number(ask_text="Type a number of your choosing: "):
    return int(input(ask_text))


user_num = get_number()


def find_prime(num):
    divisors_list = []
    x = range(2, num)
    for i in x:
        if int(num % i) == 0:
            divisors_list.append(i)
    if divisors_list == []:
        print("Your number is a prime number!")
    else:
        print("Your number is not a prime number.  Here are its divisors:")
        print(divisors_list)


find_prime(user_num)

# use function find_prime to see if it is prime, else list the divisors
