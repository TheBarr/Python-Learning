import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock,paper,scissors]

your_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
print(f"\nYour choice is \n{rps[your_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer choice is \n{rps[computer_choice]}")

if your_choice >= 3 or your_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif computer_choice == 0 and your_choice == 0 or computer_choice == 1 and your_choice == 1 or computer_choice == 2 and your_choice == 2:
  print("Draw! 🤐")
elif computer_choice == 0 and your_choice == 1 or computer_choice == 1 and your_choice == 2 or computer_choice == 2 and your_choice == 0:
  print("You Win! 😁")
else:
  print("Your lose 😭!")
