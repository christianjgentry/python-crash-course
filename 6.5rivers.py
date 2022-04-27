rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'the ganges':'india and bangladesh'
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("The following rivers are included in this data set")
for river in rivers:
    print(river.title())

print("The following countries are included in this dataset:")
for country in rivers.values():
    print(country.title())