"""
Coding Bootcamp at Monroe Township Library

3/17 Coding Examples
"""


#lists hold values of any data type, separated by comma
#lists are mutable which means the contents of the list can be changed

print("List examples:")
number_list = [1, 2, 3]
fruit_list = ["apple", "orange", "banana"]

print(fruit_list[1]) #get individual element of a list with indexing (starts with 0)

fruit_list[1] = "lemon"
print(fruit_list) #we can change individual elements using assignment

for i in fruit_list: #lists are iterable, we can use for loop to go through each element
    print(i)

#some important list methods
fruit_list.append("cherry") #append adds a new element to the end of the list
print(f"Length: {len(fruit_list)}") #returns the number of elements in a list
copied_list = fruit_list.copy() #creates a copy of the list
fruit_list.pop(2) #removes element from the list by index, if no index is given it will remove the last element
fruit_list.remove("apple") #removes a specific element

print(fruit_list)
print(copied_list)


#tuples work similarly to lists but is immutable, meaning the data inside cannot be changed

print("\nTuple Examples:")
weekend = ("Saturday", "Sunday")

print(weekend[1]) #you can get values by indexing but trying to change will give you an error
#weekend[1] = "Monday" would throw a TypeError

#some important tuple methods
print(weekend.count("Saturday")) #counts the number of times element appears in the tuple
print(weekend.index("Saturday")) #returns the index in the tuple where element is found, error if not found


#sets store a collection of values like lists and tuples but do not allow for duplicates
#sets are also unordered, meaning you cannot use index to get values
print("\nSet Examples:")
ids = {123, 456, 456, 789}
print(ids) #duplicates are automatically removed

#some important set methods
ids.add(321) #add something to the set, if it does not already exist
ids.discard(123) #remove element from the set
print(ids)

more_ids = {321, 654, 987}
combined = ids.union(more_ids) #combine the contents to 2 sets into 1, removes duplicates
print(combined)


#dictionaries are a list of key-value pairs
#dictionaries are mutable; cannot have duplicates of the same key
print("\nDictionary Examples:")
book = {
    "title" : "The Hobbit",
    "author" : "JRR Tolkien",
    "pages" : 305,
    "on_shelf" : True
} #on the left of the colon is the key, on the right is the value associated with that key

print(book["title"]) #search a dictionary by its key to retrieve the value
book["on_shelf"] = False #can change values

#some important dictionary methods
print(book.get("publisher", "Not in system"))
#get() method tries to get the value of provided key, optionally you can choose to return a value if not found
book.pop("pages") #remove an element by key
print(book.keys()) #retuns a list of all keys in dictionary

book.update({"publisher" : "Penguin"}) #add new key-value pairs to dictionary
print(book)