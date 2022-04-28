age = 20
if age <= 2:
    lifestage = 'infant'
elif age > 2 and age < 4:
    lifestage = 'toddler'
elif age >= 4 and age < 13:
    lifestage = 'kid'
elif age >= 13 and age < 20:
    lifestage = 'teenager'
elif age >= 20 and age < 65:
    lifestage = 'adult'
elif age >= 65:
    lifestage = 'elder'
print(f'your lifestage is considered {lifestage}.')