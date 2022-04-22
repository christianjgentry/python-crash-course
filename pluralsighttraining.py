#amount = 200
#tax = .07
#total = amount + amount*tax
#print(total)

#hello = "hello"
#name = input("What's your name?\n")
#greeting = hello + ", " + name
#print(greeting)

#age = int(input("How old are you?\n"))
#decades = age//10
#years = age % 10
#print(f"You are {decades} decades and {years} years old.")

#temp = 90

#if temp > 80:
#    print("it's too hot!")
 #   print("Stay inside!")
#elif temp < 60:
#    print("It's too cold!")
#    print("Stay inside!")
#else:
#    print("Enjoy your walk!")

#temp = 75
#forecast = "sunny"
#if temp < 80 and forecast != "rain":
#    print("Go outside!")
#else:
#    print("Stay inside!")

#import random

#comp_choice = random.choice(['scissors', 'rock', 'paper'])
#user_choice = input("Do you want - rock, paper, or scissors? \n")
#if comp_choice == user_choice:
#    print("TIE")
#elif user_choice == 'rock' and comp_choice == 'scissors':
#    print('WIN, the comp had scissors')
#elif user_choice == 'paper' and comp_choice == 'rock':
#    print('WIN, the comp had rock')
#elif user_choice == 'scissors' and comp_choice == 'paper':
#    print('WIN, the comp had paper')
#else: 
#    print("LOSE")


#import random
#roll = random.randint(1,6)
#guess = input('Guess the dice roll: \n')
#if guess == roll:
#        print(f"Correct! They rolled a {roll}")
#else: 
#    print(f"Wrong! They rolled a {roll}.")

#acronyms = ['lol', 'idk', 'smh', 'tbh']
#print(acronyms[0])

#acronyms = []
#acronyms.append('lol')
#acronyms.append('idk')
#print(acronyms)

#acronyms = ['lol', 'idk', 'smh', 'tbh']
#word = "smh"
#if word in acronyms:
 #   print(f"{word} is in list")

#acronyms = ['lol', 'idk', 'smh', 'tbh']
#for acronym in acronyms: 
#    print(acronym)

#expenses = [10.50, 8, 5, 15, 20, 5, 3]
#sum = 0

#for x in expenses:
#    sum = sum + x

#print(f"You spent ${sum} this week on lunch.")

#expenses = [10.50, 8, 5, 15, 20, 5, 3]
#total = sum(expenses)

#print(f"You spent ${total} this week on lunch.")

#for i in range(7):
#    print(i)

#total = 0
#expenses=[]
#for i in range(7):
#    expenses.append(float(input("Enter an expense.")))
#total = sum(expenses)
#print(f"You spent ${total}.")

#total = 0
#expenses=[]
#num_expenses = int(input("Enter # of expenses:"))
#for i in range(num_expenses):
#    expenses.append(float(input("Enter an expense.")))
#total = sum(expenses)
#print(f"You spent ${total}.")

#get the loan details


# dollars_owed = float(input("How much money do you owe in dollars?\n")) #50,000
# apr = float(input("What is the APR? \n")) #3%)
# payment = float(input("What will your monthly payment be in dollars?\n")) #1,000
# months = int(input("How many months do you want to see results for? \n")) #24

# #divide apr by 100 and then by 12 to make it a monthly percent
# monthrate = apr/100/12

# for i in range(months):
#     #add interest
#     interest_paid = dollars_owed * monthrate
#     dollars_owed = dollars_owed + interest_paid

#     if (dollars_owed - payment < 0):
#         print(f"The last payment is {dollars_owed}.")
#         print(f"You paid off the loan in {i+1} months.")
#         break

#     #make payment
#     dollars_owed = dollars_owed - payment

#     #print the results after this month
#     print(f"Paid {payment}, of which, {interest_paid} was interest.")
#     print(f"Now I owe {dollars_owed}.")

