import random

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

    if username != '':
        print('Hello ' + username)
        board_size()
    else:
        username = input('please enter a username:\n')


# Select board size
def board_size():
    """
    board_size function comments
    """
    global size
    board = input('Select a board size (enter s for 5x5, enter l for 10x10):\n')

    if board == 'l':
        size = 10
    elif board == 's':
        size = 5
    else:
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

    print(ship)     # to be removed
    game_play(ship)


# Game play
def game_play(ship):
    """
    game_play function comments
    """
    hits = 0

    while hits < len(ship):
        attempt_row = int(input("Enter x coordinate:\n"))
        attempt_column = int(input("Enter y coordinate:\n"))

        if int(str(attempt_row) + str(attempt_column)) in ship:
            print("Hit")
            area[attempt_row][attempt_column] = "X"
            hits += 1
        else:
            print("Miss")
            area[attempt_row][attempt_column] = "o"

        for row in area:
            print((" ").join(row))
        print(ship)     # to be removed
    game_complete()


# Game complete
def game_complete():
    """
    game_complete function comments
    """
    print('Congratulations ' + username + 'you sunk all the battleships')
    play_again = input('Do you want to play again (y/n)?:\n')

    if play_again == 'y':
        board_size()
    else:
        print('Goodbye, thanks for playing Battleships')


# Call functions
enter_username()
