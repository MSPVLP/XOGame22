def swap_player_turn(player1):
    """
    :param:pass the input(player) from user
    :return:swap the player turn
    """
    if player1 == "X":
        return "O"
    else:
        return "X"


if __name__ == "__main__":
    player = input("Enter option X or O:")
    player_new = swap_player_turn(player)
    print(player_new)

