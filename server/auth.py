USERS = {
    "admin": "1234",
    "user": "pass",
}

def authenticate(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False
