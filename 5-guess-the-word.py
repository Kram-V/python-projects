import random

word_list = ['jobelle', 'mark', 'diane', 'joseph', 'ryan']

random_number = random.randint(0, len(word_list) - 1)

chosen_word = word_list[random_number]

word_length = len(chosen_word)

lives = word_length + 3

print("\n")
print(f"Your lives: {lives}")
print("_" * word_length)

game_over = False
existing_letters = []

while not game_over:
  user_input = input('Please guess a letter: ').lower()
  print("\n")

  if user_input not in chosen_word or user_input in existing_letters:
    lives -= 1

  display = ""

  for letter in chosen_word:
    if letter == user_input:  
      display += letter
      existing_letters.append(letter)
    elif letter in existing_letters:
      display += letter
    else:
      display += "_"

  print(f"Your lives {lives}")
  print(display)

  if "_" not in display:
    game_over = True
    print("You win!")

  if lives == 0:
      game_over = True
      print("You lose!")