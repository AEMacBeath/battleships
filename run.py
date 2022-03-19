import random
import string
import os
import sys

# Global variables
size = 0
area = []
username = ''


# Player enter name
def enter_username():
    """
    enter_username function comments
    """
    global username
    username = input('please enter a username:\n')
    if username == 'exit':
        exit_game()

    if any(char in string.punctuation for char in username):
        print('Special character used, please use letters only')
        enter_username()
    elif any(char.isdigit() for char in username):
        print('Number used, please use letters only')
        enter_username()
    else:
        os.system('clear')
        board_size()


# Instructions
INSTRUCTIONS = """
Game Instructions

1. Enter a user name to begin the game.

2. Select a board size,
    - Small
        - Grid size = 5x5
        - Hidden ships = 5

    - Large
        - Grid size = 10x10
        - Hidden ships = 10

3. Make a guess by entering an x and y coordinate when prompted.
    - Coordinates must be numbers between
        - 1 and 5 on a small board
        - 1 and 10 on a large board

4. Continue entering guesses until all ships are found.

Enter 'exit' at anytime to close the game.

"""

# Select board size
def board_size():
    """
    board_size function comments
    """
    global size
    print('Hello ' + username)
    print("""
    Select a board size,

    - Small
        - Grid size = 5x5
        - Hidden ships = 5

    - Large
        - Grid size = 10x10
        - Hidden ships = 10
    """)
    board = input('Enter s = small or l = large:\n')

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
    print(ship)
    game_play(ship)


# Game play
def game_play(ship):
    """
    game_play function comments
    """
    hits = 0

    while hits < len(ship):
        print(f"""

Make a guess by entering an x and y coordinate when prompted.
- Coordinates must be numbers between 1 and {len(ship)}

        """)
        attempt_row = input("Enter x coordinate:\n")

        if attempt_row == 'exit':
            exit_game()
        
        attempt_column = input("Enter y coordinate:\n")

        if attempt_column == 'exit':
            exit_game()

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
                    area[int(attempt_row) - 1][int(attempt_column) - 1] = "X"
                    hits += 1
                    hit = open('hit_ascii.txt', 'r')
                    print(' '.join([line for line in hit]))
                else:
                    os.system('clear')
                    area[int(attempt_row) - 1][int(attempt_column) - 1] = "o"
                    miss = open('miss_ascii.txt', 'r')
                    print(' '.join([line for line in miss]))

            for row in area:
                print((" ").join(row))
            print(ship)
        else:
            print('Please enter numbers only.')

    game_complete()


# Game complete
def game_complete():
    """
    game_complete function comments
    """
    global area
    os.system('clear')
    print(f'Contgratulations {username}. You sunk all the Battleships')
    play_again = input('Do you want to play again (y/n)?:\n')

    if play_again == 'y':
        area = []
        os.system('clear')
        board_size()
    else:
        exit_game()


# Exit function
def exit_game():
    """
    comments
    """
    os.system('clear')
    print('Thanks for playing')
    goodbye = open('goodbye_ascii.txt', 'r')
    print(' '.join([line for line in goodbye]))
    sys.exit()


# Run programme
welcome = open('welcome_ascii.txt', 'r')
print(' '.join([line for line in welcome]))

view_instructions = input('Open instructions? (y/n):\n')

if view_instructions == 'y':
    os.system('clear')
    print(INSTRUCTIONS)

enter_username()
