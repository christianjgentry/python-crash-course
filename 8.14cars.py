def build_car(manufacturer, model, **options):
    """make dictionary representing a car."""
    car_dict = {
        'manufacturer':manufacturer.title(),
        'model':model.title(),
        }

    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_buick = build_car('buick', 'lacrosse',trim_level = 'premium trim level')
print(my_buick)

