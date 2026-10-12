print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.\n\n')

direction = input("You're at a cross road. Where you want to go?\n            Type 'left' or 'right'\n")

if direction == 'left':
  action = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across\n")

  if action == 'wait':
    color = input("You arrive at the island unharmed. There is a house with 3 doors.\n  One red, one yellow and one blue. Which color will you choose?\n")

    if color == 'yellow':
      print("You Win!") 
    else:
      print("Game Over!")
  else:
    print("Game Over!")
else:
  print("Game Over!")
