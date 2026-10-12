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

choices = [rock, paper, scissors]
random_number = random.randint(0, 2)
computer_chose = choices[random_number]

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))

if (user_input > len(choices) - 1):
  print('Invalid input, You lose!')
  exit()

user_chose = choices[user_input]

print('\n\n')

if user_input == random_number:
  print('You Chose:\n')
  print(user_chose + '\n')
  print('Computer Chose:\n')
  print(computer_chose + '\n')
  print('Its a Draw!')
elif (user_input == 0 and random_number == 2) or (user_input == 1 and random_number == 0) or (user_input == 2 and random_number == 1):
  print('You Chose:\n')
  print(user_chose + '\n')
  print('Computer Chose:\n')
  print(computer_chose + '\n')
  print('You Win!')
else:
  print('You Chose:\n')
  print(user_chose + '\n')
  print('Computer Chose:\n')
  print(computer_chose + '\n')
  print('You Lose!')

