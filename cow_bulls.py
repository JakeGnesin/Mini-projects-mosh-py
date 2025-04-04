# import random

# correct_num = random.randint(1000-9999)


# def gen_numb():
#     while True:
#         number_guess = input('I have a num 4 digits unique, guess: ')
#         if number_guess not in correct_num:
#             print('Invalid guess, needs to be 1000-9999')


# def check_cows_bulls(number_guess):
#     if number_guess == correct_num:
#         print('Correct!')
#     elif number_guess[0] == correct_num[0]:
#         print('1 bull, 3 cows')
#     elif number_guess[0, 1] == correct_num[0, 1]:
#         print('2 bulls, 2 cows')
#     elif number_guess[0, 1, 2] == correct_num[0, 1, 2]:
#         print('3 bulls, 1 cow')


# def main():
#     gen_numb()
#     check_cows_bulls()

import random

# Generate a 4-digit number with unique digits
digits = list(range(10))  # 0-9
random.shuffle(digits)
correct_num = ''.join(map(str, digits[:4]))  # Take first 4 shuffled digits


def gen_numb():
    while True:
        number_guess = input(
            'I have a 4-digit number with unique digits, guess: ')
        if (len(number_guess) != 4 or
            not number_guess.isdigit() or
                len(set(number_guess)) != 4):
            print(
                'Invalid guess, must be a 4-digit number (1000-9999) with unique digits')
            continue
        return number_guess


def check_cows_bulls(number_guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if number_guess[i] == correct_num[i]:
            bulls += 1
        elif number_guess[i] in correct_num:
            cows += 1

    if bulls == 4:
        print('Correct!')
        return True
    else:
        print(f'{bulls} bulls, {cows} cows')
        return False


def main():
    while True:
        guess = gen_numb()
        if check_cows_bulls(guess):
            break


if __name__ == "__main__":
    main()
