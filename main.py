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
import random
print("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
choice=int(input())
list=["rock","paper","scissors"]
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
else:
    print(scissors)
computer_choice=random.randint(0,2) 
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)
if (choice==0 and computer_choice==1) or (choice==0 and computer_choice==2):
    print("You win")
elif (choice==1 and computer_choice==0) or (choice==1 and computer_choice==2):
    print("You lose")
else:
    print("It's a draw")
