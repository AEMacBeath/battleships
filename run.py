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

area = []

for i in range(size):
    area.append(["O"] * size)

def print_area(area):
    """
    to be added
    """
    for line in area:
        print((" ").join(line))

print_area(area)

# Game play
# Score calculator
# Winner / loser
# Play again