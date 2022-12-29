X_SYM = 'X'
O_SYM = 'o'


def game_main():
    board = get_board()

    player = X_SYM      # X is first player

    game_result = False

    while not game_result:
        print_board(board)                      # display current board

        # loop and get next move
        move_valid = False
        while not move_valid:
            move = get_move(board,player)       # get next move
            move_valid = make_move(board,move)  # make move
            if not move_valid:
                print("Enter valid move.")          # move is invalid. loop and get again

        game_result = check_win()
        if game_result == X_SYM:
            print("X Wins!")
        elif game_result == O_SYM:
            print("O Wins!")
        elif game_result == None:
            print("Game draw!")
        else:
            player = X_SYM if player == O_SYM else O_SYM

    print("Thank you for playing.")


if __name__ == "__main__":
    game_main()
