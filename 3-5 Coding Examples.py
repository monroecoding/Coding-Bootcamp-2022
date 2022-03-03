"""
Coding Bootcamp at Monroe Township Library

3/5 Coding Examples
"""


#conditional statements (if, elif, else)

password_attempt = "admin123"
pin_attempt = "4321"

if password_attempt == "password123": #this statement is checked first, returns False
    print("Logged in with password") #this code block will not execute because condition is not True
elif pin_attempt == "1234": #this statement is checked because the first was False
    print("Logged in with PIN")
else:
    print("Invalid login") #this code will execute because all other statements were False


#conditional statements can be nested, check the outer if statment first, then the inner
if password_attempt == "admin123":
    if pin_attempt == "4321":
        print("Login successful!")


#use and, or, not to combine conditional statements
if password_attempt == "admin123" and pin_attempt == "4321":
    print("Login successful!") #requires BOTH statements to return True

if password_attempt == "admin123" or pin_attempt == "1234":
    print("Login successful!") #will print as long as EITHER statement is True

#checks conditional and then returns opposite value
#in this case (password == "password123") is False, returns True, so code in block is run
if not password_attempt == "password123":
    print("Incorrect password")


#while loops
index = 0

while index < 5: #while loops run until this condition is no longer met
    print(index)
    index += 1
#if the while condition never becomes False, it will run forever, creating an infinite loop


#for loops run through a specific set of data, we can create a range to have the
#for loop run a certain number of times
for i in range(5): #range takes a start and end, or just an end in which case it will start at 0
    print(i)

#you can use a for loop with any iterable data type; strings are iterable
for i in "hello":
    print(i)

#the break keyword jumps out of the loop as soon as it is reached
#the continue keyword will jump back to the start of the loop
#this loop will print only odd numbers between 0 and 10
new_index = 0

while True:
    if new_index == 10:
        break
    elif new_index % 2 == 0:
        new_index += 1
        continue

    print(new_index)
    new_index += 1