import random
import string
import os
import sys

# Global variables
size = 0
area = []
username = ''


# View Instrucions
def open_instructions():
    """
    open_instructions function allows the user to select
    if they want to view the game instructions.
    """
    view_instructions = input(' >>> Open instructions? (y/n):\n')

    if view_instructions == 'y':
        os.system('clear')
        print(INSTRUCTIONS)
        enter_username()
    elif view_instructions == 'n':
        enter_username()
    else:
        print(
            ' Please enter y or n to select if you would like to view the instructions.')
        open_instructions()


# Instructions
INSTRUCTIONS = """
 Game Instructions
 1. Enter a user name to begin the game.

 2. Select a board size,
    - Small - Grid size = 5x5 - Hidden ships = 5
    - Large - Grid size = 10x10 - Hidden ships = 10

 3. Make a guess by entering an x and y coordinate when prompted.
    - Coordinates must be numbers between
        - 1 and 5 on a small board
        - 1 and 10 on a large board

 4. Continue entering guesses until all ships are found.

 5. When the game is complete, to play again enter y (yes) or
    n (no) when prompted.

 Enter 'exit' at any time to close the game.
"""


# Player enter name
def enter_username():
    """
    enter_username function allows the user to enter a username.
    The username must be letters only.
    Any other characters will promt the user to try again.
    """
    global username
    username = input(' >>> Enter a username:\n')
    if username == 'exit':
        exit_game()

    if username == '':
        print(' No username entered.')
        enter_username()
    else:
        if any(char in string.punctuation for char in username):
            print(' Username contains a special character, please use letters only')
            enter_username()
        elif any(char.isdigit() for char in username):
            print(' Username contains a number, please use letters only')
            enter_username()
        else:
            os.system('clear')
            board_size()


# Select board size
def board_size():
    """
    board_size function allows the user to pick a small or large board.
    The number of ships hidden on the baord is determined by the board size.
    """
    global size
    print(' Hello ' + username)
    print("""
     Select a board size,

     - Small
        - Grid size = 5x5
        - Hidden ships = 5

     - Large
        - Grid size = 10x10
        - Hidden ships = 10
    """)
    board = input(' >>> Enter s for small or l for large:\n')

    if board == 'l':
        size = 10
    elif board == 's':
        size = 5
    else:
        print(' Invalid selection, please try again')
        board_size()

    for i in range(size):
        area.append(["."] * size)

    print_board(area)


# Print board
def print_board(area):
    """
    print_board function prints the board as a .'s to the console.
    The .'s are later replaced by x / o when shots are made.
    """
    os.system('clear')

    for row in area:
        print((" ").join(row))
    place_ships()


# Place ships
def place_ships():
    """
    place_ships function randomly selects the coordinates
    for each ship on the board.
    """
    ship = []
    for i in range(size):
        ship.append(int(str(random.randint(1, size)) + str(
                    random.randint(1, size))))

    game_play(ship, 0, 0)


# X Coordinate error check
def x_guess(ship, attempt_row):
    """
    x_guess function checks that the users x coordinate input is valid
    by checking it is not outwith the borad (< 1 or > board length),
    it is a number and a value has been entered.
    """
    attempt_row = input(f" >>> Enter x coordinate from 1 and {len(ship)}: ")

    if attempt_row == 'exit':
        exit_game()

    if attempt_row == "":
        print(' Please enter a value')
        return x_guess(ship, attempt_row)

    try:
        x_coord = int(attempt_row)
    except:
        print(f' {attempt_row} is not a valid entry. Please try again.')
        return x_guess(ship, attempt_row)
    
    if int(attempt_row) > len(ship) or int(attempt_row) < 1:
        print(' Coordinate outside of board. Please try again.')
        return x_guess(ship, attempt_row)

    return attempt_row


# Y Coordinate error check
def y_guess(ship, attempt_column):
    """
    y_guess function checks that the users y coordinate input is valid
    by checking it is not outwith the borad (< 1 or > board length),
    it is a number and a value has been entered.
    """
    attempt_column = input(f" >>> Enter y coordinate from 1 and {len(ship)}: ")

    if attempt_column == 'exit':
        exit_game()

    if attempt_column == "":
        print(' Error: please enter a value')
        return y_guess(ship, attempt_column)

    try:
        y_coord = int(attempt_column)
    except:
        print(f' Error: {attempt_column} is not a valid entry.')
        return y_guess(ship, attempt_column)

    if int(attempt_column) > len(ship) or int(attempt_column) < 1:
        print(' Coordinate outside of board. Please try again.')
        return y_guess(ship, attempt_column)

    return attempt_column


# Game play
def game_play(ship, attempt_row, attempt_column):
    """
    game_play function allows the user to input an x and y corrdinate.
    checks the input is an integer within the correct range.
    prints the updated board with HIT or MISS.
    """
    hits = 0
    attempts = []

    while hits < len(ship):

        coord_x = x_guess(ship, attempt_row)

        coord_y = y_guess(ship, attempt_column)

        attempt = int(str(coord_x + coord_y))

        if attempt in attempts:
            os.system('clear')
            print(' You have already guessed those coordinates. Please try again.')
        
        elif int(str(coord_x) + str(coord_y)) in ship:
            # os.system('clear')
            area[int(coord_x) - 1][int(coord_y) - 1] = "X"
            hits += 1
            hit = open('hit_ascii.txt', 'r')
            print(' '.join([line for line in hit]))
        else:
            # os.system('clear')
            area[int(coord_x) - 1][int(coord_y) - 1] = "o"
            miss = open('miss_ascii.txt', 'r')
            print(' '.join([line for line in miss]))

        for row in area:
            print((" ").join(row))

        attempts.append(attempt)

    game_complete()


# Restart game / play again
def restart_game():
    """
    restart_game function allows the user to 
    restart or exit the game.
    """
    play_again = input(' >>> Do you want to play again? (y/n):\n')

    global area

    if play_again == 'n':
        exit_game()
    elif play_again == 'y':
        area = []
        os.system('clear')
        board_size()
    else:
        print(' Please enter y or n to select if you would like to play again.')
        restart_game()


# Game complete
def game_complete():
    """
    game_complete function prints out a WINNER message.
    and triggers the restart_game function.
    """
    winner = open('winner_ascii.txt', 'r')
    print(' '.join([line for line in winner]))
    print(f" {username}, you sunk all the Battleships")

    restart_game()


# Exit function
def exit_game():
    """
    exit_game can be called by the user at anytime to stop playing.
    """
    os.system('clear')
    print(' Thanks for playing')
    goodbye = open('goodbye_ascii.txt', 'r')
    print(' '.join([line for line in goodbye]))
    sys.exit()


# Run programme
welcome = open('welcome_ascii.txt', 'r')
print(' '.join([line for line in welcome]))

open_instructions()
