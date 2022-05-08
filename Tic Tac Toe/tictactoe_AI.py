# X is player and O is AI 
# X = Minimiaser
# O = Maximiaser
from math import inf
from time import sleep
player = 'x'
opponent = 'o'
one = (0,0)
two = (0,1)
three = (0,2)
four = (1,0)
five = (1,1)
six = (1,2)
seven = (2,0)
eight = (2,1)
nine = (2,2)
choiceArray = [one,two,three,four,five,six,seven,eight,nine]

def isBoardEmpty(board):
    for i in board:
        for j in i:
            if j == '-':return True
    return False

def printBoard(board):
    for index,i in enumerate(board):
        print(f'{i[0]} | {i[1]} | {i[2]}')
        if index < 2:
            print(f'--|---|---')

def valueOfBoard(board):
    for i in range(3): #check for rows for x
        if board[i][0] == board[i][1] == board[i][2] == player: return 1
        elif board[0][i] == board[1][i] == board[2][i] == player: return 1
    if board[0][0] == board[1][1] == board[2][2] == player: return 1 #check for diagonal for X
    if board[0][2] == board[1][1] == board[2][0] == player: return 1
    for i in range(3): #check for rows for o
        if board[i][0] == board[i][1] == board[i][2] == opponent: return -1
        elif board[0][i] == board[1][i] == board[2][i] == opponent: return -1
    if board[0][0] == board[1][1] == board[2][2] == opponent: return -1 #check for diagonal for o
    if board[0][2] == board[1][1] == board[2][0] == opponent: return -1
    return 0

def minimax(board,depth,nextTurn):
    boardval = valueOfBoard(board)
    if boardval == 1: return 1
    elif boardval == -1: return -1
    elif not isBoardEmpty(board):return 0 

    elif nextTurn:
        bestMax = -inf
        for i in range(3): 
            for j in range(3): 
                if board[i][j] == '-':
                    board[i][j] = player
                    bestMax = max(bestMax,minimax(board,depth+1,not nextTurn))
                    board[i][j] = '-'
        return bestMax
    else:
        bestMin = inf
        for i in range(3): 
            for j in range(3): 
                if board[i][j] == '-':
                    board[i][j] = opponent
                    bestMin = min(bestMin,minimax(board,depth+1,not nextTurn))
                    board[i][j] = '-'
        return bestMin

def findAndMakeBestMove(board):
    bestBoardVal = inf
    boardCoordinates = (-inf,inf)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = opponent
                maxVal  = minimax(board,0,True)
                board[i][j] = '-'
                if maxVal < bestBoardVal:
                    bestBoardVal = maxVal
                    boardCoordinates = (i,j)
    return boardCoordinates

def loading(text,delay):
    print(end=text)
    n_dots = 0
    for i in range(3):
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
        sleep(delay)
    print()

if __name__ == "__main__":
    board = [['-' for i in range(3)]for j in range(3)]
    print('value for choosing....')
    print(f'| 1  |  2  |  3  |')
    print(f'|----|-----|-----|')
    print(f'| 4  |  5  |  6  |')
    print(f'|----|-----|-----|')
    print(f'| 7  |  8  |  9  |')
    print()
    printBoard(board)
    print(f'You are the {player.upper()} player')
    try:
        turn=0
        while True:
            if valueOfBoard(board) == 1 :
                    print("You won the game!!")
                    break
            if valueOfBoard(board) == -1 :
                    print("Computer won the game!!")
                    break
            if turn%2 == 0:
                choice = int(input("choose now: "))
                board[choiceArray[choice-1][0]][choiceArray[choice-1][1]] = player
                printBoard(board)
                if not isBoardEmpty(board): break
            else:
                coordinates = findAndMakeBestMove(board)
                board[coordinates[0]][coordinates[1]] = opponent
                loading("computer is thinking",0.5)
                printBoard(board)
                if not isBoardEmpty(board): break
            turn = turn + 1

    except:
        print("Make choice from given values... ;(")
        sleep(10)
    sleep(10)