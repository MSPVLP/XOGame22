X_SYM = "X"
O_SYM = "O"

def is_already_picked(board, move):
    """
    :param board:pass the input(board)
    :move -
    :return:if already picked return true or return false
    """
    row = move[0]
    column = move[1]
    if board[row][column] == X_SYM or board[row][column] == O_SYM:
        return True
    else:
        return False


def out_of_range(board2, move):
    """
    :param board2:pass the input(board)
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
    :param board:pass the input(board)
    :param move:
    :param sym:
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
    move1 = (0, 1)
    move2 = (1, 0)
    sym1 = "X"
    assert make_move(board1, move1, sym1) == True
    assert make_move(board1, move1, sym1) == False

    print("Test passed")


if __name__ == "__main__":
    test_make_move()





