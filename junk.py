# player.placeShip('cruiser','d4')
# player.displayBoard()


# shipLength = self.ships[type]
#             del self.ships[type]
#             print('shiplength', shipLength)
#             print('column', col)
#             print('row', row)
#             print(self.board[row][col])
#             if self.board[row][col] == '':
#                 print('9-col', 9-col)
#                 if 9-col >= shipLength:
#                     #print('able to place the ship')
#                     i = col
#                     print('able to place the ship',i)
#                     for i in range(i, i+shipLength, 1):
#                         print(row, end=" ")
#                         print(i)
#                         self.board[row][i] = '*'
#                         self.displayBoard()
#                         #print(self.board[row][i],'*')
#                 else:
#                     print('not able to place the ship')


def attackShip(self, position):
        col = position[0:1]
        row = int(position[1:len(position)]) #type conversion error if input is 'adfa1'
        if row <=10:
           # print('valid row id')
            try:
                col = self.columnMapping[col]
                #print('column found')
            except KeyError:
                print('incorrect column id')
        else:
            print('incorrect row found')