# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']

# row2[1] = 'X'

# display(row1,row2,row3)

# ------- Accepting User Input -------

# result = input("Please enter a value: ")

# print(result)

# position_index = int(input("Choose an index position: "))





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




# ------ Simpler User Interaction -------

game_list = [0,1,2]

def dispaly_game(game_list):
    print("Here is the current list: ")
    print(game_list)

# dispaly_game(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
    
        choice = input("Pick a poisiton (0,1,2): ")

        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")

    return int(choice)

# print(position_choice())

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

# print(replacement_choice(game_list,1))

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N ")

    if choice == "Y":
        return True
    else:
        return False



game_on = True
game_list = [0,1,2]

while game_on:
    dispaly_game(game_list)

    position = position_choice()
    
    game_list = replacement_choice(game_list,position)

    game_on = gameon_choice()