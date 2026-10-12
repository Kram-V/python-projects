import os

bids = {}

def find_winner(bids):
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}.")

more_bidders = True

while more_bidders:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    answer = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    
    if answer == 'no':
        more_bidders = False
        find_winner(bids)
    else:
        os.system('cls' if os.name == 'nt' else 'clear') 