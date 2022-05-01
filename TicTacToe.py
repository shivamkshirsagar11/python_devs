
def printApprovedBoard(x,y):
    one = 'X' if x[0] != 0 else ('O' if y[0] != 0 else '1')
    two = 'X' if x[1] != 0 else ('O' if y[1] != 0 else '2')
    three = 'X' if x[2] != 0 else ('O' if y[2] != 0 else '3')
    four = 'X' if x[3] != 0 else ('O' if y[3] != 0 else '4')
    five = 'X' if x[4] != 0 else ('O' if y[4] != 0 else '5')
    six = 'X' if x[5] != 0 else ('O' if y[5] != 0 else '6')
    seven = 'X' if x[6] != 0 else ('O' if y[6] != 0 else '7')
    eight = 'X' if x[7] != 0 else ('O' if y[7] != 0 else '8')
    nine = 'X' if x[8] != 0 else ('O' if y[8] != 0 else '9')
    print()
    print(f'| {one}  |  {two}  |  {three}  |')
    print(f'|----|-----|-----|')
    print(f'| {four}  |  {five}  |  {six}  |')
    print(f'|----|-----|-----|')
    print(f'| {seven}  |  {eight}  |  {nine}  |')
    print()

def sum(a,b,c): return a+b+c

def checkIfAnyWins(x,y):
    xwinstate = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    ywinstate = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in xwinstate:
        if sum(x[i[0]],x[i[1]],x[i[2]]) == 3: return True
    for i in ywinstate:
        if sum(y[i[0]],y[i[1]],y[i[2]]) == 3: return True
    return False

if __name__ == "__main__":
    x = [0,0,0,0,0,0,0,0,0]
    o = [0,0,0,0,0,0,0,0,0]
    turn = 0 #1 for o's turn 0 for x's turn
    printApprovedBoard(x,o)
    try:
        while True:
            if turn%2 == 0:
                choice = int(input("place X tile: "))
                x[choice-1] = 1
                printApprovedBoard(x,o)
                if checkIfAnyWins(x,o): 
                    print("Congrats X won the round!!")
                    break
            elif turn%2 == 1:
                choice = int(input("place O tile: "))
                o[choice-1] = 1
                printApprovedBoard(x,o)
                if checkIfAnyWins(x,o): 
                    print("Congrats O won the round!!")
                    break
            turn = turn + 1
            if turn == 9: 
                print("No one won: TIE !")
                break
    except:
        print("IO Exception...Bad Input :(")