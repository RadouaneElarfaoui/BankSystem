import json

def get_historique_user(user):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Search for the user in the list
    for u in users:
        if u['user'] == user:
            # If the user exists, return their history as a string
            history_str = ''
            for entry in u.get('history', []):
                history_str += f"{entry['date']} - ({entry['amount']})\n"
            return history_str.strip()
            break

    # If the user is not found, return an empty string
    return "pas d'action sur votre compte."




