import json

"""user = str(input("entrer un user: "))
password = str(input("entrer un password: "))

"""
def check_user(user, password):
    # Load existing user data from the file (if any)
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    # Search for the user in the list
    for u in users:
        if u['user'] == user:
            # If the user exists, check if the password is correct
            if u['pass'] == password:
                return 'TT'  # user exists and password is correct
            else:
                return 'TF'  # user exists but password is incorrect

    # If the user does not exist, return False
    return 'FF'
