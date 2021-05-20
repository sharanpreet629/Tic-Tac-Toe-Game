# Importing the libraries
import random
import os
# Global variables
theBoard = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}
mylist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
computer_choice =  []
# User defined functions
def clearScreen():
	if os.name == 'posix':
		#For UNIX system 'posix':
		_ = os.system('clear')
	else:
		#For Windows system 'nt':
		_ = os.system('cls')

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def playGame():
    player1= input("Enter first player name: ")
    player2= input("Enter second player name: ")

    print(player1 + ":X | " + player2 + ":O")
    
    turn = 'X' #Current turn 
    count = 0 #Numbers of turns played
    player = player1 #player who play first
    
    while True:
        printBoard(theBoard)

        if count == 9:
            print("The game ends in a draw")
            break
        if player == player1:
           move = input("Enter your move {}: ".format(player1))
           computer_choice.append(move)
       
        else:
            
            move= random.choice(mylist)
            computer_choice.append(move)
            if move in computer_choice:
                input(move)
            else:
                print(move)
     
            
        if move not in theBoard.keys():
            print("Invalid move")
            continue

        #If the place is empty
        if theBoard[move] == ' ':
            theBoard[move] = turn

            #Checking if we have a winner
            winner = checkWin(turn)
            if winner != '':
                printBoard(theBoard)
                print("Congratulations! The winner is", player)
                break

            else:
                count += 1
                if turn == 'X':
                    turn = 'O'
                    player = player2
                else:
                    turn = 'X'
                    player = player1

        else:
            print("Sorry that place is already filled")
            continue

def checkWin(turn):
    winner = ''

    #Checking rows
    if (theBoard['7']==theBoard['8']==theBoard['9']==turn) or (theBoard['4']==theBoard['5']==theBoard['6']==turn) or (theBoard['1']==theBoard['2']==theBoard['3']==turn):
        winner = turn

    #Checking columns
    if (theBoard['7']==theBoard['4']==theBoard['1']==turn) or (theBoard['8']==theBoard['5']==theBoard['2']==turn) or (theBoard['9']==theBoard['6']==theBoard['3']==turn):
        winner = turn

    #Checking diagonals
    if (theBoard['7']==theBoard['5']==theBoard['3']==turn) or (theBoard['9']==theBoard['5']==theBoard['1']==turn):
        winner = turn

    return winner #Value can be '', 'X', 'O'
#asking for restart
def restartgame():
    choose = input("play again??\n yes or no: ")
    if choose.lower()=="yes":
        for values in theBoard:
            theBoard[values]=" "
        clearScreen()
        main()
    else:
        print("***THANKS FOR PLAYING***")
        
# Main function
def main():
    playGame()
    restartgame()
    
    
    
if __name__=="__main__":
    main()

