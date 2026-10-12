import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def print_computer_user_cards(user_cards, computer_cards):
  joined_user_cards = ",".join(str(card) for card in user_cards)
  first_computer_card = str(computer_cards[0])

  print(f"Your cards: {joined_user_cards}")
  print(f"Computer's first card: {first_computer_card}")

def check_who_win(user_total_cards, computer_total_cards):
  if user_total_cards > 21:
    print("You Lose!")
  elif computer_total_cards > 21:
    print("You Win!")
  elif user_total_cards > computer_total_cards:
    print("You Win!")
  elif user_total_cards < computer_total_cards:
    print("You Lose!")
  else:
    print("Draw!")

answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if answer == 'y':
  user_hand = random.sample(cards, 2)
  computer_hand = random.sample(cards, 2)

  user_cards = user_hand
  computer_cards = computer_hand
elif answer == 'n':
  exit()
else:
  print('Invalid Input')
  exit()

print_computer_user_cards(user_cards, computer_cards)

game_over = False

while not game_over:
  answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()

  if answer == 'y':
    user_hand = random.sample(cards, 1)

    user_cards.append(user_hand[0])

    if sum(computer_cards) < 17:
      computer_hand = random.sample(cards, 1)

      computer_cards.append(computer_hand[0])

    print_computer_user_cards(user_cards, computer_cards)
  elif answer == 'n':
    user_total_cards = sum(user_cards)

    if sum(computer_cards) < 17:
      computer_hand = random.sample(cards, 1)

      computer_cards.append(computer_hand[0])

    computer_total_cards = sum(computer_cards)

    joined_user_cards = ",".join(str(card) for card in user_cards)
    joined_computer_cards = ",".join(str(card) for card in computer_cards)

    print(f"Your final hand: {joined_user_cards} ({user_total_cards})")
    print(f"Computer's final hand: {joined_computer_cards} ({computer_total_cards})\n\n")

    check_who_win(user_total_cards, computer_total_cards)

    game_over = True
  else:
    print('Invalid Input')
    exit()