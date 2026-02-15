import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
print("Let's play rock, paper, scissors game.")
print("==========================================================")
print("What do you choose?")
computer_choice = random.randint(0, 2)
player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print("==========================================")

print(f"You chose: {choices[player_choice]}")
print(f"Computer chose: {choices[computer_choice]}")
print("==========================================")

if computer_choice == player_choice:
    print("It's a draw")
elif (computer_choice == 0 and player_choice == 1) or \
    (computer_choice == 1 and player_choice == 2) or \
    (computer_choice == 2 and player_choice == 0):
    print("You Win!")
else:
    print("You Lose!")