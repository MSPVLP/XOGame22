

def print_board(board):
    n = len(board)
    for i in range(n):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('_____________')


if __name__ == "__main__":
    board = [['x', 'o', 'x'], ['o', 'x', 'x'], ['o', 'x', 'x']]
    print_board(board)
