print('Welcome to the Tip Calculator\n\n')

total_bill = float(input('What was the total bill? '))
tip = int(input('How much tip would you like to give (in percent)? '))
people_to_split_the_bill = int(input('How many people should pay the bill? '))

tip_percentage = tip / 100

tip_to_give = total_bill * tip_percentage

total_amount = total_bill + tip_to_give

total_amount_per_person = total_amount / people_to_split_the_bill

print(f"Each person should pay ${round(total_amount_per_person, 2)}. And you gave ${round(tip_to_give, 2)} tip.")