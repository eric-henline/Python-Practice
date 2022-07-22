import random
num_try = 1
while True:
    x = random.randint(1, 9)  # this includes 1 and 9
    user_guess = int(input("Game: Guess a number between 1 and 9 (inclusive):"))
    if user_guess == x:
        print("Your guess was exactly correct!")
    elif user_guess > x:
        print("Your guess was too high!")
    else:
        print("Your guess was too low!")
    user_play = input("Would you like to play againt? y/n: ")
    if user_play == "n":
        print("You played the game", num_try, "time(s). Goodbye!")
        break
    else:
        num_try += 1
        print("This is your try number: ", num_try)
