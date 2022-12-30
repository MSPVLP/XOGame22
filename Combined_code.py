X_SYM = 'X'
O_SYM = 'O'
p1 = "Player 1"
p2 = "Player 2"


def game_main():
    board = get_board()
    sym = X_SYM  # X is first player
    player = p1
    game_result = False

    while not game_result:
        print_board(board)  # display current board

        # loop and get next move
        move_valid = False
        while not move_valid:
            move = get_move(player)  # get next move
            move_valid = make_move(board, move, sym)  # make move
            if not move_valid:
                print("Enter valid move.")  # move is invalid. loop and get again

        game_result = check_win(board, X_SYM, O_SYM)
        if game_result == X_SYM:
            print("X Wins!")
        elif game_result == O_SYM:
            print("O Wins!")
        elif game_result is None:
            print("Game draw!")
        if sym == O_SYM:
            sym = X_SYM
            player = p1
        else:
            sym = O_SYM
            player = p2

    print("Thank you for playing.")


def get_board():
    """
    :return list - return the board
    """
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return game_board


def get_move(player):
    print("This is", player, "turn.")
    while True:
        try:
            row = int(input("Enter a row:"))
            column = int(input("Enter a column:"))
            move = (row, column)
            return move
            break
        except ValueError:
            print("Enter valid number")


def make_move(board, move, sym):
    if out_of_range(board, move, sym):
        return False
    elif is_already_picked(board, move, sym):
        return False
    else:
        if is_board_not_filled(board):
            row = move[0]
            column = move[1]
            board[row][column] = sym
            return True
        else:
            return False


def is_already_picked(board, move, sym):
    row = move[0]
    column = move[1]
    if (board[row][column] == X_SYM) or (board[row][column] == O_SYM):
        return True
    else:
        return False


def out_of_range(board, move, sym):
    row = move[0]
    column = move[1]
    if (row > 2 or row < 0) or (column > 2 or column < 0):
        return True
    else:
        return False


def is_board_not_filled(board):
    """
    This function is used to check whether a board is filled or not.
    :param board: nested list
    :return: bool - It returns True if the board is not filled. Otherwise returns False.
    """
    is_filled = False
    for i in range(3):
        if board[i][0] != '' or board[i][1] != '' or board[i][2] != '':
            return True
    else:
        return False


def check_win(board, player_sym1, player_sym2):
    """
    This function is used to display a player result.
    :param board:Nested list
    :param player_sym1:char
    :param player_sym2: char
    :return:char - player_sym1 or player_sym2
    """

    n = len(board)
    win = None
    # check row wise
    for i in range(n):
        if board[i][0] == player_sym1 and board[i][1] == player_sym1 and board[i][2] == player_sym1:
            return player_sym1
        elif board[i][0] == player_sym2 and board[i][1] == player_sym2 and board[i][2] == player_sym2:
            return player_sym2
    # check column wise
    for j in range(n):
        if board[0][j] == player_sym1 and board[1][j] == player_sym1 and board[2][j] == player_sym1:
            return player_sym1
        elif board[0][j] == player_sym2 and board[1][j] == player_sym2 and board[2][j] == player_sym2:
            return player_sym2
    # check diagonals wise
    if (board[0][0] == player_sym1 and board[1][1] == player_sym1 and board[2][2] == player_sym1) or (
            board[0][0] == player_sym2 and board[1][1] == player_sym2 and board[2][2] == player_sym2):
        return player_sym1
    elif (board[0][2] == player_sym1 and board[1][1] == player_sym1 and board[2][0] == player_sym1) or (
            board[0][2] == player_sym2 and board[1][1] == player_sym2 and board[2][0] == player_sym2):
        return player_sym2


def print_board(board):
    n = len(board)
    print('----+---+---')
    for i in range(n):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('----+---+---')


if __name__ == "__main__":
    game_main()
