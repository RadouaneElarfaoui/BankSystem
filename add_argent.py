import json
from datetime import datetime


def add_to_total(user, number):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Search for the user in the list
    for u in users:
        if u['user'] == user:
            # If the user exists, add the number to the total value
            u['total'] = u.get('total', 0) + number
            u.setdefault('history', []).append({
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'amount': number
                })
            #print("user existe")

            break

    # Save the updated user data to the file
    with open('users.json', 'w') as f:
        json.dump(users, f)
    return True
