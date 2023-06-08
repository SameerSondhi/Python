# Boolean expressions
day = "Tuesday"
temperature = 30
isRaining = True

# not keyword reverses the true to false
# and has precedence over or
if day == "Tuesday" and temperature > 27 and not isRaining:
    print("Go swimming")
else:
    print("Learn Python")

# 0 and empty sequences evaluate to false
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your first name: ")
# if name != ""
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the one with no name?")