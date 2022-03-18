import random
import string

# Global variables
size = 0
area = []
username = ''

# Welcome message
print('Welcome to BATTLESHIPS')


# Player enter name - required
def enter_username():
    """
    enter_username function comments
    """
    global username
    username = input('please enter a username:\n')

    if any(char in string.punctuation for char in username):
        print('Special character used, please use letters only')
        enter_username()
    elif any(char.isdigit() for char in username):
        print('Number used, please use letters only')
        enter_username()
    else:
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
        ship.append(int(str(random.randint(0, size - 1)) + str(
                    random.randint(0, size - 1))))

    # print(ship)
    game_play(ship)


# Game play
def game_play(ship):
    """
    game_play function comments
    """
    hits = 0

    while hits < len(ship):
        attempt_row = input("Enter x coordinate:\n")
        try:
            x_coord = int(attempt_row)
        except:
            print(f'Error: {attempt_row} is not a valid entry')

        attempt_column = input("Enter x coordinate:\n")
        try:
            y_coord = int(attempt_column)
        except:
            print(f'Error: {attempt_column} is not a valid entry')

        if str(attempt_row).isdigit() and str(attempt_column).isdigit():
            if int(attempt_row) >= len(ship) or int(attempt_column) >= len(ship):
                print('Coordinates outside of board. Please try again.')
            else:
                if int(str(attempt_row) + str(attempt_column)) in ship:
                    print("Hit")
                    area[int(attempt_row)][int(attempt_column)] = "X"
                    hits += 1
                else:
                    print("Miss")
                    area[int(attempt_row)][int(attempt_column)] = "o"

            for row in area:
                print((" ").join(row))
            # print(ship)

        else:
            print('Please enter numbers only.')

    game_complete()


# Game complete
def game_complete():
    """
    game_complete function comments
    """
    print('Congratulations ' + username + ' you sunk all the battleships')
    play_again = input('Do you want to play again (y/n)?:\n')

    if play_again == 'y':
        board_size()
    else:
        print('Goodbye, thanks for playing Battleships')


# Call functions
enter_username()
