# Example of a string
print("Hello, nice to meet you")

# Naming variables
age = 30
name = "Sameer"

# Multiplying int and float stored in variables
# Multiplying any number by a float results in a float
# Define variables before operations
wage = 12.50
hours_worked = 40

print(wage * hours_worked)


# Getting values from user using input function and storing it in a variable
user_name = input("What is your name? ")

# Cannot concatenate a string and a number, so we need to use the variable instead
print("Hello: " + user_name)

# Convert string to number or vice versa
days_in_feb = str(28)  # This will be the same as writing days_in_feb = "28"

days_in_july = int("31")  # This will be the same as writing days_in_july = 31

# String to float and then float to int
wage = float("18.50")
print(int(wage))  # This truncates the float and results in 18

# STRING INTERPOLATION
string1 = "John is 24 years old"

# 4 ways to interpolate the above string
interpolated_string1 = "{} is {} years old".format("John", 24)
interpolated_string2 = string1.format("John", 24)
interpolated_string3 = "{0} is {1} years old".format("John", 24)
interpolated_string4 = "{name} is {age} years old".format(name="John", age=24)

# f-strings
first_name = "John"
age_in_years = 24
print(f"{first_name} is {age_in_years} years old")
print(f"{first_name} is {age_in_years * 12} months old")

# Built-in string functions
string = "Sam"
second_string = "      Sam      "
print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.title())

# Removes extra white space
print(second_string.strip())

# Chaining methods
print(second_string.strip().upper())


