import random
import string
import os

# Global variables
size = 0
area = []
username = ''

# Welcome message
print('Welcome to BATTLESHIPS')


# Instructions
INSTRUCTIONS = """
1. To begin the game please enter a user name below.

2. Select a board size,
    - Small
        - Grid size = 5x5
        - Hidden ships = 5

    - Large
        - Grid size = 10x10
        - Hidden ships = 10

3. Make a guess by entering an x and y coordinate as prompted. 
    - Coordinates must be numbers between
        - 1 and 5 on a small board
        - 1 and 10 on a large board

4. Continue entering guesses until all ships are found.

If you would like to quit the game at any time please enter x.
"""
print(INSTRUCTIONS)

# Player enter name - required
def enter_username():
    """
    enter_username function comments
    """
    global username
    username = input('please enter a username:\n')

    if any(char in string.punctuation for char in username):
        os.system('clear')
        print('Special character used, please use letters only')
        enter_username()
    elif any(char.isdigit() for char in username):
        os.system('clear')
        print('Number used, please use letters only')
        enter_username()
    else:
        os.system('clear')
        print('Hello ' + username)
        board_size()


# Select board size
def board_size():
    """
    board_size function comments
    """
    global size
    board = input('Select a board size. s = small or l = large:\n')

    if board == 'l':
        size = 10
    elif board == 's':
        size = 5
    else:
        print('Invalid selection, please try again')
        board_size()

    for i in range(size):
        area.append(["."] * size)

    print_board(area)


# Print board
def print_board(area):
    """
    print_board fnuction comments
    """
    os.system('clear')
    for row in area:
        print((" ").join(row))

    place_ships()


# Place ships
def place_ships():
    """
    place_ships function comments
    """
    ship = []
    for i in range(size):
        ship.append(int(str(random.randint(1, size)) + str(
                    random.randint(1, size))))

    game_play(ship)


# Game play
def game_play(ship):
    """
    game_play function comments
    """
    hits = 0

    while hits < len(ship):
        attempt_row = input("Enter x coordinate:\n")
        attempt_column = input("Enter y coordinate:\n")

        try:
            x_coord = int(attempt_row)
        except:
            print(f'Error: {attempt_row} is not a valid entry')

        try:
            y_coord = int(attempt_column)
        except:
            print(f'Error: {attempt_column} is not a valid entry')

        if str(attempt_row).isdigit() and str(attempt_column).isdigit():
            if int(attempt_row) > len(ship) or int(attempt_column) > len(ship):
                print('Coordinates outside of board. Please try again.')
            else:
                if int(str(attempt_row) + str(attempt_column)) in ship:
                    os.system('clear')
                    print("Hit")
                    area[int(attempt_row) - 1][int(attempt_column) - 1] = "X"
                    hits += 1
                else:
                    os.system('clear')
                    print("Miss")
                    area[int(attempt_row) - 1][int(attempt_column) - 1] = "o"

            for row in area:
                print((" ").join(row))

        else:
            print('Please enter numbers only.')

    game_complete()


# Game complete
def game_complete():
    """
    game_complete function comments
    """
    os.system('clear')
    print('Congratulations ' + username + ' you sunk all the battleships')
    play_again = input('Do you want to play again (y/n)?:\n')

    if play_again == 'y':
        board_size()
    else:
        os.system('clear')
        print('Goodbye, thanks for playing Battleships')


# Call functions
enter_username()
