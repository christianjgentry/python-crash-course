def formatted_city(city, country):
    """Pair City with its respective country."""
    city_country = f"{city}, {country}"
    return city_country.title()

city_country= formatted_city('santiago', 'chile')
print(city_country)

city_country= formatted_city('paris', 'france')
print(city_country)

city_country= formatted_city('christchurch', 'new zealand')
print(city_country)