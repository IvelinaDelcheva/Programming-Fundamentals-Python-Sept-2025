usernames = input().split(', ')


def lenght_validation(some_user: str) -> bool:
    if len(some_user) in range(3, 16):
        return True

def symbol_validation(some_username: str) -> bool:
    if some_username.isalnum() or '-' in some_username or '_' in some_username:
        return True

def redundant_symbol(user_name: str) -> bool:
    if ' ' not in user_name:
        return True

def validate_username(user: str) -> str:
    if lenght_validation(user) and symbol_validation(user) and redundant_symbol(user):
        return user


for username in usernames:
    username = validate_username(username)
    if username:
        print(username)