pizzas = ['supreme', 'extra pepperoni', 'Neopolitan']
for pizza in pizzas:
    print(f"I like {pizza} pizzas.")
print("However, I don't like pizza as much as I like Chinese food.")

friendpizzas = pizzas[:]

pizzas.append('spicy')
print(pizzas)
print(friendpizzas)

friendpizzas.append('buffalo chicken')
print(friendpizzas)

for pizza in pizzas:
    print(pizza)
    
for friendpizza in friendpizzas:
    print(friendpizza)