name = input("What is your name? ").strip().capitalize()
age = int(input(f"What is your age, {name}? "))

# if age >=18:
#     print("You are old enough to vote!")
# else:
#     print(f"You are not old enough to vote. Come back in {18-age} years to vote")

if age<18:
    print(f"You are not old enough to vote. Come back in {18 - age} years to vote")
elif age == 900:
    print(f"No way you are {age} years old")
else:
    print("You are old enough to vote!")
    print("Put an X in the box")
