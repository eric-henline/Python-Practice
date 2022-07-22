x = input("Please enter a string: \n")
print(x[:])
print(x[::-1])
if x[:] == x[::-1]:
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome.")
