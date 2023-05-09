import data as d


def is_a_board_finished(board, player):
    """check if a little board is finished and then if the game is entirely over"""

    # Get the sign of the player
    if player == 1:
        sign = d.player1_sign
    elif player == 2:
        sign = d.player2_sign

    is_complete_game_finished = False

    # check if the little boards are finished



    counter = 0
    for lst in board:
        # If the board is not finished check if finished
        if len(lst) == 9:

            for i in range(0, 9, 3):
                # if a row is completed
                if lst[i] == lst[i+1] == lst[i+2] != 0:
                    board[counter] = sign
                    break

            for i in range(3):
                # if a column is completed
                if lst[i] == lst[i+3] == lst[i+6] != 0:
                    board[counter] = sign
                    break

            # if a diagonal is completed
            if lst[2] == lst[4] == lst[6] != 0 or lst[0] == lst[4] == lst[8] != 0:
                board[counter] = sign
                break
            


            #check if the box is full => draw
            counter_signs = 0   # if equal to 9 and no alignment there is a draw
            for i in range(9):
                # if the box contains a sign add 1 to counter_sign
                if lst[i] == d.player1_sign or lst[i] == d.player2_sign:
                    counter_signs +=1
                    
                    if counter_signs == 9:
                        board[counter] = "G"

                    
        counter += 1
        
        


 



    # Check if the big board if finished
    
    for i in range(0, 9, 3):
        # if a row is completed
        if board[i] == board[i+1] == board[i+2] == sign:
            is_complete_game_finished = True

    for i in range(3):
        # if a column is completed
        if board[i] == board[i+3] == board[i+6] == sign:
            is_complete_game_finished = True

    # if a diagonal is completed
    if board[2] == board[4] == board[6] == sign or board[0] == board[4] == board[8] == sign:
        is_complete_game_finished = True
        
    
    

    return board, is_complete_game_finished
