def is_solved(board):
    horizontal1 = [board[0][0], board[0][1],board[0][2]]
    horizontal2 = [board[1][0], board[1][1],board[1][2]]
    horizontal3 = [board[2][0], board[2][1],board[2][2]]
    vertical1 = [board[0][0], board[1][0], board[2][0]]
    vertical2 = [board[0][1], board[1][1], board[2][1]]
    vertical3 = [board[0][2], board[1][2], board[2][2]]
    diag1 = [board[0][0],board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    winconditions = [horizontal1,horizontal2,horizontal3, vertical1,vertical2, vertical3, diag1, diag2]
    for i in winconditions:
        if i[0] == 1 and i[1] == 1 and i[2] == 1:
            return 1
        if i[0] == 2 and i[1] == 2 and i[2] == 2:
            return 2
    for i in board:
        for j in i:
            if j == 0:
                return -1
    return 0
