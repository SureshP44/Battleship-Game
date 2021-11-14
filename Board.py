class Board:
    board = []
    def __init__(self):
        self.name = ''
        self.board = [['-' for i in range(10)] for j in range(10)]
        self.battleBoard = [['-' for i in range(10)] for j in range(10)]
        self.rowMapping = {'a':0, 'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
        self.ships = {'carrier':5, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}
        self.hitCount = 0
    def displayBoard(self):
        print('  1 2 3 4 5 6 7 8 9 10')
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for i in range(10):
            print(rows[i], end = " ")
            for j in range(10):
                print(self.board[i][j],end =" ")
            print('\n', end="")
    
    def checkSpace(self, type, index):
        shipLength = 0
        row = index[0:1]
        row = self.rowMapping[row]
        col = int(index[1:len(index)]) #type conversion error if input is 'adfa1'
        i, j = row, col
        if self.board[i][j] == '-':
            if j+shipLength <= 11:
                del self.ships[type]
                for j in range(j, j+shipLength, 1):
                    if self.board[i][j-1] != '-':
                        return False
                return True
            else:
                return False
        else:
            print('already occupied')


    def placeShip(self, type, index):
        # to handle invalid length of row.
        shipLength = 0
        row = index[0:1]
        col = int(index[1:len(index)]) #type conversion error if input is 'adfa1'
        if col <=10:
           # print('valid row id')
            try:
                row = self.rowMapping[row]
                #print('column found')
            except KeyError:
                print('incorrect column id')
        else:
            print('incorrect row found')
        print(self.checkSpace(type, index))
        if type in self.ships:
            shipLength = self.ships[type]
            i, j = row, col
            print(self.checkSpace(type, index))
            if self.board[i][j] == '-':
                if j+shipLength <= 11:
                    del self.ships[type]
                    for j in range(j, j+shipLength, 1):
                        # print(i, end=" ")
                        # print(j)
                        self.board[i][j-1] = '*'
                    print('ship placed.')    
                else:
                    print('cant place here, length is not enough')
            else:
                print('already occupied')

        else:
            print('ship not available')
    
class PlayerActions(Board):
    def attack(self, obj, position):
        row = position[0:1]
        col = int(position[1:len(position)]) #type conversion error if input is 'adfa1'
        if col <=10:
            try:
                row = self.rowMapping[row]
            except KeyError:
                print('incorrect column id')
        else:
            print('incorrect row found')
        i, j = row, col
        if(obj.board[i][j-1] != '-'):
            print('its a hit')
            obj.board[i][j-1] = '1'
            self.battleBoard[i][j-1] = '1'
           # obj.displayBoard()
            self.hitCount = self.hitCount+1
        else:
            print('its a miss')
            obj.board[i][j-1] = '0'
            self.battleBoard[i][j-1] = '0'
           # obj.displayBoard()

    def displayBothBoards(self, obj):
        print('\t{0}\t\t\t{1}'.format(self.name, obj.name))
        print('  1 2 3 4 5 6 7 8 9 10 \t\t  1 2 3 4 5 6 7 8 9 10')
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for i in range(10):
            print(rows[i], end = " ")
            for j in range(10):
                print(self.board[i][j],end =" ")
            print('\t\t',end="")
            print(rows[i], end = " ")
            for j in range(10):
                print(self.battleBoard[i][j],end =" ")
            print('\n', end="")


    def checkWin(self):
        if self.hitCount == 17:
            print('{0} wins', self.name)
            return True
        else:
            return False


        
        
    
player = PlayerActions()


player.placeShip('cruiser', 'a3')
# player.placeShip('cruiser', 'c1')
player.displayBoard()
# player2 = PlayerActions()
# player2.placeShip('carrier', 'e2')
# player2.placeShip('cruiser', 'a3')
# player2.displayBothBoards(player)

# player2.attack(player, 'd6')
# # player.attack(player2, 'a3')
