"""
Developer : Suresh Perumal
Functionality: Contains a Board Class, essentially to set board properties, by initializing,  
                1. initialize the board
                2. to display board, 
                3. validate the position that user given
                4. Check the available space to place the ship of required length.
"""

class Board:
    board = []
    def __init__(self):
        # initializing variables
        self.name = ''
        self.board = [['-' for i in range(10)] for j in range(10)]  #current player board
        self.battleBoard = [['-' for i in range(10)] for j in range(10)]  #opponent board to keep track of places where attacked.
        self.rowMapping = {'a':0, 'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
        self.ships = {'carrier':5, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}
        self.hitCount = 0
        self.row = 0
        self.col = 0

    def displayBoard(self):
        #printing the neccessary headers.
        print('  1 2 3 4 5 6 7 8 9 10')
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        for i in range(10):
            print(rows[i], end = " ")
            for j in range(10):
                print(self.board[i][j],end =" ")
            print('\n', end="")
    
    def checkSpace(self, type):
        #check the space whether we can place the ship or not, if we can place it will return True or else False.
        shipLength = self.ships[type]
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
        #check the user given space, if the row lies between 1-10 and column lies between a-j
        #  and of length min 2 and max 10 then this function will return True or else False.
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
        # After successful check of index and space availability it will place the ship
        # and delete the ship from the available ships
        shipLength = 0
        if type in self.ships:
            shipLength = self.ships[type]
            if(self.checkPostion(index)):
                # print(self.checkSpace(type))
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

