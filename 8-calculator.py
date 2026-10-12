total = 0

def start_calculating():
  global total
  num1 = float(input("Enter first number: \n"))
  operation = input("Select operation (+,-,/,*): \n")
  num2 = float(input("Enter second number: \n"))

  if operation == '+':
    total = num1 + num2
  elif operation == '-':
    total = num1 - num2
  elif operation == '/':
    total = num1 / num2
  elif operation == '*':
      total = num1 * num2
  else:
    print('Invalid Operation')

  print(f"The answer is {round(total, 2)}\n\n")

def continue_calculating():
  global total
  operation = input("Select operation (+,-,/,*): \n")
  num = float(input("Enter number: \n"))

  if operation == '+':
    total += num
  elif operation == '-':
    total -= num
  elif operation == '/':
    total /= num
  elif operation == '*':
      total *= num
  else:
    print('Invalid Operation')

  print(f"The answer is {round(total, 2)}\n\n")

start_calculating()

calculating = True

while calculating:
  answer = input(f"Type 'y' to continue calculating {total}, or type 'n' to start a new calculation.\n").lower()

  if answer == "y":
    continue_calculating()
  else:
    total = 0
    start_calculating()

