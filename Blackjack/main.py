############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from replit import clear
from art import logo
def play_game():
  
  user_card = []
  comp_card = []
  score=0
  score_comp=0
  end_game = True
  choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if choice=="y":
    clear()
    print(logo)
    user_card=random.sample(cards,2)
    comp_card=random.sample(cards,2)
    while end_game:
      for i in user_card:
        score+=i
      for i in comp_card:
        score_comp+=i
      first_card_comp=comp_card[0]
      print(f"Your cards: {user_card}, current score: {score}")
      print(f"Computer's first card: {first_card_comp}")
      if score>21:
        print("You went over. You lose")
        end_game=False
      elif sum(user_card)==21 and len(user_card)==2:
        print("You won with a blackjack.")
      elif sum(comp_card)==21 and len(comp_card)==2:
        print("Computer won with a blackjack")
      elif 11 in user_card and sum(user_card)>21:
        user_card.remove(11)
        user_card.append(1)
      else:
        option_to_continue=input("Type 'y' to get another card, type 'n' to pass: ")
        if option_to_continue=="n":
          end_game=False
          print(f"Your final hand: {user_card}, final score: {score}")
          print(f"Computer's final hand: {comp_card}, final score: {score_comp}")
          if score>score_comp:
            print("You win")
          elif score==score_comp:
            print("Draw")
          else:
            print("You lose")
        else:
            end_game=True
            new_card=random.choice(cards)
            new_compcard=random.choice(cards)
            user_card.append(new_card)
            comp_card.append(new_compcard)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  print(logo)
  play_game()
