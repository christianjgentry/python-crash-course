responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("What's your dream vacation spot?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\nPolling is complete the results are below.")

for name,response in responses.items():
    print(f"{name.title()} would love to visit {response.title()}.")
