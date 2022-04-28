current_users = ['admin', 'alex', 'lauren', 'flor', 'genesis']
new_users = ['margo', 'elizabeth', 'charles', 'flor', 'genesis']

for new_user in new_users:
    if new_user in current_users:
        print(f"sorry, {new_user} is already in use. Please select another.")
    else:
        print(f"{new_user} is available.")