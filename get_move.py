

def get_move(player):
    print("This is", player, "turn.")
    row = int(input("Enter a row:"))
    column = int(input("Enter a column:"))
    move = (row, column)
    return move


if __name__ == "__main__":
    board = [["x", "o"], ["o", "x"]]
    move1 = get_move("player2")
    print(move1)

