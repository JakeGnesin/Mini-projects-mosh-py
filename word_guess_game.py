# import random
# import string

# letter_options = string.ascii_lowercase

# words = ('dumb', 'cunt', 'earth', 'puppy', 'melatonin')

# empty_word_guess = []

# generated_word = random.choice(words)


# def form_guess(letter_guess):
#     if letter_guess in generated_word:
#         empty_word_guess.append(letter_guess[generated_word])
#     else:
#         print('Wrong guess')


# def main():
#     while True:
#         letter_guess = input('Enter a letter: ').lower()
#         if letter_guess != letter_options:
#             print('Please use letter only')
#             continue
#         else:
#             break

# #// if wrong 10 times print game over, the answer was ...
# #// if word guessed right, print Correct! game over


# if __name__ == '__main__':
#     main()

# ///////////


import random
import string

letter_options = string.ascii_lowercase
words = ('dumb', 'cunt', 'earth', 'puppy', 'melatonin')

# Initialize the game
generated_word = random.choice(words)
# Creates list of underscores matching word length
empty_word = ['_' for _ in generated_word]
wrong_guesses = 0
max_wrong = 10
guessed_letters = set()  # To track already guessed letters


def form_guess(letter_guess):
    global wrong_guesses
    if letter_guess in guessed_letters:
        print(f"You've already guessed '{letter_guess}'")
        return

    guessed_letters.add(letter_guess)

    if letter_guess in generated_word:
        # Update all matching positions
        for i, letter in enumerate(generated_word):
            if letter == letter_guess:
                empty_word[i] = letter_guess
        print(' '.join(empty_word))
    else:
        wrong_guesses += 1
        remaining = max_wrong - wrong_guesses
        print(f"Wrong guess! {remaining} attempts left")
        print(' '.join(empty_word))


def main():
    print("Welcome to Word Guess!")
    print(' '.join(empty_word))

    while wrong_guesses < max_wrong:
        letter_guess = input('Enter a letter: ').lower()

        # Check if input is valid
        if len(letter_guess) != 1 or letter_guess not in letter_options:
            print('Please enter a single letter')
            continue

        form_guess(letter_guess)

        # Check win condition
        if '_' not in empty_word:
            print(f"Correct! You won! The word was '{generated_word}'")
            break

    # Check lose condition
    if wrong_guesses >= max_wrong:
        print(f"Game Over! The answer was '{generated_word}'")


if __name__ == '__main__':
    main()
