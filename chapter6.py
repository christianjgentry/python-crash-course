# person1 = {'firstname':'caroline', 'lastname':'trotter', 'age':'22', 'location':'    richardson'}
# print(person1['firstname'].title())
# print(person1['lastname'].title())
# print(person1['age'])
# print(person1['location'].title().strip())

# favorite_numbers = {'caroline': 9, 'steven': 7, 'flor': 4, 'lauren': 11, 'alex': '6'}
# print(favorite_numbers)

# glossary = {
#     'tuple': 'unchanging list',
#     'string': 'string of text',
#     'float': 'number with a decimal',
#     'slice': 'cutting part of a list to use',
#     'boolean': 'conditional test',
#     'set': 'removes duplicates',
#     }

# # definition = glossary.get('tuple', "No definition provided")
# # print(f"The definition of a tuple is an {definition}.")
# # definition = glossary.get('string', "No definition provided")
# # print(f"The definition of a string is a {definition}.")

# for key, value in glossary.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


# rivers = {
#     'nile': 'egypt',
#     'amazon': 'south america',
#     'the ganges':'india and bangladesh'
#     }

# for river, country in rivers.items():
#     print(f"The {river.title()} flows through {country.title()}.")

# print("The following rivers are included in this data set")
# for river in rivers:
#     print(river.title())

# print("The following countries are included in this dataset:")
# for country in rivers.values():
#     print(country.title())

# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
#     }   

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# coders = ['jen', 'sarah', 'edward', 'alex', 'phil', 'flor']

# for coder in coders:
#     if coder in favorite_languages:
#         print (f"Thank you for taking the poll, {coder.title()}.")
#     else:
#         print(f"{coder.title()}, please take our poll.")


# people = []

# person =  { 
#     'firstname':'caroline', 
#     'lastname':'trotter', 
#     'age':'22', 
#     'location':'richardson',
#     }
# people.append(person)
    
# person = {
#     'firstname':'lauren', 
#     'lastname':'trotter', 
#     'age':'36', 
#     'location':'forney',
#     }
# people.append(person)

# person = {
#     'firstname':'grant', 
#     'lastname':'trotter', 
#     'age':'30', 
#     'location':'denton',
#     }
# people.append(person)

# for person in people:
#     name = f"{person['firstname'].title()} {person['lastname'].title()}"
#     age = person['age']
#     city = person['location'].title()

#     print(f"{name}, in {city} is {age} years old.")


# pets = []
# pet = { 
#     'name':'pippin', 
#     'color':'white', 
#     'age': '8', 
#     'breed':'samoyed mix',
#     }
# pets.append(pet)
    
# pet =  { 
#     'name':'merry', 
#     'color':'Grey and White', 
#     'age': '1', 
#     'breed':'alaskan malamute',
#     }
# pets.append(pet)
# print(pets)

# for pet in pets:
#     print(f"\nHere's what I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key.title()}:{value.title()}")

# favorite_places = {
#     'lauren':['scotland', 'new zealand', 'muir woods', 'greece'],
#     'flor':["the dining room of the home of my parents when food has been made", 'bathtub','top deck of a cruise ship', 'recliner farthest from the tv'],
#     }

# for name, places in favorite_places.items():
#     print(f"\n {name.title()}'s favorite places are as follows:")
#     for place in places:
#         print(f"-{place.title()}")

# favorite_numbers = {
#     'caroline': [9, 11, 13], 
#     'steven': [7, 5, 3],
#     'flor': [4, 6], 
#     'lauren': [11, 77, 99, 55],
#     'alex': [66, 88, 44],
#     }

# for name, number in favorite_numbers.items():
#     print(f"\n {name.title()}'s favorite number is {number}.")

favorite_places = {
    'lauren':['scotland', 'new zealand', 'muir woods', 'greece'],
    'flor':["the dining room of the home of my parents when food has been made", 'bathtub','top deck of a cruise ship', 'recliner farthest from the tv'],
    'flor, now that she understands the assignment':['dallas', 'chicago', 'grand canyon'],
    }

for name, places in favorite_places.items():
    print(f"\n {name.title()}'s favorite places are as follows:")
    for place in places:
        print(f"-{place.title()}")

