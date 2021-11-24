import os
import random

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

def player_input():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        player1 = marker
        
    if player1 == 'X':
            player2 = 'O'
    else:
            player2 = 'X'
        
    return (player1, player2)
    
player_input()


    

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    position = input('Where would you like to move? (1-9): ')
    position_int = int(position)
    board[position_int] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    if board[1] and board[2] and board[3] == mark:
        return True
    elif board[4] and board[5] and board[6] == mark:
        return True
    elif board[7] and board[8] and board[9] == mark:
        return True
    elif board[1] and board[5] and board[9] == mark:
        return True
    elif board[3] and board[5] and board[7] == mark:
        return True
    else:
        return False
    
print(win_check(test_board,'X'))

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint(). Return a string of which player went first.

def choose_first():
    first = random.randint(0,2)
    if first == 1:
        print('Player 1 goes first')
    elif first == 2:
        print('Player 2 goes first')

choose_first()

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):

    if board[position] == ' ':
        return True
    else:
        return False

print('Space check: ')
print(space_check(test_board, 1))

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    empty = ' '
    if empty not in board:
        return True
    else:
        return False

print('Full board check: ')
print(full_board_check(test_board))