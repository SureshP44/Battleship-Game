import Board

# def PlaceShips(player):
#     while len(player.ships) != 0:
#         print('available ships', player.ships)
#         ship = input('choose the ship')
#         position = input('choose the position')
#         player.placeShip(ship, position)
#         player.displayBoard()

def attackInput(player, opponent):
    print('{0} attacks {1}'.format(player.name, opponent.name))
    position = input('position to attack...')
    if(position == "show both"):
        player.displayBothBoards(opponent)
        attackInput(player, opponent)
    else:
        player.attack(opponent, position)
        player.displayBothBoards(opponent)


player = [Board.PlayerActions(),Board.PlayerActions()]
player[0].name = 'Player A'
player[1].name = 'Player B'
player[0].placeShip('cruiser', 'a2')
player[0].placeShip('battleship', 'b3')
player[0].placeShip('submarine', 'g1')
player[0].placeShip('destroyer', 'f6')
player[0].placeShip('carrier', 'i2')
player[1].placeShip('cruiser', 'i2')
player[1].placeShip('battleship', 'c4')
player[1].placeShip('submarine', 'h2')
player[1].placeShip('destroyer', 'a5')
player[1].placeShip('carrier', 'j1')

# PlaceShips(player[0])
# PlaceShips(player[1])
print('----ATTACK-----')
flag = True
print((player[0].checkWin()) or (player[1].checkWin()))
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
            
    