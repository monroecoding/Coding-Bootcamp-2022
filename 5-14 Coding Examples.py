"""
Coding Bootcamp at the Monroe Township Library

5/14 Coding Examples
"""


#scope, in Python, refers to the availabilty of variables

global_var = 20 #variables created outside of functions are in the global scope

def print_global():
    print(global_var) #we can access the value of a global variable inside a function


def create_local():
    local_var = 5 #this variable is only accessible inside of this function

#print(local_var) #trying to access a local variable outside of scope will throw an error


#creating a local variable with the same name DOES NOT override the global variable's value
#global_var inside the function is treated as a completely separate variable
def new_var():
    global_var = 5
    print(global_var)

new_var() #prints 5, the value of 'global_var' in the function
print(global_var) #prints 20, the value of 'global_var' as defined in the global scope


#we can read and write text files with Python using the 'open' function
#to use 'open', pass in the name of the file you want to access, and a letter representing what
#you want to do with the file (r for read, w for write, a for append)
file = open("test.txt", "w") #if the file does not already exist, it will be created when opening with 'write'

file.write("Hello World\n") #we can pass a string to add a single line of text
new_lines = ["line1\n", "line2\n", "line3\n"]
file.writelines(new_lines) #use writelines to pass in a bunch of text as a list

file.close() #make sure to close the file when you are finished with it

#you can use the 'with' keyword to do all file handling in one block of code
with open("test.txt", "r") as file:
    lines = file.readlines() #use readlines to return a list where each line is an element
    print(lines)
    #file will close automatically at the end of the block

#using append mode will only add text to the end of the file instead of overwriting
with open("test.txt", "a") as file:
    file.write("line4")


#the import keyword allows you to import python modules and use functions, classes, and variables defined in them

import random #random is a module in the Python standard library

print(random.randint(1, 9)) #use dot notation to access module functions

from math import sqrt, floor #you can import just specific components from a module

print(floor(sqrt(90))) #you do not need to use dot notation when you import the functions by name