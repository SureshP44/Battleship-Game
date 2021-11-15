class Board:
    board = []
    def __init__(self):
        self.name = ''
        self.board = [['-' for i in range(10)] for j in range(10)]
        self.battleBoard = [['-' for i in range(10)] for j in range(10)]
        self.rowMapping = {'a':0, 'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
        self.ships = {'carrier':5, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}
        self.hitCount = 0
        self.row = 0
        self.col = 0

    def displayBoard(self):
        print('  1 2 3 4 5 6 7 8 9 10')
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for i in range(10):
            print(rows[i], end = " ")
            for j in range(10):
                print(self.board[i][j],end =" ")
            print('\n', end="")
    
    def checkSpace(self, type):
        shipLength = self.ships[type]
        print(self.row)
        print(self.col)
        i, j = self.row, self.col-1
        if self.board[i][j] == '-':
            if j+shipLength <= 10:
                for j in range(j, j+shipLength, 1):
                    if self.board[i][j-1] != '-':
                        return False
                return True
            else:
                return False
        else:
            return False
    
    def checkPostion(self, index):
        if len(index) == 2 or len(index) == 3:
            self.row = index[0:1]
            try:
                self.col = int(index[1:len(index)]) #type conversion error if input is 'adfa1'
            except ValueError:
                return False
            if self.col < 10:
                # print('valid row id')
                try:
                    self.row = self.rowMapping[self.row]
                    return True
                except KeyError:
                    return False
            else:
                print('======== SPACE WAS NOT ENOUGH :( ======')
                return False
        return False

    def placeShip(self, type, index):
        # to handle invalid length of row.
        shipLength = 0
        #print(self.checkSpace(type, index))
        if type in self.ships:
            shipLength = self.ships[type]
            if(self.checkPostion(index)):
                print(self.checkSpace(type))
                i, j = self.row, self.col
                if self.checkSpace(type):
                    if j+shipLength <= 11:
                        del self.ships[type]
                        for j in range(j, j+shipLength, 1):
                            # print(i, end=" ")
                            # print(j)
                            self.board[i][j-1] = '*'
                        print('======== SHIP PLACED !!!! ======')   
                    else:
                         print('======== Cannot place here, SHIP LENGTH IS NOT ENOUGH :( ======')
                else:
                     print('======== That position is already occupied :( ======')
            else:
                 print('======== That was a INVALID POSITION :( ======')
        else:
            print('======== Ship was not available :( ======')
    
class PlayerActions(Board):
    def attack(self, obj, position):
        if(self.checkPostion(position)):
            i, j = self.row, self.col
            if obj.board[i][j-1] == '*':
                print('======== That was a HIT !!!!! ======')
                obj.board[i][j-1] = '1'
                self.battleBoard[i][j-1] = '1'
                self.hitCount = self.hitCount+1
            elif obj.board[i][j-1] == '1' or obj.board[i][j-1] == '0':
                print('======== That was a MISS :( ======')
            else:
                print('======== That was a MISS :( ======')
                obj.board[i][j-1] = '0'
                self.battleBoard[i][j-1] = '0'
        else:
            print('======== That was a INVALID POSITION :( ======')


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
            print('{0} wins'.format(self.name))
            return True
        else:
            return False

