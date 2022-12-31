# Simple game of "Rock, Paper, Scissors" accompanied by ASCII art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rps = [rock, paper, scissors]

prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

opponent = random.randint(0,2)

if prompt == 0 and opponent == 1:
  print(rock)
  print(rps[opponent])
  print("You lost!")

if prompt == 0 and opponent == 2:
  print(rock)
  print(rps[opponent])
  print("You won!")

if prompt == 1 and opponent == 0:
  print(paper)
  print(rps[opponent])
  print("You won!")

if prompt == 1 and opponent == 2:
  print(paper)
  print(rps[opponent])
  print("You lost!")

if prompt == 2 and opponent == 0:
  print(scissors)
  print(rps[opponent])
  print("You lost!")

if prompt == 2 and opponent == 1:
  print(scissors)
  print(rps[opponent])
  print("You won!")
  
if prompt == opponent:
  print("This one's a draw!")
