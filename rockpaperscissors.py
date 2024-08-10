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

choices = ["Rock","Paper","Scissors"]

print("Welcome to Rock, Paper, Scissors!")
inn = int(input('Press 0 to pick "Rock", press 1 to pick "Paper" or press 2 to pick "Scissors"'))

user = choices[inn]
rand = random.randint(0, len(choices)-1)
computer = choices[rand]

if user == "Rock" and computer == "Scissors":
    print("User: ")
    print(rock)
    print("Computer: ")
    print(scissors)
    print("\nUser has won!")

elif user == "Paper" and computer == "Rock":
    print("User: ")
    print(paper)
    print("Computer: ")
    print(rock)
    print("\nUser has won!")

elif user == "Scissors" and computer == "Paper":
    print("User: ")
    print(scissors)
    print("Computer: ")
    print(paper)
    print("\nUser has won!")

elif user == computer:
    print("User: ")
    print(user)
    print("Computer: ")
    print(computer)
    print("\nIt's a TIE. Try again!")


if computer == "Rock" and user == "Scissors":
    print("Computer: ")
    print(rock)
    print("User: ")
    print(scissors)
    print("\nComputer has won!")

elif computer == "Paper" and user == "Rock":
    print("Computer: ")
    print(paper)
    print("User: ")
    print(rock)
    print("\nComputer has won!")

elif computer == "Scissors" and user == "Paper":
    print("Computer: ")
    print(scissors)
    print("User: ")
    print(paper)
    print("\nComputer has won!")