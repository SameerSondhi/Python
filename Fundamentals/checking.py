parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("Not in {}.".format(parrot))

activity = input("What would you like to do today? ")
# Using casefold()
if "cinema" not in activity.casefold():
    print("I'd like to go to the cinema")
