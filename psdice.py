import random
roll = random.randint(1,6)
guess = input('Guess the dice roll: \n')
if guess == roll:
       print(f"Correct! They rolled a {roll}")
else: 
   print(f"Wrong! They rolled a {roll}.")