# import random

# slot_options = {'cherry': '🍒', 'star': '⭐️', 'music': '🎵'}

# total__amount = 0


# def betting(total_money):
#     while True:
#         try:
#             bet = input('Enter bet: ')
#             if bet > total_money:
#                 print('You do not have enough for this bet')
#                 continue
#         except ValueError:
#             print('Invalid bet')
#             break


# def slot_spin(bet, total_money, total_amount):
#     while True:
#         if bet:
#             spin = random.choice(slot_options[0:2])
#             if spin(range(1)):
#                 total__amount += bet * 2
#             print(f'{spin}')
#             print(f'you won, you have {total__amount}')
#         if spin(range(2)):
#             total__amount += bet * 10
#             print(f'You won, you have {total__amount}')
#         elif spin != set(slot_options):
#             total__amount -= bet
#             print('You lose')


# def play_again():
#     spin_again = input('Play again? (y/n): ')
#     if spin_again == 'y':
#         betting()
#         slot_spin()


# def main():
#     while True:
#         try:
#             total_money = input('Enter an amount to play with: ')
#             total__amount += total_money
#         except ValueError:
#             print('Invalid amount')
#             continue
#         betting()
#         slot_spin()
#         play_again()


# if __name__ == '__main__':
#     main()


# /////////////


import random

# Define slot symbols and their payouts
slot_options = {
    'cherry': {'symbol': '🍒', 'payout': 2},
    'star': {'symbol': '⭐️', 'payout': 5},
    'music': {'symbol': '🎵', 'payout': 10}
}
symbols = list(slot_options.keys())


def betting(total_money):
    while True:
        try:
            bet = float(input('Enter bet: '))
            if bet <= 0:
                print('Bet must be greater than 0')
                continue
            if bet > total_money:
                print('Not enough money for this bet')
                continue
            return bet
        except ValueError:
            print('Please enter a valid number')
            continue


def slot_spin(bet, total_money):
    # Spin three reels
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    # Display the spin result
    result = f"{slot_options[reel1]['symbol']} | {slot_options[reel2]['symbol']} | {slot_options[reel3]['symbol']}"
    print(f"\nSpin result: {result}")

    # Calculate winnings
    if reel1 == reel2 == reel3:  # Three matching symbols
        winnings = bet * slot_options[reel1]['payout']
        total_money += winnings
        print(f"Jackpot! Three {reel1}s! You won ${winnings:.2f}")
    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:  # Two matching symbols
        winnings = bet * 0.5
        total_money += winnings
        print(f"Two matches! You won ${winnings:.2f}")
    else:  # No matches
        total_money -= bet
        print(f"No match. You lost ${bet:.2f}")

    return total_money


def play_again():
    while True:
        response = input('Play again? (y/n): ').lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' or 'n'")


def main():
    # Get initial money
    while True:
        try:
            total_money = float(input('Enter an amount to play with: $'))
            if total_money <= 0:
                print('Amount must be greater than 0')
                continue
            break
        except ValueError:
            print('Please enter a valid number')

    print(f"Starting balance: ${total_money:.2f}")

    # Main game loop
    while total_money > 0:
        bet = betting(total_money)
        total_money = slot_spin(bet, total_money)
        print(f"Current balance: ${total_money:.2f}")

        if total_money <= 0:
            print("You're out of money! Game Over!")
            break

        if not play_again():
            print(f"Game ended. Final balance: ${total_money:.2f}")
            break


if __name__ == '__main__':
    main()
