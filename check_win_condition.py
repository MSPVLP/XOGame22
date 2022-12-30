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


if __name__ == '__main__':
    p1 = [['o', 'x', 'x'], ['x', 'o', 'x'], ['o', 'o', 'x']]
    result = check_win(p1, 'x', 'o')
    if result == 'o':
        print("o win")
    elif result == 'x':
        print("x win")
    elif result == None:
        print("Match draw!")
