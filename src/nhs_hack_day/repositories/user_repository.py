

users = {}

def list_users():
    print(users)
    return users.items()

def create_new_user(user):
    global users
    users[user.user_id] = user
    return user
