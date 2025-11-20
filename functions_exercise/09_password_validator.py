def password_validator(some_password: str) -> list:
    error_messages = []
    count_digits = 0
    if len(some_password) not in range(6, 10 + 1):
        error_messages.append('Password must be between 6 and 10 characters')
    if not some_password.isalnum():
        error_messages.append('Password must consist only of letters and digits')
    for letter in some_password:
        if letter.isdigit():
            count_digits += 1
    if count_digits < 2:
        error_messages.append('Password must have at least 2 digits')
    
    return error_messages


pasword = input()
list_with_error_messages = password_validator(pasword)
if list_with_error_messages:
    print('\n'.join(list_with_error_messages))
else:
    print('Password is valid')