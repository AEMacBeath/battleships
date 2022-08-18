# Battleships

Battleships is a console based game where the player attempts to guess the location of the hidden ships by entering grid coordinates. This game is aimed at players of all ages looking for a quick and easy game to play.

The players will be able to enter a username, select a board size and play the game. When the game is complete they will be given the option to play again if they want. 

Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

![responsive_screenshot](/readme_scsreenshots/responsive_screenshot.png)

## Table of Contents

1. [Game Instructions](#game-instructions)
2. [User Stories](#user-stories)
3. [Application Flow Diagram](#application-flow-diagram)
4. [Features](#features)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Technologies Used](#technologies-used)
8. [Credits](#credits)
9. [Future Development](#future-development)

## Game Instructions
 1. Enter a user name to begin the game.

 2. Select a board size,
    - Small - Grid size = 5x5 - Hidden ships = 5
    - Large - Grid size = 10x10 - Hidden ships = 10

 3. Make a guess by entering an x and y coordinate when prompted.
    - Coordinates must be numbers between
        - 1 and 5 on a small board
        - 1 and 10 on a large board

 4. Continue entering guesses until all ships are found.

 5. When the game is complete, to play again enter y (yes) or
    n (no) when prompted.

 Enter 'exit' at any time to close the game.

## User Stories
As a player of this game I can
- view the game instructions.
- enter a username of my choice.
- choose the size of board to play.
- play the game.
- restart the game.
- exit the game

## Application Flow Diagram

![flow_diagram](/readme_scsreenshots/flow_diagram.png)

## Features
### Welcome Screen
The welcome screen consists of the following elements as shown in the below screenshot.
- A WELCOME message written with ASCII art.
- An option to view the game instructions.

![welcome_screen](/readme_scsreenshots/welcome_screen.png)

### Instructions Screen
The instructions screen is an ordered list of steps required to complete the game. As shown in the below screenshot.

![instructions_screen](/readme_scsreenshots/instructions_screen.png)

### Select Board Screen
The select board screen contains information about each board size and an input for the user to select which one they would like to use. 
As shown below.

![board_selection](/readme_scsreenshots/board_selection.png)

### Game play
At the start of the game, the board is made up of .'s printed to the console. 
The user is then asked to enter x and y coordinates.

#### 5x5 Board

![game_play_5x5](/readme_scsreenshots/game_play_5x5.png)

#### 10x10 Board

![game_play_10x10](/readme_scsreenshots/game_play_10x10.png)

#### Board with shots taken

![game_play_shots](/readme_scsreenshots/game_play_shots.png)

#### Shot feedback
After each shot a HIT or MISS message is printed to the console with an updated board showing an X for hit or O for miss. 

![hit_ascii](/readme_scsreenshots/hit_ascii.png)

![miss_ascii](/readme_scsreenshots/miss_ascii.png)

### Game Complete Screen
When the game is complete there is a WINNER message and option to play again. As shown below.

![game_complete](/readme_scsreenshots/game_complete.png)

### Goodbye screen
The goodbye screen which appears when the user selects;
- No to playing again.
- Exit at any time during the game.

![goodbye_screen](/readme_scsreenshots/goodbye_screen.png)

## Testing

### Feature Testing

See [feature_testing.md](/feature_testing.md)

### Validator Testing
Python - no errors found when passing through [PEP8 online](http://pep8online.com)

![pep8_results](/readme_scsreenshots/pep8_results.png)

### Bugs
#### Fixed bugs
1.  _Open Instructions? (y/n)_ on the [Welcome Screen](#welcome-screen) accepts invalid/empty inputs
    -   Fix: Defined open_instrcutions function to catch invalid / empty inputs.
2.  GamePlay function accepts 0 as x and y coordinate when the instructions state to enter only between 1 and 5.
    -   Fix: Created, x_guess and y_guess, functions to check user input for errors. 
3.  When users enter coordinates that have already been entered, there is no feedback provided.
    -   Fix: Added attempts array to record the attempt values and an if statement to check if new entries have already been entered.
4.  Play again? (y/n) accepts empty and invalid inputs.
    -   Fix: Created restart_game function to check the user input and provide feedback if the input is invalid.
5.  Enter username accepts empty values.
    -   Added if statement to check if a value has been entered before running further checks. 


## Deployment

This site was deployed to Heroku by following the below steps:

- On [Heroku.com](https://dashboard.heroku.com), create a new app
- Under the settings tab, set the build packs to 
    - heroku/python
    - heroku/nodejs
- Link the app to the [GitHub Repository](https://github.com/AEMacBeath/battleships)
- Enable automatic Deploys and click Deploy
- Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

## Technologies used

- Python3
- GitHub
- GitPod
- Heroku
- ASCII art
- [Lucid](https://lucid.app/) to create flow chart

## Credits

- Initial code inspired by [Trinket](https://trinket.io/python/051179b6d3)
- ASCII are from [Patorjk](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=battleships)

## Future Development

- Add player board
    - Player will be able to set the coordinates for their ships.
    - The player and computer will then take turns to guess the location of each others ships.

- Add attempts counter to show the player how many attempts it took them to locate all the ships.