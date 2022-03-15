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

for i in range(size):
    print(" . " * size)

# Game play
# Score calculator
# Winner / loser
# Play again