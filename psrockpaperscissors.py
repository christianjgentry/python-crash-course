import random

comp_choice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input("Do you want - rock, paper, or scissors? \n")
if comp_choice == user_choice:
   print("TIE")
elif user_choice == 'rock' and comp_choice == 'scissors':
   print('WIN, the comp had scissors')
elif user_choice == 'paper' and comp_choice == 'rock':
   print('WIN, the comp had rock')
elif user_choice == 'scissors' and comp_choice == 'paper':
   print('WIN, the comp had paper')
else: 
   print("LOSE")