

def is_already_picked(board1):
    """
    :param board1:pass the input(board)
    :return:if already picked return true or return false
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] != '':
                return True
            else:
                return False


def out_of_range(board2):
    """
    :param board2:pass the input(board)
    :return:if out of range,return true or return false
    """
    for i in range(3):
        for j in range(3):
            if board[i] < 3 and board[j] < 3:
                return True
            else:
                return False


def make_move(board3, move, sym):
    """
    :param board3:pass the input(board)
    :param move:
    :param sym:
    """
    if out_of_range(board3) or is_already_picked(board3):
        print("Pick the correct one")
    else:
        row = move[0]
        column = move[1]
        board[row][column] = sym


if __name__ == "__main__":
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    make_move(board,(1,0),"X")






