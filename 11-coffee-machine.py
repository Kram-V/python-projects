menu = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18
    },
    "cost": 1.5
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24
    },
    "cost": 2.5
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24
    },
    "cost": 3.0
  },
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
  "money": 0
}

is_off = False

while not is_off:
  print("You can type 'report' to see the current resources")
  coffee = input("What would you like? (espresso/latte/cappucino): ").lower()
  
  if coffee == 'off':
    is_off = True
    continue

  if coffee == 'report':
    for key, value in resources.items():
      if key == 'water' or key == 'milk':
        print(f"{key.capitalize()}: {value}ml")
      elif key == 'coffee':
        print(f"{key.capitalize()}: {value}g")
      else:
        print(f"{key.capitalize()}: ${value}")
    continue

  if coffee == 'espresso':
    ingredients = menu[coffee]['ingredients']
    cost = menu[coffee]['cost']

    if ingredients['water'] > resources['water']:
      print("Sorry there is not enough water.")
      continue

    if ingredients['coffee'] > resources['coffee']:
      print("Sorry there is not enough coffee.")
      continue

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.10
    nickles_amount = nickles * 0.05
    pennies_amount = pennies * 0.01

    total_amount = quarters_amount + dimes_amount + nickles_amount + pennies_amount

    if total_amount < cost:
      print("Sorry that's not enough money. Money refunded.")
    elif total_amount > cost:
      change = total_amount - cost
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['coffee'] -= ingredients['coffee']

      print(f"Here is ${round(change, 2)} dollars in change.")
    else:
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['coffee'] -= ingredients['coffee']
  elif coffee == 'latte':
    ingredients = menu[coffee]['ingredients']
    cost = menu[coffee]['cost']

    if ingredients['water'] > resources['water']:
      print("Sorry there is not enough water.")
      continue

    if ingredients['milk'] > resources['milk']:
      print("Sorry there is not enough milk.")
      continue

    if ingredients['coffee'] > resources['coffee']:
      print("Sorry there is not enough coffee.")
      continue

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.10
    nickles_amount = nickles * 0.05
    pennies_amount = pennies * 0.01

    total_amount = quarters_amount + dimes_amount + nickles_amount + pennies_amount

    if total_amount < cost:
      print("Sorry that's not enough money. Money refunded.")
    elif total_amount > cost:
      change = total_amount - cost
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['milk'] -= ingredients['milk']
      resources['coffee'] -= ingredients['coffee']

      print(f"Here is ${round(change, 2)} dollars in change.")
    else:
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['milk'] -= ingredients['milk']
      resources['coffee'] -= ingredients['coffee']
  elif coffee == 'cappuccino':
    ingredients = menu[coffee]['ingredients']
    cost = menu[coffee]['cost']

    if ingredients['water'] > resources['water']:
      print("Sorry there is not enough water.")
      continue

    if ingredients['milk'] > resources['milk']:
      print("Sorry there is not enough milk.")
      continue

    if ingredients['coffee'] > resources['coffee']:
      print("Sorry there is not enough coffee.")
      continue

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.10
    nickles_amount = nickles * 0.05
    pennies_amount = pennies * 0.01

    total_amount = quarters_amount + dimes_amount + nickles_amount + pennies_amount

    if total_amount < cost:
      print("Sorry that's not enough money. Money refunded.")
    elif total_amount > cost:
      change = total_amount - cost
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['milk'] -= ingredients['milk']
      resources['coffee'] -= ingredients['coffee']

      print(f"Here is ${round(change, 2)} dollars in change.")
    else:
      resources['money'] += cost
      resources['water'] -= ingredients['water']
      resources['milk'] -= ingredients['milk']
      resources['coffee'] -= ingredients['coffee']
  else:
    print("Invalid Input!")