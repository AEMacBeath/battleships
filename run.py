import random

# Global variables
size = 0
area = []

# Gamge heading
print('WELCOME TO BATTLESHIPS')


# Player enter name - required
def enter_username():
    """
    enter_username function comments
    """
    username = input('please enter a username: ')

    if username != '':
        print('Hello ' + username)
        board_size()
    else:
        username = input('please enter a username: ')


# Select board size
def board_size():
    """
    board_size function comments
    """
    global size
    board = input('Select a board size (enter s for 5x5, enter l for 10x10): ')

    if board == 'l':
        size = 10
    elif board == 's':
        size = 5
    else:
        board_size()
    
    print_board()


# Print board
def print_board():
    """
    print_board fnuction comments
    """

    for i in range(size):
        area.append(["."] * size)
    for row in area:
        print((" ").join(row))
    
    place_ships()


# Randomly select ship placement
ships = []


def place_ships():
    """
    to be added
    """
    for i in range(size):
        ships[i] = random.randint(0, size - 1)
    
    print(ships)


# Game play
def game_play():
    """
    game_play function comments
    """

    hits = 0

    while hits == 0:
        attempt_row = int(input("Enter x coordinate: "))
        attempt_column = int(input("Enter y coordinate: "))
        
        for i in range(size):
            if attempt_row == ship_row[i] and attempt_column == ship_column[i]:
                print("Hit")
                area[attempt_row][attempt_column] = "X"
                hits += 1
            else:
                print("Miss")
                area[attempt_row][attempt_column] = "o"


# Call functions
enter_username()
