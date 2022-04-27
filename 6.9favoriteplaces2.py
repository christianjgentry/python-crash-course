

favorite_places = {
    'lauren':['scotland', 'new zealand', 'muir woods', 'greece'],
    'flor':["the dining room of the home of my parents when food has been made", 'bathtub','top deck of a cruise ship', 'recliner farthest from the tv'],
    'flor, now that she understands the assignment':['dallas', 'chicago', 'grand canyon'],
    }

for name, places in favorite_places.items():
    print(f"\n {name.title()}'s favorite places are as follows:")
    for place in places:
        print(f"-{place.title()}")

    