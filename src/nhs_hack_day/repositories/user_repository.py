

users = {}

def list_users():
    return list(users.values())

def create_new_user(user):
    global users
    users[user.user_id] = user
    return user
