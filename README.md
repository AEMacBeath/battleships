# Battleships

Battleships is a console based game where the player attempts to guess the location of the hidden ships by entering grid coordinates. This game is aimed at players of all ages looking for a quick and easy game to play.

The players will be able to enter a username, select the board size and play the game. When the game is complete they will be given the option to play again if they want. 

Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

![am_i_responsive_screenshot](/readme_scsreenshots/am_i_responsive_screenshot.png)

## Table of Contents

1. [Game Instructions](#game-instructions)
2. [User Stories](#user-stories)
3. [Features](#features)
    - [Welcome Screen](#welcome-screen)
    - [Enter Username](#enter-username)
    - [Game Play](#game-play)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    - [Bugs](#bugs)
    - [Validator Testing](#validator-testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Future Development](#future-development)

## Game Instructions
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

5. Whent the game is complete, to play again enter y (yes) or n (no) when prompted.

Enter 'exit' at anytime to close the game.

## User Stories

As a user of this site I can
- enter a username of my choice
- choose the size of board to play
- play the game
- restart the game

## Features

### Welcome Screen

The welcome screen consists of the following elements as shown in the below screenshot.
- A WELCOME TO BATTLESHIPS! message.
- Game instructions.
- An input section for users to add a username of their choice.

![Welcome_screen]()

### Enter username
A message to ask users to enter a username<br>
![Enter nickname message](add screenshot)

### Game play

At the start of the game, the board is made up of .'s printed to the console<br>
![Starting game screenshot](add screenshot)

The user is then asked to enter x and y coordinates to make their guess <br>
![enter coords](add screenshot)

After each guess a HIT or MISS message is printed to the console with an updated board showing an X for hit or O for miss. 
![re-ptrined board](add screenshot)

When the game is complete there is a Congratulations message and option to play again.
![game complete](add screenshot)

## Technologies used

- Python3
- GitHub
- GitPod
- Heroku
## Testing

### Bugs

- to be added (none so far)

### Validator Testing
- Python - ![PEP8 online](http://pep8online.com/checkresult) <!-- update link with final check -->

## Deployment

This site was deployed to Heroku by following the below steps:

- add steps once complete
- Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

## Credits

- Inital code inspired by [Trinket](https://trinket.io/python/051179b6d3)
- ASCII are from [Patorjk](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=battleships)

## Future Development

- Add player board
    - Player will be able to set the coordinates for thier ships
    - The player and computer will then take turns to guess the location of each others ships

- Add attempts counter to show the player how many attempts it took them to locate all the ship