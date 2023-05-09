# -----------TicTacToe's function--------------------------------

def is_3_aligned(board):
    # check if a player has won

    # checks if a row is filled by a player
    for i in range(3):
        # checks if a row is filled by a player
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True

        # checks if a row is filled by a player
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True

    # checks if diagonal left to right is filled by a player
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True

    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True

    return False
