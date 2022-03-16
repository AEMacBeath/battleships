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
    else:
        username = input('please enter a username: ')


# Board setup
def board_size():
    """
    board_size function comments
    """
    board = input('Select a board size (enter s for 5x5, enter l for 10x10): ')

    if board == 'l':
        global size
        size = 10
    elif difficulty == 's':
        size = 5
    else:
        print('Please select a board size (s = 5x5 l = 10x10')


# Call functions
enter_username()
board_size()
