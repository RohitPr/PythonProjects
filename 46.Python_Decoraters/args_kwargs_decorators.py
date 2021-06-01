class User:
    def __init__(self, name):
        self.name = name
        self.is_online = False


def check_status(function):
    def wrapper(*args, **kwargs):
        if args[0].is_online:
            function(args[0])

    return wrapper


@check_status
def create_account(user):
    print(f"This is {user.name}'s account")


user = User("Rohit")
user.is_online = True
create_account(user)
