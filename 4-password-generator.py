import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the Password Generator.\n\n")

number_of_letters = int(input('How many letters would you like in your password? '))

if number_of_letters > len(letters):
    print(f"You can only choose up to {len(letters)} letters.")
    exit()

number_of_numbers = int(input('How many numbers would you like in your password? '))

if number_of_numbers > len(numbers):
    print(f"You can only choose up to {len(numbers)} numbers.")
    exit()

number_of_symbols = int(input('How many symbols would you like in your password? '))

if number_of_symbols > len(symbols):
    print(f"You can only choose up to {len(symbols)} symbols.")
    exit()

random_letters = random.sample(letters, number_of_letters)
random_numbers = random.sample(numbers, number_of_numbers)
random_symbols = random.sample(symbols, number_of_symbols)

combined = random_letters + random_numbers + random_symbols

easy_generated_password = "".join(combined)

random.shuffle(combined)

hard_generated_password = "".join(combined)

print('\n')
print(f"Your Easy Generated Password: {easy_generated_password} \n")
print(f"Your Hard Generated Password: {hard_generated_password} \n")




