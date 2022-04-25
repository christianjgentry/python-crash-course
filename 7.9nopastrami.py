sandwich_orders = ['cheese louise', 'poblano picasso', 'tunami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami today, suckers!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I have made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches are ready:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())