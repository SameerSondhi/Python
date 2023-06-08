# List of tuples
people = [
    ("Jon", 35),
    ("Garfield", 7),
    ("Odie", 8)
]

# Accessing values in tuple
print(people[0][0])
print(people[0])

person = people[0]
print(person[0])

# Single tuple
names = ("Jon",)

# Are the two lists the same?
list1 = [1,2,3]
list2 = [1,2,3]

# id prints a reference to the location in memory
print(id(list1))
print(id(list2))

# This will be true because they contain the same data
print(list1==list2)

# This is false because they are stored in separate memory locations
print(list1 is list2)