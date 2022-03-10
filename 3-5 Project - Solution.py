"""
Coding Bootcamp at the Monroe Township Library

3/5 Project

Create an interactive game of rock, paper, scissors. The program should take user input and
the computer will generate a pick randomly. Print to the terminal whether the user wins, loses, or ties.

Things to consider:
    -make sure your program accounts for the user inputting something other than one of the 3 choices
    -you might also want to consider accounting for case (Rock or ROCK could still be valid inputs)
    -you could also print out the computer's pick to make sure your program is working correctly

Test cases:
    input -> rock
    computer_pick -> rock
    output -> Tie!

    input -> paper
    computer_pick -> scissors
    output -> You lose!

    input -> rock
    computer_pick -> scissors
    output -> You win!

    input -> hello
    output -> Not a valid option

If you want an additional challenge, keep the game running until the user wins. (Hint: use a loop)
"""


# getting the computer's randomly generated pick
# you don't need to understand this code right now, just use the computer_pick variable in your code
import random

options = ["rock", "paper", "scissors"]
computer_pick = random.choice(options)


while True:
    print("-----")
    user_pick = input("Choose rock, paper, or scissors: ").lower()

    if user_pick == computer_pick:
        print(f"Computer chose {computer_pick}")
        print("Tie!")
    
    elif user_pick == "rock":
        if computer_pick == "scissors":
            print(f"Computer chose {computer_pick}")
            print("You win!")
            break
        elif computer_pick == "paper":
            print(f"Computer chose {computer_pick}")
            print("You lose!")

    elif user_pick == "paper":
        if computer_pick == "scissors":
            print(f"Computer chose {computer_pick}")
            print("You lose!")
        elif computer_pick == "rock":
            print(f"Computer chose {computer_pick}")
            print("You win!")
            break

    elif user_pick == "scissors":
        if computer_pick == "paper":
            print(f"Computer chose {computer_pick}")
            print("You win!")
            break
        elif computer_pick == "rock":
            print(f"Computer chose {computer_pick}")
            print("You lose!")
    
    else:
        print("Not a valid option")
