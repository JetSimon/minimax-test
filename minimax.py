def minimax(board, depth, player):
    if depth > 0:
        best = 0
        for i in range(len(board)):
            slot = board[i]
            if slot != "0":
                continue
            newboard = board.copy()
            newboard[i] = "Z" if not player else "X"
            attempt = minimax(board, depth - 1, not player)
    return (move, score)

board = ["0"] * 7

while True:

    print(board)

    #Get and set player move
    while True:
        playerMove = int(input("Which slot (zero index)?: "))
        if playerMove > 0 and playerMove < len(board) and board[playerMove] == "0":
            break
        print("PLEASE CHOOSE A VALID POSITION\n")
    board[playerMove] = "X"
    
    #CPU turn
    board[minimax(board, 2, False)[0]] = "Z"

    #Check win
    joinedBoard = "".join(board)
    if "XXX" in joinedBoard:
        print("Player Wins")
        break
    if "ZZZ" in joinedBoard:
        print("CPU Wins")
        break
    if "0" not in joinedBoard:
        print("It's a Tie!")
        break