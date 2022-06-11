"""
Coding Bootcamp at the Monroe Township Library

5/26 Project

Password Generator/Validator
Create a simple tool that can randomly generate secure passwords or
check an input password to see if it's secure

The criteria we'll use for a secure password is:
    -Must be at least 12 characters long
    -Must contain at least 1 of each (letter, number, symbol)

When generating a password we'll randomly select 8 letters, 2 numbers, and 2 symbols
String constants containing the available characters have already been created
You'll need to complete the helper functions generate_password() and check_password()
"""

import string
import random

ALPHABET = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*"


def generate_password():
    """
    randomly generates a secure password using letters, numbers, and symbols

    returns string -- 12 char secure password
    """
    pass


def check_password(password):
    """
    password {string} -- password to be verified
    
    returns bool -- True if password is >= 12 chars
    and has at least 1 letter, number, and symbol, otherwise False
    """
    pass


def main():
    """
    main function, user can either generate a secure password,
    or check if a password is secure
    """

    print("Secure password generator/validator")
    print("-------")

    while True:
        command = input("Do you want to (g)enerate or (v)alidate a password?: ").lower()

        if command == "g":
            new_password = generate_password()
            print(f"Password: {new_password}")
            break

        elif command == "v":
            password = input("Enter the password to check: ")

            if check_password(password) == True:
                print("Secure password")
            else:
                print("Password not secure")
            break


if __name__ == "__main__":
    main()