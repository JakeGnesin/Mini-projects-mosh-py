# import random
# import re


# nums = list(range(9))
# chars_upper = list(range('A-Z'))
# specials = (r'!@#$%^&_-')


# def check_pass():
#     while True:
#             pass_len = input('Enter pass length: ')
#             upper_case =  input('Use upper case? (y/n): ')
#             if upper_case == 'y':
#                 # logic to use upper case
#                 use_nums = input('Use nums? (y/n): ')
#                 if use_nums == 'y':
#                     # logic to use numbers
#                     spec_chars = input('Use special chars? (y/n): ')
#                     if spec_chars == 'y':
#                         # logic to use special characters
#         return password


# def main():
#     password = check_pass()


# if __name__ == '__main__':
#     main()

# //////////////////////


import random
import string


def create_pass():
    # Define character sets
    nums = string.digits  # '0123456789'
    chars_upper = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars_lower = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    specials = '!@#$%^&*_-'

    while True:
        try:
            # Get password length
            pass_len = int(input('Enter password length (minimum 8): '))
            if pass_len < 8:
                print("Password length must be at least 8 characters")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    # Initialize character pool with lowercase (minimum requirement)
    char_pool = list(chars_lower)
    password = []

    # Upper case option
    upper_case = input('Use upper case? (y/n): ').lower()
    if upper_case == 'y':
        char_pool.extend(chars_upper)
        # Ensure at least one uppercase
        password.append(random.choice(chars_upper))

    # Numbers option
    use_nums = input('Use numbers? (y/n): ').lower()
    if use_nums == 'y':
        char_pool.extend(nums)
        password.append(random.choice(nums))  # Ensure at least one number

    # Special characters option
    spec_chars = input('Use special characters? (y/n): ').lower()
    if spec_chars == 'y':
        char_pool.extend(specials)
        password.append(random.choice(specials))  # Ensure at least one special

    # Fill remaining length with random characters from pool
    remaining_length = pass_len - len(password)
    password.extend(random.choice(char_pool) for _ in range(remaining_length))

    # Shuffle the password
    random.shuffle(password)

    # Join characters into final password
    return ''.join(password)


def main():
    while True:
        password = create_pass()
        print(f"Generated password: {password}")

        # Ask if user wants another password
        again = input("Generate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
