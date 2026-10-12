import random

easy_attempts = 10
hard_attempts = 5

random_number = random.randint(1, 30)

print('Please guess a number between 1 to 30')
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

if difficulty not in ('easy', 'hard'):
    print("Invalid input!")
    exit()

attempts = easy_attempts if difficulty == 'easy' else hard_attempts
print(f"You have {attempts} attempts to guess a number")

game_over = False

while not game_over:
  guess_number =  int(input("Make a guess: "))

  if guess_number < 1 or guess_number > 30:
    print("Oops! Your guess is out of range. Please pick a number between 1 and 30.")
    attempts -= 1
    print(f"You have {attempts} attempts left to guess a number")
  elif guess_number > random_number:
    print("Too high!")
    print("Guess again.")
    attempts -= 1
    print(f"You have {attempts} attempts left to guess a number")

    if attempts == 0:
      print("You lose!")
      exit()
  elif guess_number < random_number:
    print("Too low!")
    print("Guess again.")
    attempts -= 1
    print(f"You have {attempts} attempts left to guess a number")

    if attempts == 0:
      print("You lose!")
      exit()
  elif guess_number == random_number:
    print("You win!")
    game_over = True