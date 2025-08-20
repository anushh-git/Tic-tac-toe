board = [' ' for _ in range(9)]
def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    while True:
        print("Your turn player {}".format(number))
        move = input("Enter your move (1-9): ")

        if not move.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Invalid move. Please enter a number between 1 and 9.")
        elif board[move - 1] != ' ':
            print("Sorry, this space is taken!")
        else:
            board[move - 1] = icon
            break
def is_victory(icon):
    return (
        (board[0] == icon and board[1] == icon and board[2] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        (board[0] == icon and board[3] == icon and board[6] == icon) or
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[0] == icon and board[4] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon)
    )
while True:
    print_board()
    player_move('X')
    if is_victory('X'):
        print_board()
        print("Player 1 wins! Congratulations!")
        break
    elif ' ' not in board:
        print_board()
        print("It's a tie!")
        break
    print_board()
    player_move('O')
    if is_victory('O'):
        print_board()
        print("Player 2 wins! Congratulations!")
        break
    elif ' ' not in board:
        print_board()
        print("It's a tie!")
        break
