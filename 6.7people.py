
people = []

person =  { 
    'firstname':'caroline', 
    'lastname':'trotter', 
    'age':'22', 
    'location':'richardson',
    }
people.append(person)
    
person = {
    'firstname':'lauren', 
    'lastname':'trotter', 
    'age':'36', 
    'location':'forney',
    }
people.append(person)

person = {
    'firstname':'grant', 
    'lastname':'trotter', 
    'age':'30', 
    'location':'denton',
    }
people.append(person)

for person in people:
    name = f"{person['firstname'].title()} {person['lastname'].title()}"
    age = person['age']
    city = person['location'].title()

    print(f"{name}, in {city} is {age} years old.")
