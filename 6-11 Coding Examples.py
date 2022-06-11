"""
Coding Bootcamp at the Monroe Township Library

5/26 Code Examples
"""

import this #imports the 'Zen of Python'


#use try and except keywords to handle expected exceptions
try:
    number = input("Please input a whole number: ") 
    number = int(number) #normally if the user's input can't be converted to an int, the program would crash
except:
    print("Not a whole number") #when the code in the try block encounters an exception, it will run this code instead


try:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = int(num1) / int(num2)
    print(result)

except ValueError: #it is good practice to specify which exceptions you are handling
    print("Not a number")

except ZeroDivisionError: #you can include multiple except statements for different errors
    print("Cannot divide by zero")

finally:
    print("-------") #this code will execute at the end of the block regardless of if errors were encountered


#docstrings go at the top of your function and should explain what (if any) arguments are required
#what data type the args should be, what the function returns, etc.
def combine_words(word1, word2):
    """
    Arguments:
        word1 {string} -- first part of word
        word2 {string} -- second part of word

    Returns:
        string -- Combined word
    """

    return word1 + word2


#list comprehensions are a shorthand way of creating lists
word = "hello"
letters = [letter for letter in word] #the letter variable will get appended to the new list at each step of the loop

#you can also give conditions for list comprehensions
even_numbers = []

for num in range(10):
    if num % 2 == 0:
        even_numbers.append(num)

#the code above can be done in a single line with a list comprehension
evens = [num for num in range(10) if num % 2 == 0]


#you can 'unpack' the contents of a list or tuple and save them as separate variables
file = "file.txt"
parts_of_file = file.partition(".") #partition is a string method that returns a tuple of strings, split by the argument given

#this creates 3 new variables separated by commas and assigns the value of that index in the tuple
name, _, file_type = parts_of_file #it is convention to use an underscore for vars you don't need

print(file_type)