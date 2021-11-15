import Board

def PlaceShips(player):
    while len(player.ships) != 0:
        print('available ships:=', player.ships)
        ship = input('{0} - choose the ship...'.format(player.name))
        position = input('{0} - choose the position...'.format(player.name))
        player.placeShip(ship, position)
        player.displayBoard()

def attackInput(player, opponent):
    print('{0} attacks {1}'.format(player.name, opponent.name))
    position = input('{0} - Enter the position to attack...'.format(player.name))
    if(position == "show both"):
        player.displayBothBoards(opponent)
        attackInput(player, opponent)
    else:
        player.attack(opponent, position)
        player.displayBothBoards(opponent)


player = [Board.PlayerActions(),Board.PlayerActions()]
player[0].name = 'Player A'
player[1].name = 'Player B'

print('====== PLAYER A ======')
PlaceShips(player[0])
print('====== PLAYER B ======')
PlaceShips(player[1])
print('----ATTACK-----')
flag = True
# print((player[0].checkWin()) or (player[1].checkWin()))
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
            
    