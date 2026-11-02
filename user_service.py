class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


def get_user(user_id):
    users = {
        1: User(1, "Alice", "alice@example.com"),
        2: User(2, "Bob", "bob@example.com"),
        3: User(3, "Charlie", "charlie@example.com"),
    }

    return users.get(user_id)


def validate_user(user):
    if user is None:
        return False

    if not user.user_id or not user.email:
        return False

    return True


def get_user_email(user_id):
    user = get_user(user_id)

    if not user:
        return None

    return user.email

def print_user(user_id):
    user = get_user(user_id)

    if not validate_user(user):
        print("Invalid user")
        return