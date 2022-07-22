while True:
    start_input = input("Would you like to play? y/n:")
    if start_input == "y":
        print("Let's play rock, paper, scissors.")
        incorrect_answer = ("Incorrect input:  Please type r, p, or s:")
        correct_answers = ["rock", "paper", "scissors"]

        p1_answer = input("Player 1 - Please type rock, paper, or scissors:")
        while p1_answer not in correct_answers:
            p1_answer = input(incorrect_answer)

        p2_answer = input("Player 2 - Please type rock, paper, or scissors:")
        while p2_answer not in correct_answers:
            p2_answer = input(incorrect_answer)

        p1win = str("Player 1 wins!")
        p2win = str("Player 2 wins!")

        def compare(p1, p2):
            if p1 == p2:
                return("It's a tie!")
            elif p1 == "rock":
                if p2 == "scissors":
                    return(p1win + " " + p1_answer + " beats " + p2_answer + "!")
                else:
                    return(p2win + " " + p2_answer + " beats " + p1_answer + "!")
            elif p1 == "paper":
                if p2 == "rock":
                    return(p1win + " " + p1_answer + " beats " + p2_answer + "!")
                else:
                    return(p2win + " " + p2_answer + " beats " + p1_answer + "!")
            elif p1 == "scissors":
                if p2 == "paper":
                    return(p1win + " " + p1_answer + " beats " + p2_answer + "!")
                else:
                    return(p2win + " " + p2_answer + " beats " + p1_answer + "!")
            else:
                return

        print(compare(p1_answer, p2_answer))

    elif start_input == "n":
        print("Goodbye.")
        break
    else:
        print("Invalid input.  Please try again:")

# use xxx = ''' to comment out blocks of code
