import json

def delete_user(user):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Search for the user in the list
    for i, u in enumerate(users):
        if u['user'] == user:
            # If the user exists, remove it from the list
            del users[i]
            break

    # Save the updated user data back to the file
    with open('users.json', 'w') as f:
        json.dump(users, f)
