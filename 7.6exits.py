
prompt = "\nPlease enter a topping you want."
prompt += "\n(Enter 'quit' when you are finished.)"

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("We will add that topping.")


