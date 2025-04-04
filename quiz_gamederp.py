import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'


def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)

    return input('Your answer: ').upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(
            index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint(f'Wrong! the correct answer is {item[ANSWER]}', 'red')

            print()

    print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


def main():
    quiz = [
        {
            QUESTION: 'What is the capital of France?',
            OPTIONS: ['A. Rome', 'B. Paris', 'C. Ottawa', 'D. Dootberg'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'What is the red planet?',
            OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Pluto'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'Who is the king?',
            OPTIONS: ['A. Trump', 'B. Elon', 'C. Obombna', 'D. Gay boy'],
            ANSWER: 'A'
        }
    ]

    run_quiz(quiz)


if __name__ == '__main__':
    main()
