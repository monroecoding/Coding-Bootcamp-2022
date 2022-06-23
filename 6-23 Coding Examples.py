"""
Coding Bootcamp at the Monroe Township Library

6/11 Code Examples
"""


#the data types we've been using are members of classes
string = "hello" #when we create a string, we are really creating an instance of the str class
print(string.find("e")) #find() is a method defined in the str class


#defining a new class
class Book:
    def __init__(self, title, author): #init method is called whenever a new instance is created
        self.title = title #self refers to the actual instance of the class
        self.author = author
        self.available = True #can also define variables that are not passed in as arguments

    def check_out(self): #define class methods that can be called on instances of this class
        self.available = False


#create a new instance of a class by using the class name and passing in arguments to the init method
new_book = Book("The Hobbit", "JRR Tolkien")

print(new_book.title) #attributes of the object can be accessed using dot notation
new_book.check_out() #methods can be called using dot notation
print(new_book.available)


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y})"


#create 2 separate coordinate objects
coords1 = Coordinates(1,2)
coords2 = Coordinates(3,4)

#using default __add__ functionality, adding these together will throw an error
print(coords1 + coords2) #since the functionality for __add__ is defined in the class, it uses that definition instead
print(coords1 == coords2)

print(coords1) #passing an object to the print function uses its defined __str__ method


#classes can inherit from other classes, in this example 'Employee' is the parent class
class Employee:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = f"{str(Employee.id).zfill(3)}"
        self.access = False
        Employee.id +=1

    def print_badge(self):
        print("-------")
        print(self.name)
        print(self.id)
        print("-------")


#TechSupport inherits from the Employee class, all properties and methods from that class are available to this class
class TechSupport(Employee):
    #the super() function gets the parent class so we can call the same __init__ function without having to implement it twice
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def grant_access(self):
        if self.level == "senior":
            self.access = True


employee = TechSupport("Jo", "senior")

#we can still call print_badge() even though it's not defined in TechSupport class because it is defined in parent class
employee.print_badge()
employee.grant_access()
print(employee.access)