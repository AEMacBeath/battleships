# Battleships

Battleships is a console based game where the player attempts to guess the location of the hidden ships by entering grid coordinates. This game is aimed at players of all ages looking for a quick and easy game to play.

The players will be able to enter a username, select a board size and play the game. When the game is complete they will be given the option to play again if they want. 

Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

![am_i_responsive_screenshot](/readme_scsreenshots/am_i_responsive_screenshot.png)

## Table of Contents

1. [Game Instructions](#game-instructions)
2. [User Stories](#user-stories)
3. [Features](#features)
    - [Welcome Screen](#welcome-screen)
    - [Instructions Screen](#instructions-screen)
    - [Username Validation](#username-validation)
    - [Select Board Screen](#select-board-screen)
    - [Game Play](#game-play)
    - [Game Complete Screen](#game-complete-screen)
    - [Goodbye Screen](#goodbye-screen)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    - [Bugs](#bugs)
    - [Validator Testing](#validator-testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Future Development](#future-development)

## Game Instructions
 Game Instructions
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

## Flow Diagram

### Application flow diagram
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

### Username Validation
The players username should contain letters only. 
The follow error messages will appear if the user attempts to enter any other characters.

Number error

![username_number_error](/readme_scsreenshots/username_number_error.png)

Special character error

![username_special_error](/readme_scsreenshots/username_special_error.png)

No value error
![username_novalue_error](/readme_scsreenshots/username_novalue_error.png)

### Select Board Screen
The select board screen contains information about each board size and an input for the user to select which one they would like to use. 
As shown below.

![select_board](/readme_scsreenshots/select_board.png)

### Game play

At the start of the game, the board is made up of .'s printed to the console. 
The user is then asked to enter x and y coordinates to make their guess
![start_game](/readme_scsreenshots/start_game.png)

After each guess a HIT or MISS message is printed to the console with an updated board showing an X for hit or O for miss. 
![shot_hit](/readme_scsreenshots/shot_hit.png) 
![shot_miss](/readme_scsreenshots/shot_miss.png)

### Game Complete Screen
When the game is complete there is a WINNER message and option to play again. As shown below.
![game_complete](/readme_scsreenshots/game_complete.png)

### Goodbye screen
The goodbye screen which appears when the user selects;
    - No to playing again.
    - Exit at any time during the game.

![goodbye_screen](/readme_scsreenshots/goodbye_screen.png)

## Technologies used

- Python3
- GitHub
- GitPod
- Heroku
- ASCII art

## Testing

### Bugs

#### Fixed bugs
1.  _Open Instructions? (y/n)_ on the [Welcome Screen](#welcome-screen) accepts invalid/empty inputs
    -   Fix: Defined open_instrcutions function to catch invalid / empty inputs.
2.  GamePlay function accepts 0 as x and y coordinate when the instructions state to enter only between 1 and 5.
    -   Fix: Created, x_guess and y_guess, functions to check user input for errors. 
3.  When users enter coordinates that have already been entered, there is no feedback provided.
    -   Fix: Added attempts array to record the attempt values and an if statment to check if new enteries have already been entered.
4.  Play again? (y/n) accepts empty and invalid inputs.
    -   Fix: Created restart_game funcation to check the user input and provide feedback if the ipnut is invalid.
5.  Enter username accepts empty values.
    -   Added if statement to check if a value has been entered before running further checks. 

#### Feature testing
Run [heroku app](https://battleships-am.herokuapp.com/) to load welcome screen

##### [Welcome Screen](#welcome-screen)
-  Welcome ascii art loads
-  _Open instructions? (y/n)_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   No value

Enter y - opens Instructions Screen
Enter n - _Enter a username?_ visible and waiting for user input

##### [Instructions Screen](#instructions-screen)
-   Game instructions load
-   _Enter a username?_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   Special characters
-   No value

Enter a valid username - goes to Select Board Size Screen

##### [Select Board Screen](#select-board-screen)
-   Board options and information loads
-   _Enter s for small or l for large_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except s or l
-   No value

Enter s or l - goes to Game Play screen

##### [Game Play](#game-play)
-   Board loads as .'s (5 x 5 or 10 x 10 depending on board selection)
-   _Enter x coordinate from..._ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   0 or number higher than
    -   5 (5x5 board)
    -   10  (10x10 board)
-   Letters
-   Special characters
-   No value

Enter a valid x coordinate
-   _Enter y coordinate from..._ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   0 or number higher than
    -   5 (5x5 board)
    -   10  (10x10 board)
-   Letters
-   Special characters
-   No value

Play the game until all ships are found - goes to Game Complete Screen

###### [Game Complete Screen](#game-complete-screen)
-   Winner ascii loads
-   _Do you want to play again? (y/n)_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   Special characters
-   No value

Enter y - goes back to Select Board Screen
Enter n - goes to Goodbye Screen

###### [Goodbye Screen](#goodbye-screen)
-   Goodbye ascii loads

### Validator Testing

- Python - no errors found whne passing through [PEP8 online](http://pep8online.com/checkresult)

## Deployment

This site was deployed to Heroku by following the below steps:

- On [Heroku.com](https://dashboard.heroku.com), create a new app
- Under the settings tab, set the build packs to 
    - heroku/python
    - heroku/nodejs
- Link the app to the [GitHub Repository](https://github.com/AEMacBeath/battleships)
- Enable automatic Deploys and click Deploy
- Link to deployed website - [Battleships](https://battleships-am.herokuapp.com/)

## Credits

- Initial code inspired by [Trinket](https://trinket.io/python/051179b6d3)
- ASCII are from [Patorjk](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=battleships)

## Future Development

- Add player board
    - Player will be able to set the coordinates for their ships.
    - The player and computer will then take turns to guess the location of each others ships.

- Add attempts counter to show the player how many attempts it took them to locate all the ships.