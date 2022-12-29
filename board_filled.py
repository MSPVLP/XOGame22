

def is_board_filled(board1):
    """
    :param board1: nested list
    :return: check whether the board is filled or not
    """
    is_filled = False
    for i in range(3):
        if board[i][0] == '' or board[i][1] == '' or board[i][2] == '':
            return True
    else:
        return False


if __name__ == "__main__":
    board = [["x", "o", "x"], ["x", "", "x"], ["x", "o", "o"]]
    var = is_board_filled(board)
    if var:
        print("board not filled")
    else:
        print("board filled")












