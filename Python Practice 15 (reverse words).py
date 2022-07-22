str1 = str(input("Please enter a string of multiple words:"))
print(str1)
# make a function that prints the string in reverse order


def reverse_v1():
    y = str1.split()
    result = []
    for word in y:
        result.insert(0,word)
    return " ".join(result)


print(reverse_v1())
