
def is_board_filled(board):
    """
    :param board: nested list
    :return: It returns True if board not filled
             Returns False if board filled
    """
    is_filled = False
    for i in range(3):
        if board[i][0] == ' ' or board[i][1] == ' ' or board[i][2] == ' ':
            return True
    else:
        return False


def test_board_filled():
    board1 = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "O"]]
    assert is_board_filled(board1) == False
    board2 = [["X", " ", "X"], ["X", "O", "X"], ["X", "O", "O"]]
    assert is_board_filled(board2) == True
    board3 = [["X", "O", " "], ["X", "O", "X"], ["X", "O", "O"]]
    assert is_board_filled(board3) == True
    board4 = [["X", "O", "X"], ["X", "O", " "], ["X", "O", "O"]]
    assert is_board_filled(board4) == True
    board5 = [["X", " ", "X"], ["X", "O", "X"], ["X", "O", "O"]]
    assert is_board_filled(board5) == True
    print("Test passed")


if __name__ == "__main__":
    test_board_filled()
