"""
Developer : Suresh Perumal
Functionality: Contains a PlayerActions Class it was inherited from board class, 
essentially to perform actions like 
                1. Attack the opponent at given position.
                2. to display board both player's board
                3. To check the win condition.
"""

import Board

class PlayerActions(Board.Board):
    def attack(self, obj, position):
        # after checking the given position, 
        # if the opponent board position is * which is a hit and update the battleboard with 1 and increment the hitcount
        # else if the opponent board is '1' or '0' then its a miss, we dont need to update any sts, then its a miss
        # else its miss and update the battleboard as '0'
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
        # It will display both the user board, and battle board.
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
        # if the hitcount as reached the 17 which means the total ships length is 17.
        if self.hitCount == 17:
            print('{0} wins'.format(self.name))
            return True
        else:
            return False