pets = []
pet = { 
    'name':'pippin', 
    'color':'white', 
    'age': '8', 
    'breed':'samoyed mix',
    }
pets.append(pet)
    
pet =  { 
    'name':'merry', 
    'color':'Grey and White', 
    'age': '1', 
    'breed':'alaskan malamute',
    }
pets.append(pet)
print(pets)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}:{value.title()}")