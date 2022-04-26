chosen_number = input("Please give me a number.")
chosen_number = int(chosen_number)
if chosen_number % 10 == 0:
    print(f"{chosen_number} is a multiple of 10.")
else:
    print(f"{chosen_number} is not a multiple of 10.")