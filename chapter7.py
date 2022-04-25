# prompt = "What kind of car would you like to rent"
# rental_car = input(prompt)
# print(f"Let me see if we have a(n) {rental_car} at this time.")

# group_size = input("How many people will be in your group tonight?")

# group_size = int(group_size)

# if group_size > 8:
#     print(f"For a party of {group_size}, we estimate a 30 minute wait.")
# else:
#     print("Please follow the hostess to your table.")

# chosen_number = input("Please give me a number.")
# chosen_number = int(chosen_number)
# if chosen_number % 10 == 0:
#     print(f"{chosen_number} is a multiple of 10.")
# else:
#     print(f"{chosen_number} is not a multiple of 10.")

# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished."

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
    
#     if age < 3:
#         print("You get in free!")
#     elif age < 13:
#         print("Your ticket is $10.")
#     else:
#         print("Your ticket is $15.")

# prompt = "\nPlease enter a topping you want."
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else:
#         print("We will add that topping.")


prompt = "\nPlease enter a topping you want."
prompt += "\n(Enter 'quit' when you are finished.)"

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("We will add that topping.")


