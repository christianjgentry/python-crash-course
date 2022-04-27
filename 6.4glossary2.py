definition = glossary.get('tuple', "No definition provided")
print(f"The definition of a tuple is an {definition}.")
definition = glossary.get('string', "No definition provided")
print(f"The definition of a string is a {definition}.")

for key, value in glossary.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
