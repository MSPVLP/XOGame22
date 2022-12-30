X_SYM = "X"
O_SYM = "O"
Match = "False"
def check_win(board, player_sym1, player_sym2):
    """
    This function used to display win a player
    :param board:Nested list
    :param player_sym1:char
    :param player_sym2: char
    :return:player_sym1 or player_sym2
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


def test_check_win():
    assert check_win([['O', 'X', 'X'], ['X', 'O', 'X'], ['O', 'O', 'X']], 'X', 'O') == X_SYM
    assert check_win([['X', 'O', 'O'], ['X', 'X', 'X'], ['O', 'X', 'O']], 'O', 'X') == X_SYM
    assert check_win([['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'X']], 'X', 'O') == O_SYM
    assert check_win([['O', 'X', 'O'], ['O', 'X', 'X'], ['X', 'X', 'O']], 'O', 'X') == X_SYM
    assert check_win([['O', 'X', 'X'], ['O', 'O', 'X'], ['X', 'X', 'X']], 'X', 'O') == X_SYM
    assert check_win([['O', 'O', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']], 'X', 'O') == O_SYM
    assert check_win([['O', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'O']], 'X', 'O') == O_SYM
    assert check_win([['O', 'X', 'O'], ['X', 'O', 'O'], ['X', 'X', 'O']], 'X', 'O') == O_SYM
    assert check_win([['X', 'O', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']], 'X', 'O') == X_SYM
    assert check_win([['X', 'X', 'X'], ['O', 'O', 'X'], ['X', '0', 'X']], 'X', 'O') == X_SYM
    assert check_win([['X', 'O', 'O'], ['X', 'X', 'O'], ['O', 'O', 'X']], 'X', 'O') == X_SYM
    assert check_win([['O', 'X', 'X'], ['O', 'O', 'X'], ['X', 'O', 'O']], 'O', 'X') == O_SYM
    assert check_win([['O', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']], 'X', 'O') == O_SYM
    assert check_win([['O', 'X', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']], 'O', 'X') == X_SYM
    assert check_win([['X', 'O', 'X'], ['O', 'O', 'O'], ['O', 'X', 'O']], 'X', 'O') == O_SYM

    print("Board is Validate")


if __name__ == '__main__':
        test_check_win()


