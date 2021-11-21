game_list = [0,1,2]

def display_game(game_list):
    print("Here is the game list: ")
    print(game_list)

def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0','1', '2']:
            print('Sorry, invalid choice! ')
    return int(choice)

position_choice()

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list 

replacement_choice(game_list, 1)

print(game_list)
