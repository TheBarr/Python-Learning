from random import choice
from game_data import data
from replit import clear
from art import logo, vs

a = choice(data)
data.remove(a)
b = choice(data)
data.remove(b)


def porownanie(a, b):
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    if a_followers > b_followers:
        return "a"
    elif b_followers > a_followers:
        return "b"

game = True
counter = 0
while game:
    print(logo)
    if counter > 0:
        print(f"You're right! Current score: {counter}.")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(a['follower_count'])
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    print(b['follower_count'])
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    answer = porownanie(a, b)
    if user_answer == answer:
        counter += 1
        clear()
        if answer == "b":
            a = b
        b = choice(data)
        data.remove(b)
    else:
        clear()
        print(f"Your final score is {counter}")
        game = False
