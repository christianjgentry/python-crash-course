prompt = "\nPlease enter a topping you want."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
     topping = input(prompt)

     if topping == 'quit':
         break
     else:
         print("We will add that topping.")