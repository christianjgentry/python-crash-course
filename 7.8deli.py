# i don't eat sandwiches so i'm using burgers of the day from Bob's Burgers

sandwich_orders = ['cheese louise', 'poblano picasso', 'tunami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I have made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches are ready:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())