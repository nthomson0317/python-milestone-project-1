
import random

# 2 players should be able to play the game (both sitting at the computer)

# The board should be printed out every time a player makes a move

# You should be able to accept input of the player position and then place a symbol on the board

# Step 1 write a function that can print out a board. set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation
def display_board(board):
    #clear_output()
    print('   |   |')
    print(' ' + board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# test_board_2 = ['#',' ','O','X','O','X','O','X','O','X']

# display_board(test_board)

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
# player_input()


    

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board, marker, position):
    position = input('Where would you like to move? (1-9): ')
    position_int = int(position)
    board[position_int] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)) 

        
# print('win check')    
# print(win_check(test_board,'X'))

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint(). Return a string of which player went first.

def choose_first():
    first = random.randint(0,2)
    if first == 1:
        print('Player 1 goes first')
    elif first == 2:
        print('Player 2 goes first')

# choose_first()

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):

    if board[position] == ' ':
        return True
    else:
        return False

# print('Space check: ')
# print(space_check(test_board, 1))

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# print('Full board check: ')
# print(full_board_check(test_board))

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    full = False
    while full == False:
        position = input('Input next position (1-9): ')
        if space_check(board,int(position)):
            full = True
            return position
        else:
            print('Sorry, that space is already taken. Please try again. ')
        
# print(player_choice(test_board_2))

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    hold = True
    while hold == True:
        play_again = input('Would you like to play again? (Y/N): ')

        if play_again == 'Y':
            hold = False
            return True
        elif play_again == 'N':
            hold = False
            return False
        else:
            print('Sorry, please choose Y or N')

# replay()

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

print('Welcome to Tic Tac Toe!')
while True:
    #Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] =='y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

