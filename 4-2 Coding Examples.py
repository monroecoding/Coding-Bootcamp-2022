"""
Coding Bootcamp at Monroe Township Library

4/2 Coding Examples
"""


#define a function using the def keyword, a name, and arguments
def say_hello():
    print("Hello!")

#functions don't run unless they are called
say_hello()


#functions can take arguments, which are passed into the function when it is called
def add_numbers(num1, num2):
    print(num1 + num2)

#we can call a function multiple times and pass in different arguments each time
add_numbers(3,4)
add_numbers(6,7)


#the return keyword allows your function to return a value which can be used or saved as a variable
#a function with no return statement will return None
#once the function reaches a return statement, it jumps out of the function block
def square(num):
    return num ** 2
    print("This will not print!")

#function is called and passed an argument, runs function and saves result to variable
num_squared = square(3)
print(num_squared)


#you can set a default argument that will be used if no other argument is passed
def greeting(name="friend"):
    print(f"Hello, {name}!")

greeting("Amy") #when given an argument, will override the default value
greeting() #calling the function without the argument is also fine, it will use the default


#you can define a function to accept an unspecified amount of arguments using an * before the argument name
def multiple_args(*args):
    print(args)

multiple_args(3,4,5,6) #there is no limit on the number of arguments we can pass in

#an example of a function that takes an unspecified amount of arguments and prints their sum
def sum_numbers(*nums): 
    print(sum(nums))

sum_numbers(3,4,5,6)


#functions can also accept an unspecified amount of keyword arguments using a double asterisk **
def keyword_args(**kwargs):
    print(kwargs)

keyword_args(name="Harry Potter", age=18) #kwargs are entered as a dictionary of key: value pairs

#example of a function for printing concert tickets, if row and seat numbers are provided they print on ticket
#if not provided we just issue a general admission ticket
#first argument is required, kwargs are not
def print_ticket(number, **kwargs):
    print(f"Ticket number: {number}")

    row = kwargs.get("row")
    seat = kwargs.get("seat")

    if row == None or seat == None:
        print("General Admission")
    else:
        print(f"Row: {row}, Seat: {seat}")

print_ticket(34)
print_ticket(35, row="C", seat=8)




