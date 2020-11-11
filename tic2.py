# Imports
import random


# display board
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
clear_board = [' ']*10
clear_board[0] = '#'
# display_board(test_board)

def player_input():
    marker = ''

    # Keep asking player 1 to choose 'X' or 'O'
    while marker != 'X' or marker != 'O':
        marker = input("Choose 'X' or 'O': ")

        player1 = marker

        # Assign Player2 the opposite marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        return (player1, player2)

# Display player markers
# print('\n')
# player1_marker, player2_marker = player_input()
# print('Player 1: '+player1_marker)
# print('Player 2: '+player2_marker)


def user_choice():
    # Variables
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number (1-9): ')

        # Check that choice is an integer
        if choice.isdigit() == False:
            print('Please enter a digit from your number pad.')
        
        # Check that choice is within range
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptable range.')
                within_range = False
        
        return int(choice)

def place_marker(board, marker, position):
    marker_chosen = marker

    move = position

    board[move] = marker_chosen
    display_board(board)

    return board

# place_marker(clear_board, player1_marker, pos)

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return 'Winner'
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return 'Winner'
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return 'Winner'
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return 'Winner'
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return 'Winner'
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return 'Winner'
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return 'Winner'
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return 'Winner'
    else:
        pass

# print(win_check(test_board, 'X'))

def choose_first():
    rando_num = random.randint(1,2)

    if rando_num == 1:
        print('Player 1 goes first!')
        return 'Player 1'
    else:
        print('Player 2 goes first!')
        return 'Player 2'

def space_check(board, position):
    available_pos = False
    
    while available_pos == False:
        if board[position] == ' ':
            available_pos = True
        else:
            available_pos = False
            
    return available_pos

def full_board_check(board):
    for x in board:
        if x != ' ':
            return True
        else:
            return False

def replay():
    player_response = input('Would you like to play again? (Y or N): ')

    if player_response == 'Y':
        return True
    else:
        return False

print('Welcome To Tic Tac Toe!')

while True:

    # Play The Game

    ## Set Everything Up (Board, Whos First, Choose Marker)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## Game Play

    while game_on:

        if turn == 'Player 1':

            # Show the board
            display_board(the_board)
            # Choose a position
            position = user_choice()
            # Place the marker on the position
            place_marker(the_board, player1_marker,position)
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Has Won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'

        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = user_choice()
            # Place the marker on the position
            place_marker(the_board, player1_marker,position)
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 2 Has Won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'
            # Or check if there is a tie

            # No tie and no win? Then next player's turn

        ### PLAYER ONE TURN

    
    if not replay():
        break




