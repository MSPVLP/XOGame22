X_SYM = "X"
O_SYM = "O"

def is_already_picked(board, move):
    """

    :param board:pass the input(board in list)
    :param move:tuple that contains row and column number
    :return:if already picked return true,or return false
    """
    row = move[0]
    column = move[1]
    if board[row][column] == X_SYM or board[row][column] == O_SYM:
        return True
    else:
        return False


def out_of_range(board2, move):
    """
    :param board2:pass the input(board in list)
    :param move:tuple that contains row and column number
    :return:if out of range,return true or return false
    """
    row = move[0]
    column = move[1]
    if (row < 3 and column < 3) and (row > 0 and column > 0):
        return True
    else:
        return False


def make_move(board, move, sym):
    """
    :param board:pass the input(board in list)
    :param move:tuple that contains row and column number
    :param sym:pass the input(symbol x,o)
    """
    if out_of_range(board, move) or is_already_picked(board, move):
        return False
    else:
        row = move[0]
        column = move[1]
        board[row][column] = sym
        return True

def test_make_move():
    board1 = [[' ', ' ', ' '], ['O', ' ', ' '], [' ', ' ', ' ']]
    move1 = (0, 0)
    move2 = (1, 0)
    sym1 = "X"
    sym2 = "O"
    assert make_move(board1, move1, sym1) == True
    assert make_move(board1, move2, sym2) == False
    board2 = [[' ', ' ', ' '], ['O', 'O', ' '], [' ', ' ', ' ']]
    move3 = (0, 1)
    move4 = (1, 1)
    sym3 = "X"
    sym4 = "O"
    assert make_move(board2, move3, sym3) == True
    assert make_move(board2, move4, sym4) == False
    board3 = [[' ', ' ', ' '], ['O', ' ', 'O'], [' ', ' ', ' ']]
    move5 = (0, 2)
    move6 = (1, 2)
    sym5 = "X"
    sym6 = "O"
    assert make_move(board3, move5, sym5) == True
    assert make_move(board3, move6, sym6) == False
    board4 = [[' ', ' ', ' '], ['O', ' ', ' '], [' ', 'O', ' ']]
    move7 = (2, 0)
    move8 = (2, 1)
    sym7 = "X"
    sym8 = "O"
    assert make_move(board4, move7, sym7) == True
    assert make_move(board4, move8, sym8) == False





    print("Test passed")


if __name__ == "__main__":
    test_make_move()





