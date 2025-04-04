import random

dice_numbs = (1, 2, 3, 4, 5, 6)


def main():
    doot_score = 0
    skits_score = 0

    print('Player Doots turn')
    doot_score, game_over = roll_dice(doot_score, "Doot", skits_score)

    print('Player Skits\'s turn')
    if game_over and doot_score == 0:  # If Doot rolled a 1
        # Force at least one roll for Skits
        roll = random.choice(dice_numbs)
        print(f'You rolled a {roll}')
        skits_score = keep_score(skits_score, roll, "Skits")
        if roll != 1:  # If Skits doesn't roll a 1, ask to roll again
            skits_score, _ = roll_dice(skits_score, "Skits", doot_score)
    else:
        skits_score, _ = roll_dice(skits_score, "Skits", doot_score)

    compare_scores(doot_score, skits_score)


def roll_dice(score, player, other_player_score):
    while True:
        roll = random.choice(dice_numbs)
        print(f'You rolled a {roll}')
        score = keep_score(score, roll, player)

        if roll == 1:
            return score, True  # Game over if roll is 1

        continue_rolling = input('Roll again? (y/n): ').lower()
        if continue_rolling == 'n':
            print(f'\nPlayer {player} final score: {score}')
            return score, False  # Game continues
        elif continue_rolling != 'y':
            print('\nInvalid choice. Please enter y or n')
            # Loop continues, asking for input again


def keep_score(score, roll, player):
    """Update and maintain the player's score based on the roll"""
    if roll == 1:
        score = 0
        print('Tough Luck Pig')
        print(f'\nCurrent score: {score}')
        return score
    else:
        score += roll
        print(f'Current score: {score}')
        return score


def compare_scores(doot_score, skits_score):
    """Compare final scores and declare the winner"""
    print(f'\nFinal Scores:')
    print(f'Player Doot: {doot_score}')
    print(f'Player Skits: {skits_score}')

    if doot_score > skits_score:
        print('Player Doot wins!')
    elif skits_score > doot_score:
        print('Player Skits wins!')
    else:
        print('It\'s a tie!')


if __name__ == "__main__":
    main()
