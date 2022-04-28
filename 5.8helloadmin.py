usernames = ['admin', 'alex', 'lauren', 'flor', 'genesis']

for username in usernames: 
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello, {username}.")