import os

# 2 players should be able to play the game (both sitting at the computer)

# The board should be printed out every time a player makes a move

# You should be able to accept input of the player position and then place a symbol on the board

# Step 1 write a function that can print out a board. set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation
def display_board(board):
    #clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[7]+'|'+board[8]+'|'+board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def x_or_o():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        player1 = marker
        
    if player1 == 'X':
            player2 = 'O'
    else:
            player2 = 'X'
        
    return (player1, player2)
    
x_or_o()


    

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    pass

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    pass

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint(). Return a string of which player went first.