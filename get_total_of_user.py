import json

def get_user_total(user):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Search for the user in the list
    for u in users:
        if u['user'] == user:
            # If the user exists, return the total value
            return u.get('total', 0)

    # If the user does not exist, return 0
    return 0
