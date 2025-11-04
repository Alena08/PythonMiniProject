global board
board = ["-","-","-","-","-","-","-","-","-"]
play= True
currentPlayer = "X"
winner=None
 
def printBoard():
    """
    -------------
    | * | * | * |
    -------------
    | * | * | * |
    -------------
    | * | * | * |
    -------------
    """

    # print("-"*13)
    # for i in range(9):
    #     if i in[0,3,6]:
    #         print("| "+ board[i]+ " | "+board[i+1]+ " | "+board[i+2]+ " |") 
    #         print("-"*13)
    print("+-------" * 3,"+", sep="")
    for i in range(9):
        if i in[0,3,6]:
            print("|       " * 3,"|", sep="")
            print("|   "+ board[i]+ "   |   "+board[i+1]+ "   |   "+board[i+2]+ "   |") 
            #print("|   " + str(board[row][col]) + "   ", end="")
            #print("|")
            print("|       " * 3,"|",sep="")
            print("+-------" * 3,"+",sep="")

def playGame():
    while True:
        a = input("Gib Number von 1 bis 9")
        if a.isdigit():
            a = int(a)
            if a in range(1,10):
                if board[a-1] == "-":
                    board[a-1] = currentPlayer
                    break
                else:
                    print("Position is occupide")
        else:
            print("gib richtige number!")

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer="X"
 
def checkHorzWin():
    global winner
    if (board[0]== board[1] ==board[2]) and board[0] != "-":
        winner  = board[0]
        return True
    elif (board[3]== board[4] ==board[5]) and board[3] != "-":
        winner  = board[3]
        return True
    elif (board[6]== board[7] ==board[8]) and board[6] != "-":
        winner  = board[4]
        return True
        
 
def checkVerWin():
    global winner
    if (board[0]== board[3] ==board[6]) and board[0] != "-":
        winner  = board[0]
        return True
    elif (board[1]== board[4] ==board[7]) and board[1] != "-":
        winner  = board[1]
        return True
    elif (board[2]== board[5] ==board[8]) and board[2] != "-":
        winner  = board[2]
        return True
 
def checkDiagWin():
    global winner
    if (board[0]== board[4] ==board[8]) and board[0] != "-":
        winner  = board[0]
        return True
    elif (board[2]== board[4] ==board[6]) and board[2] != "-":
        winner  = board[1]
        return True
 
def checkWin():
    global play
    if(checkHorzWin() or checkVerWin() or checkDiagWin()):
        play = False
        print(f"Spieler {winner} hat gewonnen!")
        return True
 
def checkTie():
    global play
    if "-" not in board:
        print("Unentscheiden!")
        play = False
        return True

        
 
while play:
    printBoard()
    playGame()
    if checkWin():
        printBoard()
    if checkTie():
        printBoard()
    switchPlayer()

