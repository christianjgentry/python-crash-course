group_size = input("How many people will be in your group tonight?")

group_size = int(group_size)

if group_size > 8:
    print(f"For a party of {group_size}, we estimate a 30 minute wait.")
else:
    print("Please follow the hostess to your table.")