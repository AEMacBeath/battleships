import random 

# Gamge heading
print('WELCOME TO BATTLESHIPS')

# Player enter name - required
"""username = input('please enter a username: ')
print('Hello ' + username)"""

# Board setup
difficulty = input('Select a difficulty: ')

if difficulty == 'h':
    size = 10
else:
    size = 5

ships = size
area = []

for i in range(size):
    area.append(["."] * size)

def print_area(area):
    """
    to be added
    """
    for row in area:
        print((" ").join(row))


print_area(area)

def random_row(area):
    """
    to be added
    """
    return random.randint(0, size)

def random_column(area):
    """
    to be added
    """
    return random.randint(0, size)

ship_row = random_row(area)
ship_column = random_column(area)
hits = 0

# Game play
while ships >= hits:
    attempt_row = int(input("Enter x coordinate: "))
    attempt_column = int(input("Enter y coordinate: "))

    if attempt_row == ship_row and attempt_column == ship_column:
        print("Hit")
        area[attempt_row][attempt_column] = "X"
        hits =+ 1
    else:
        print("Miss")
        area[attempt_row][attempt_column] = "o"

    print_area(area)

# Score calculator
# Winner / loser
# Play again