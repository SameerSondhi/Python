names = ["Nermal", "Jon", "Garfield", "Odie"]

# This will print the first item in the list
print(names[0])

# Will print last item -> useful when you don't know how many items in the list
print(names[-1])

names = names + ["Simon"]
print(names)

names.append("Simon")
print(names)

#  index, value
names.insert(3, "Arlene")
print(names)

#  Removing items
names.remove("Arlene")
print(names)

# Also removes items at a particular index
del names[0]
print(names)

names.pop()
print(names)

names.pop(-1)
print(names)

# Since pop returns the item that is removed, we can print that returned item
last_name_in_list = names.pop()
print(names)
print(last_name_in_list)

# clear removes every item in list
names.clear()
print(names)