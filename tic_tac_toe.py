row_one = [' ', ' ', ' ']
row_two = [' ', ' ', ' ']
row_three = [' ', ' ', ' ']


def board():
    print('-' * 3 + '+' + '-' * 3 + '+' + '-' * 3)
    print(f' {row_one[0]} | {row_one[1]} | {row_one[2]} ')
    print('-' * 3 + '+' + '-' * 3 + '+' + '-' * 3)
    print(f' {row_two[0]} | {row_two[1]} | {row_two[2]} ')
    print('-' * 3 + '+' + '-' * 3 + '+' + '-' * 3)
    print(f' {row_three[0]} | {row_three[1]} | {row_three[2]} ')
    print('-' * 3 + '+' + '-' * 3 + '+' + '-' * 3)


def get_columns():
    column_one = [row_one[0], row_two[0], row_three[0]]    # Left column
    column_two = [row_one[1], row_two[1], row_three[1]]    # Middle column
    column_three = [row_one[2], row_two[2], row_three[2]]  # Right column
    return column_one, column_two, column_three


def check_win(player):
    # Check rows
    if row_one == [player, player, player] or \
       row_two == [player, player, player] or \
       row_three == [player, player, player]:
        return True

    # Check columns
    columns = get_columns()
    if columns[0] == [player, player, player] or \
       columns[1] == [player, player, player] or \
       columns[2] == [player, player, player]:
        return True

    # Check diagonals
    if [row_one[0], row_two[1], row_three[2]] == [player, player, player] or \
       [row_one[2], row_two[1], row_three[0]] == [player, player, player]:
        return True

    return False

# Function to check if the board is full (draw)


def is_board_full():
    return ' ' not in row_one and ' ' not in row_two and ' ' not in row_three


rows = ['0', '1', '2']

player_x_turn = True

board()


while True:
    if player_x_turn:
        print('Player X turn')
        player = 'X'
    else:
        print('Player O turn')
        player = 'O'

    player_input_row = input('Enter a row (0-2): ')
    player_input_col = input('Enter a column (0-2): ')

    if player_input_row in rows and player_input_col in rows:
        row_idx = int(player_input_row)
        col_idx = int(player_input_col)
        # Map input to the correct row and place X or O
    if row_idx == 0:
        if row_one[col_idx] == ' ':  # Check if cell is empty
            row_one[col_idx] = 'X' if player_x_turn else 'O'
        else:
            print("Cell already taken!")
            continue
    elif row_idx == 1:
        if row_two[col_idx] == ' ':  # Check if cell is empty
            row_two[col_idx] = 'X' if player_x_turn else 'O'
        else:
            print("Cell already taken!")
            continue
    elif row_idx == 2:
        if row_three[col_idx] == ' ':  # Check if cell is empty
            row_three[col_idx] = 'X' if player_x_turn else 'O'
        else:
            print("Cell already taken!")
            continue
    else:
        print('Invalid input')
        continue

    board()

    if check_win(player):
        print(f'Player {player} wins!')
        break

    # Check for a draw
    if is_board_full():
        print("It's a draw!")
        break

    player_x_turn = not player_x_turn
