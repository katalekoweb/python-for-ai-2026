# Data Structures

# age = 24
# has_licence = True

# my_list = ["Alice", 25, age, True, has_licence]

# name = my_list[0] # Alice
# age = my_list[1]

# my_list[0] = "Dave"
# my_list.append("Alice")
# # Insert, add in specific position
# my_list.insert(1, "Alice")
# my_list.remove("Alice")

# has_licence = my_list[-1] # Latest Index

# print(my_list)

# Dictionaries
# Key Value 
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# person["name"] = "Dave"
# person["licence"] = True

# del person["licence"]
# print(person)
# print(person.keys())
# print(person.values())
# print(person.items())

# Tuples - are immutables
# empty = ()
# point = (3,5)
# colors = ("red", "green", "blue")

# colors[0] = "blue"
# print(colors)

# Sets
# Empty set (careful!)
empty_set = set() # Not {}

# Set with values
numbers = {1,2,3,4,5}
fruits = set(["Apple", "banana", "orange"])

# From a list removes duplicates
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores) # dont accept duplicates