from rich import print
from copy import copy

def printBoard(board):
    out = ""
    for space in board:
        if space == "X":
            out += "[green]X[/green]"
        elif space == "Z":
            out += "[red]Z[/red]"
        else:
            out += "[blue]" + space + "[/blue]"
    print(out)

def checkWin(board):
    joinedBoard = "".join(board)
    if "XXX" in joinedBoard:
        return False
    if "ZZZ" in joinedBoard:
        return True
    if "0" not in joinedBoard:
        return False

def minimax(board, depth, player):
    if depth > 0:
        for i in range(len(board)):
            slot = board[i]
            if slot != "0":
                continue
            newboard = copy(board)
            newboard[i] = "Z" if not player else "X"
            #print("TEST", newboard)
            if minimax(newboard, depth - 1, not player):
                return i
        return -1 #If cannot win then give up by returning -1
    return checkWin(board)

board = ["0"] * 10

while True:

    printBoard(board)

    #Get and set player move
    while True:
        playerMove = int(input("Which slot (zero index)?: "))
        if playerMove >= 0 and playerMove < len(board) and board[playerMove] == "0":
            break
        print("PLEASE CHOOSE A VALID POSITION\n")
    board[playerMove] = "X"
    
    #CPU turn
    m = minimax(board, board.count("0"), False)
    if m == -1:
        print("CPU Gives Up")
        break
    board[m] = "Z"

    #Check win
    joinedBoard = "".join(board)

    if "0" not in joinedBoard or ("XXX" in joinedBoard and "ZZZ" in joinedBoard):
        printBoard(board)
        print("It's a Tie!")
        break
    if "XXX" in joinedBoard:
        printBoard(board)
        print("Player Wins")
        break
    if "ZZZ" in joinedBoard:
        printBoard(board)
        print("CPU Wins")
        break
