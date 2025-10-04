import random

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

game_images = [rock, paper, scissors]

people = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if people < 0 or people > 2:
    print("You typed an invalid number. You lose!")
else:
    print("You chose:")
    print(game_images[people])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer])

    if people == computer:
        print("It's a draw.")
    elif (people == 0 and computer == 2) or (people == 1 and computer == 0) or (people == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose.")
