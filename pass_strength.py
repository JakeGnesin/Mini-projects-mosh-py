# strength = 0


# def main():
#     while True:
#         password = input('Enter a passwrod 8 characters long: ')
#         if password == list(range(9)):
#             check_pass()
#         else:
#             print('Invalid password, must be only 8 characters long')

# def check_pass():
#     if strength == 1:
#         print('Very Weak')
#     elif strength == 2:
#         print('Weak')
#     elif strength == 3:
#         print('Medium')
#     elif strength == 4:
#         print('strong')
#     elif strength == 5:
#         print('Very strong')


# main()

# # check for upper and lower case and spec char using reg expression
# # add to strength based on ^

import re


def check_pass(password):
    strength = 0

    # Check if password is exactly 8 digits
    if len(password) == 8 and password.isdigit():
        return 'Very Weak'

    # Base strength for minimum length (8 characters)
    if len(password) >= 8:
        strength += 1

    # Check for different character types using regex
    if re.search(r'[A-Z]', password):  # Uppercase
        strength += 1
    if re.search(r'[a-z]', password):  # Lowercase
        strength += 1
    if re.search(r'[0-9]', password):  # Numbers
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Special characters
        strength += 1

    # Evaluate strength
    strength_messages = {
        1: 'Very Weak',
        2: 'Weak',
        3: 'Medium',
        4: 'Strong',
        5: 'Very Strong'
    }

    return strength_messages.get(strength, 'Invalid')


def main():
    while True:
        password = input('Enter a password (minimum 8 characters): ')
        if len(password) < 8:
            print('Invalid password, must be at least 8 characters long')
        else:
            result = check_pass(password)
            print(f'Password strength: {result}')


if __name__ == '__main__':
    main()
