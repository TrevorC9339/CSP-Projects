import random

player = 'X'#assign players their role
player2 = 'O'
winner = None
gameRunning = True#use this to make the while loop work until the game is over
winstatus = False#make this so the while loop stops when the game ends
board = ['-','-','-',#this is where you will play the game the underscores are empty slots for players, it makes the board a list so you can use numbers for inputs
         '-','-','-',
         '-','-','-']
def board_(board):#create the board using previous varible
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])# creates lines inbetween the underscores for more clarity
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    return board

print(board_(board))#print the emtpy board for the begining of the game and the list so it is more clear what spacei s waht number and what space is taken

def input_(board):#this is for the players inputs to actually get on the board
    inp = int(input("each space is a number, tope left is 1 and bottom left is 9. type the number that is in your space. each item in the list is the board layed out in a line, once player one has made their choce, player two must also input their decison : "))#this takes the input as a number and is used to find which slot the player wants filled
    board = board_(board)#this defines board in the function and allows the input to interact with it, so the players inputs can apear on the board after it is updated
    if inp >= 1 and inp <= 9:#makes sure that there are not too many slots filled on the board
        print(inp)#takes input of user
        if board[inp-1] == '-':
            board[inp-1] = 'X'#replaces the empty space with an x

    else:
        print('Please check the input value before playing the game')#this checks to make sure the input is valid and works with the code

def checkHorizontal(board):#this checks for all the possiblites there are of winning with a horizontail three in a row
    if board[0] == board[1] == board[2] and board[0] != '-':#this checks for the top row 
        print('three in a row!')
        winstatus = True#ends the game
        gameRunning = False#makes sre the while loop stops
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':#this checks second row
        print('three in a row!')
        winstatus = True
        gameRunning = False
    elif board[6] == board[7] == board[8] and board[6] != '-':#this checks the last row
        print('three in a row!')
        winstatus = True
        gameRunning = False

def checkVertical(board):# this is the same as the horizontal but it checks for vertical win
    if board[0] == board[3] == board[6] and board[0] != '-':
        print('three in a row!') 
        winstatus = True
        gameRunning = False
    elif board[1] == board[4] == board[7] and board[1] != '-':
        print('three in a row!')
        winstatus = True
        gameRunning = False
    elif board[2] == board[5] == board[8] and board[2] != '-':
        print('three in a row!')
        winstatus = True
        gameRunning = False

def checkDiagonal(board):#same as others but it is diagonal it is shorter becasue there are less opputunities for a win on diagonal
    if board[0] == board[4] == board[8] and board[0] != '-':
        print('three in a row!')
        winstatus = True
        gameRunning = False

    elif board[2] == board[4] == board[6] and board[2] != '-':
        print('three in a row!')
        winstatus = True
        gameRunning = False


def checkTie(board):#this makes sure that if there is no possible win then the game ends
    for i in range(0,0):
        if board[i] != '-':#this makes it so if there are no underscores and noone won then the game is over
            print('Tie game')
            gameRunning = False#ends the game

def switchPlayer(board):#this changes the players turn
    rand_ = random.randint(0,9)#selects a random number 1 through 9
    if board[rand_] != 'X' and board[rand_] == '-':#this checks if it is x or o
        board[rand_] = 'O'
    


while gameRunning:#uses all the functions in the while loop so the game runs this creates an easy overview of what is happening and in what order
    input_(board)
    checkHorizontal(board)
    checkVertical(board)
    checkDiagonal(board)
    checkTie(board)
    switchPlayer(board)
    board_(board)
