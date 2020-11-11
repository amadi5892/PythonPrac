

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# declare players
def player_input():
    marker = ''

    # KEEP ASKING PLAYER 1 TO choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # ASSIGN PLAYER 2, the opposite marker
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

player1_marker , player2_marker = player_input()
print('Player 1: '+player1_marker)
print('Player 2: '+player2_marker)

def start_game():
    print('Welcome to Tic Tac Toe!')
    print('To play, you will us your number padd')
    num_pad = ['#','1','2','3','4','5','6','7','8','9']
    display_board(num_pad)
    print('Choose a number to place your symbol')
    
    # There are nine total moves, will repeat process
    # move 1

    game_board = [' ']*10
    game_board[0] = '#'
    p1_move = user1_choice()
    game_board[p1_move] = player1_marker

    display_board(game_board)

    # move 2

    game_board = game_board
    p2_move = user2_choice()
    game_board[p2_move] = player2_marker
    
    display_board(game_board)

    # move 3

    game_board = game_board
    p1_move = user1_choice()
    game_board[p1_move] = player1_marker
    
    display_board(game_board)

    # move 4

    game_board = game_board
    p2_move = user2_choice()
    game_board[p2_move] = player2_marker
    
    display_board(game_board)

    # move 5

    game_board = game_board
    p1_move = user1_choice()
    game_board[p1_move] = player1_marker
    
    display_board(game_board)

    # move 6

    game_board = game_board
    p2_move = user2_choice()
    game_board[p2_move] = player2_marker
    
    display_board(game_board)

    # move 7

    game_board = game_board
    p1_move = user1_choice()
    game_board[p1_move] = player1_marker
    
    display_board(game_board)

    # move 8

    game_board = game_board
    p2_move = user2_choice()
    game_board[p2_move] = player2_marker
    
    display_board(game_board)

    # last move

    game_board = game_board
    p1_move = user1_choice()
    game_board[p1_move] = player1_marker
    
    display_board(game_board)

    


def user1_choice():

    # VARIABLES

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # Two Conditions To Check
    # DIGIT OR WITHIN_RANGE==FALSE
    while choice.isdigit() == False or within_range == False:

        choice = input("Player 1, Please enter a number (1-9): ")

        # Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range.")
                within_range = False

    return int(choice)

def user2_choice():

    # VARIABLES

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # Two Conditions To Check
    # DIGIT OR WITHIN_RANGE==FALSE
    while choice.isdigit() == False or within_range == False:

        choice = input("Player 2, Please enter a number (1-9): ")

        # Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range.")
                within_range = False

    return int(choice)
    
start_game()

# ------ Validating User Input-------

# def user_choice():

#     # VARIABLES

#     # Initial
#     choice = 'WRONG'
#     acceptable_range = range(0,10)
#     within_range = False

#     # Two Conditions To Check
#     # DIGIT OR WITHIN_RANGE==FALSE
#     while choice.isdigit() == False or within_range == False:

#         choice = input("Please enter a number (0-10): ")

#         # Digit Check
#         if choice.isdigit() == False:
#             print("Sorry that is not a digit!")

#         # Range Check
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Sorry, you are out of acceptable range.")
#                 within_range = False

#     return int(choice)

# print(user_choice())