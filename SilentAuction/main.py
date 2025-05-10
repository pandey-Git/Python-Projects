from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
info={}
detail=[]
end_auction=True
while end_auction:
  name=input("What is your name?")
  bid=int(input("What is your bid? $"))
  detail_list=[name,bid]
  detail.append(detail_list)
  info.update(detail)
  word=input("Are there any bidders? Type 'yes' or 'no'.\n")
  if word=="yes":
    clear()
  else:
    end_auction=False
    
def check(name,bid):
  for key in info:
    max_bid=info[key]
    if info[key]>max_bid:
      max_bid=info[key]
  print(f"The winner is {name} with a bid of ${max_bid}")
check(name, bid)
