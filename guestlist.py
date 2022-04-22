guests = ["Grandfox", "Jesus", "Winston Churchill"]
print(f"{guests[0]}, Would you please come to dinner?")
print(f"{guests[1]}, Would you please come to dinner?")
print(f"{guests[-1]}, You better bring your ass to dinner?")

popped_guests = guests.pop()
print(guests)
print(popped_guests)

guests.append("Grandmother")
print(guests)

print(f"{guests[0]}, Would you please come to dinner?")
print(f"{guests[1]}, Would you please come to dinner?")
print(f"{guests[-1]}, You better bring your ass to dinner!")

message = "I am going to invite more guests."
print(message)

guests.insert(0,"Caroline")
print(guests)

guests.insert(2, "Kyle")
print(guests)

guests.append("Grant")
print(guests)

print(f"{guests[0]}, Would you please come to dinner?")
print(f"{guests[1]}, Would you please come to dinner?")
print(f"{guests[2]}, Would you please come to dinner?")
print(f"{guests[3]}, Would you please come to dinner?")
print(f"{guests[4]}, Would you please come to dinner?")
print(f"{guests[-1]}, You better bring your ass to dinner!")

message = "I just found out I can only invite 2 guests to dinner. I need you all to fight to the death to see who can come."
print(message)

popped_guests = guests.pop()
print(guests)
print(f"{popped_guests}, I'm sorry you're dead and can't come to dinner")

popped_guests = guests.pop()
print(guests)
print(f"{popped_guests}, I'm sorry you're dead and can't come to dinner")

popped_guests = guests.pop()
print(guests)
print(f"{popped_guests}, I'm sorry you're dead and can't come to dinner")

popped_guests = guests.pop()
print(guests)
print(f"{popped_guests}, I'm sorry you're dead and can't come to dinner")

print(f"{guests[0]}, You did not die in the battle to the death so you may still attend dinner.")
print(f"{guests[1]}, You did not die in the battle to the death so you may still attend dinner.")

guests.remove("Caroline")
print(guests)

del guests[0]
print(guests)