### Feature testing
Run [heroku app](https://battleships-am.herokuapp.com/)

#### [Welcome Screen](#welcome-screen)
-  Welcome ascii art loads
-  _>>> Open instructions? (y/n)_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   No value

Error feedback

![input_errors_view_instructions](/readme_scsreenshots/input_errors_view_instructions.png)

Enter y - opens Instructions Screen

Enter n - _>>> Enter a username?_ visible and waiting for user input

#### [Instructions Screen](#instructions-screen)
-   Game instructions load
-   _>>> Enter a username?_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   Special characters
-   No value

Error feedback

![input_errors_username](/readme_scsreenshots/input_errors_username.png)

Enter a valid username - goes to Select Board Size Screen

#### [Select Board Screen](#select-board-screen)
-   Board option information loads
-   _>>> Enter s for small or l for large_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except s or l
-   No value

Error feedback

![input_errors_board_selection](/readme_scsreenshots/input_errors_board_selection.png)

Enter s or l - goes to Game Play screen

#### [Game Play](#game-play)
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

Error feedback

![input_error_x_coord](/readme_scsreenshots/input_error_x_coord.png)

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

Error feedback

![input_error_y_coord](/readme_scsreenshots/input_error_y_coord.png)

Play the game until all ships are found - goes to Game Complete Screen

##### [Game Complete Screen](#game-complete-screen)
-   Winner ascii loads
-   _Do you want to play again? (y/n)_ visible and waiting for user input

Error checking:
Try entering the below invalid inputs
-   Anything except y or n
-   Special characters
-   No value

Error feedback

![input_error_play_again](/readme_scsreenshots/input_error_play_again.png)

Enter y - goes back to Select Board Screen
Enter n - goes to Goodbye Screen

##### [Goodbye Screen](#goodbye-screen)
-   Goodbye ascii loads