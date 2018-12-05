
class Piece:
    def __init__(self, row, column):
        self.player = '-'
        self.group = None
        self.ko = False
        self.liberties = 4
        self.row = row
        self.column = column
        self.board = None

    def calculateLiberties(self):
        self.liberties = 4

        # Check the upper liberty
        if self.row == 0 or self.board.pieces[self.row - 1][self.column].player != '-':
            self.liberties -= 1
            
        # Check the lower liberty
        if self.row == 18 or self.board.pieces[self.row + 1][self.column].player != '-':
            self.liberties -= 1 

        # Check the left liberty
        if self.column == 0 or self.board.pieces[self.row][self.column - 1].player != '-':
            self.liberties -= 1

        # Check the right liberty
        if self.column == 18 or self.board.pieces[self.row][self.column + 1].player != '-':
            self.liberties -= 1

    def setBoard(self, board):
        self.board = board

    def __str__(self):
        return self.player
