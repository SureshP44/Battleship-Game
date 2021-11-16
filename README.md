

Battleship-Game

DESCRIPTION

Its a Two Player Game, created with python and targeted to make it as P2P Game. Currently this will work on Command line, it has 5 ships in total with various lengths {'carrier':5, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}

At first it will allow you to place the ships in 10 x 10 board. After succesfully placed the ships by both the players, it will allow players to ATTACK

PLACING SHIPS

It requires ship name and the starting position to place the ships.

example : Player A - choose the ship...cruiser Player B - choose the position...d4 This will place the cruiser at d4 - d7

Initially the board will filled with '-' the position row starts from a-j and column starts from 1-10 anything apart from this or the position is already occupied will be considered as invalid. once the place is valid, those positions will filled with '*'

ATTACKING SHIPS

It will show the current state of the player and opponents board aswell

Example: Player A Attacks Player B Player A - Enter the position to attack.. a3 returns hit or miss

If the position is valid and the opponent has ship then it is considered as 'hit' other than this is 'miss' If it was a successful hit, that position will be marked as '1', else it will be marked as '0'.

At the middle of attack, you can view both the boards by giving input 'show both', Or to view the current user board  by giving input "show board".


RESULT

The player who first attacks all the ships will be considered as "WINNER".

HOW TO RUN THE GAME

Clone the repo and run the main.py

Next Steps

It can be enhanced with P2P network with the help of package 'twisted'.
