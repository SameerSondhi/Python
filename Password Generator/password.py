#Random Password Generator by Sameer Sondhi
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for char in range (1, nr_letters+1):
  letter_result = random.choice(letters)
  password += letter_result

for char in range(1, nr_symbols+1):
    symbol_result = random.choice(symbols)
    password += symbol_result

for char in range(1, nr_numbers+1):
    number_result = random.choice(numbers)
    password += number_result

random.shuffle(password)

final_password = ""
for char in password:
  final_password += char
print("Your randomly generated password is: " + final_password)