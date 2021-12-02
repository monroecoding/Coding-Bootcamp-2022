"""
Coding Bootcamp at Monroe Township

2/17 Coding Examples
"""

#getting user input

word = input("Enter a word: ")
print(word)


#ints and floats, perform basic math operations

print("\nInt and float examples: ")

print(5 + 5.0) #any operation including a float returns a float
print(5 / 5) #float division
print(5 // 2) #floor/int division, if there is decimal it will round down
print(5 + 3 * 6 / 3 - 2) #PEMDAS order of operations
print(5 % 2) #modulus, returns remainder


#strings

print("\nString examples: ")

word = "Hello World"

print(len(word)) #gives the length of a string (number of characters)
print(word[1]) #string indexing, starts from 0
print(word.count("l")) #counts the number of times something appears in a string
print(word.lower()) #turns all characters to lowercase
print(word.upper()) #turns all character to uppercase
print(word.find("e"))

first_name = "John"
last_name = "Smith"

print(first_name + last_name) #you can join string using concatenation
print("First name is " + first_name + ", last name is " + last_name)
#formatted strings allow you to concatenate in a more readable way
print(f"First name is {first_name}, last name is {last_name}")


#booleans

print("\nBoolean examples: ")

#aside from using bools True and False, other data types have 'truthy' or 'falsey' values
print(bool("")) #empty strings are 'falsey'
print(bool("Hello world")) #non-empty strings are 'truthy'
print(bool(0)) #0 is 'falsey'
print(bool(23)) #every other number is 'truthy'
print(bool(None)) #NoneTypes are 'falsey'


#type conversion, these are all valid type conversions
int("123")
str(3.14)
bool(None)
float(9)
int(True)


#not valid conversions
"""
int("hello world")
float("apple")
"""