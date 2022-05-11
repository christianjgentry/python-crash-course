def make_sandwich(*items):
    """make sandwiches with provided items."""
    print("\nI'll make you a sammie")
    for item in items:
        print(f"...adding {item} to your sammie.")
    print("Your sammie is ready.")

make_sandwich('roast beef', 'cheddar', 'lettuce')
make_sandwich('tuna', 'gouda', 'lettuce')
make_sandwich('turkey', 'pepper jack', 'bacon', 'avocado lime ranch')