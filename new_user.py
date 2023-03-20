import json

def add_user(user, password):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Create a new user dictionary and add it to the list
    new_user = {'user': user, 'pass': password}
    users.append(new_user)

    # Save the updated user data to the file
    with open('users.json', 'w') as f:
        json.dump(users, f)
