""" Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first
and last elements of the given list. For practice, write this
code inside a function. """

a = [5, 10, 15, 20, 25]
print("List 'a' is: ", a)


def list_ends(xlist):
    new_list = []
    list_len = len(xlist)
    new_list.append(xlist[0])
    if xlist[list_len - 1] != xlist[0]:
        new_list.append(xlist[list_len-1])
    print("The end points of this list are:")
    print(new_list)


list_ends(a)


b = [7, 17, 55, 3, 9, 88, 67]
print("List 'b' is: ", b)

# OR this way

def list_ends2(xlist):
    return [xlist[0], xlist[len(xlist)-1]]


print(list_ends2(b))
