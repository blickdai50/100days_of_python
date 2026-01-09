import random

options = ["rock", "paper", "scissors"]
graphics = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

option= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
human = options[option]
print(graphics[option])
print("Computer chose:\n")
ch = random.randint(0, 2)
computer = options[ch]
print(graphics[ch])
msg = ''

if human == computer:
    msg = "It's a draw"
elif human == "rock" and computer == "scissors":
    msg = "You win"
elif human == "scissors" and computer == "paper":
    msg = "You win"
elif human == "paper" and computer == "rock":
    msg = "You win"
else:
    msg = "You lose"

print(msg)