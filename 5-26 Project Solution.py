"""
Coding Bootcamp at the Monroe Township Library

5/14 Project

Hangman
A simplified game of hangman where the user has 5 guesses to pick the correct letters of
a randomly selected word

You will need to complete 4 helper functions so that the main() function runs properly
First, you need to access the text file 'word_list' to return a list of all possible words
then choose one of the words randomly from that list

Next you'll need functions that check if the user has guessed the word correctly
and if not, you want to display which letters are correct

Things to remember:
    -Use the 'with' keyword when working with files, otherwise don't forget to close file manually
    -Remember that line breaks '\n' are included when reading text files
    -You can use the 'in' keyword to check if an element is present in an iterable (list, tuple, str, etc.)
    -Use for loops to cycle through an iterable
    -If you want to test individual functions, just comment out the if name == main block

Feel free to refactor the code however you want if it makes it easier for you!
"""

import random
import string


def get_word_list():
    """
    this function should access the 'word_list' text file
    and return all words in the file as a list which can be used to select
    a random word for the game
    """

    with open("word_list.txt", "r") as file:
        words = file.readlines()

    return words


def choose_word(word_list):
    """
    word_list {list} -- of ~5000 five-letter words

    returns string -- randomly selected word from list
    """
    
    word = random.choice(word_list)
    return word[0:5]


def check_guess(word, user_guess):
    """
    word {string} -- correct word
    user_guess {list of strings} -- all letters guessed by user

    returns bool -- True if word contains all letters guessed by user
    otherwise False
    """

    #complete this function
    for letter in word:
        if letter not in user_guess:
            return False
    
    return True


def display_letters(word, user_guess):
    """
    word {string} -- correct word
    user_guess {list of strings} -- all letters guessed by user

    returns string -- representation of correct letters guessed
    correct letters will be visible, otherwise shows an underscore e.g.: "h_ll_"
    """

    display = ""

    for letter in word:
        if letter in user_guess:
            display += letter
        else:
            display += "_"

    return display


def main():
    """
    main game loop, user gets 5 tries to guess the correct word
    asks for user input, a single letter time
    After each guess, checks if user has the correct word, if not displays current correct letters
    keeps track of available letters, and letters guessed
    """

    print("Welcome to Hangman")
    print("You have 5 tries to guess a 5-letter word")

    word = choose_word(get_word_list())

    tries = 5
    available_letters = list(string.ascii_lowercase)
    letters_guessed = []

    while tries > 0:
        print("-------")
        print(f"You have {tries} guesses remaining...")
        print(f"Available letters: {available_letters}")

        guess = input("Enter a letter: ").lower()

        if guess not in available_letters:
            print("Invalid guess")
            continue
            
        else:
            available_letters.remove(guess)
            letters_guessed.append(guess)

            if check_guess(word, letters_guessed) == True:
                print("-------")
                print(f"You got it! Correct word: {word}")
                break
            else:
                print(display_letters(word, letters_guessed))
                tries -= 1

    print("-------")
    print(f"Out of tries, correct word: {word}")


if __name__ == "__main__":
    main()