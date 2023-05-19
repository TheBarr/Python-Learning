from replit import clear
from art import logo

print(logo)
values = {}
repeat = True
while repeat:
    print("Welcome to the secred auaction program.")
    name = input("What's your name?: ")
    bid = input("What's your bid?: ")
    again = input("Are there any other bids? (yes/no): ").lower()
    values[name] = bid
    if again == "no":
        repeat = False
        highest_bid = 0
        winner = ""
        for name in values:
            new_bid = int(values[name])
            if new_bid > highest_bid:
                highest_bid = new_bid
                winner = name
        print(f"The winnes is {winner} with a bid of ${highest_bid} bid")
    elif again == "yes":
        clear()
