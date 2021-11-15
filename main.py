"""
Developer : Suresh Perumal
Functionality: Contains a helper functions,
essentially to perform actions like 
                1. To create two objects for playerActions, as two players.
                2. To allow both the users to place the ships
                3. To allow attack operations till the checkwin condition is satisfied.
"""
import playerActions

def PlaceShips(player):
    # To place all the ships of the user, till the ships are emptied.
    while len(player.ships) != 0:
        print('available ships:=', player.ships)
        ship = input('{0} - choose the ship...'.format(player.name))
        position = input('{0} - choose the position...'.format(player.name))
        ship = ship.strip()
        position = position.strip()
        player.placeShip(ship, position)
        player.displayBoard()

def attackInput(player, opponent):
    # To attack the oppenent at the given position.
    print('{0} attacks {1}'.format(player.name, opponent.name))
    position = input('{0} - Enter the position to attack...'.format(player.name))
    position = position.strip()
    if(position == "show both"):
        player.displayBothBoards(opponent)
        attackInput(player, opponent)
    else:
        player.attack(opponent, position)
        player.displayBothBoards(opponent)

#create the player objects
player = [playerActions.PlayerActions(),playerActions.PlayerActions()]
player[0].name = 'Player A'
player[1].name = 'Player B'

print('====== PLAYER A ======')
PlaceShips(player[0])
print('====== PLAYER B ======')
PlaceShips(player[1])
print('----ATTACK-----')

flag = True

# till either of the player wins, it allows user to attack.
while True:
    if(player[0].checkWin()) or (player[1].checkWin()):
        break
    else:
        if flag:
            attackInput(player[0], player[1])
            flag = False
        else:
            attackInput(player[1], player[0])
            flag = True
            
    