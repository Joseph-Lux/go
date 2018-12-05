from Piece import Piece
from Group import Group

class Board:
    def __init__(self):
        self.pieces = [[Piece(row, column) for column in range(19)] for row in range(19)]
        self.groups = []
        self.turn = 'X'
        self.ko = None

    def setPiecesBoard(self):
        for row in self.pieces:
            for piece in row:
                piece.board = self

    def checkMove(self, row, column):
        # Check to see if there is already a piece there
        if self.pieces[row][column].player != '-':
            return False

        # Check to see if move is killing itself
        

        # Return the reverse of the ko property 
        # This will return true, we can go there, if there is no ko, 
        # but false, we cannot go there if there is a ko

        return True

    def addPiece(self, row, column):
        # Change the player of the piece at the position of the move
        self.pieces[row][column].player = self.turn 

        # Calculate the liberties of the new move
        self.pieces[row][column].calculateLiberties()

        # Update groups
        self.addToGroups(row, column)

        # Update liberties of opposing pieces around the move
        self.updateLibsAround(row, column)

        # Remove groups
        self.removeGroups()

        # Switch the player
        self.turn = self.oppositeTurn()
        
    def oppositeTurn(self):
        if self.turn == 'X':
            return 'O'
        else:
            return 'X'

    def addToGroups(self, row, column):
        # Make a new group for the new piece
        newGroup = Group(self.turn, self)
        newGroup.appendPiece(self.pieces[row][column])

        # Add the upper neighbor if it matches player
        if row != 0 and self.pieces[row - 1][column].player == self.turn:
            newGroup.appendGroup(self.pieces[row - 1][column].group)

        # Add the right neighbor if it matches player
        if column != 18 and self.pieces[row][column + 1].player == self.turn:
            newGroup.appendGroup(self.pieces[row][column + 1].group)

        # Add the lower neighbor if it matches player
        if row != 18 and self.pieces[row + 1][column].player == self.turn:
            newGroup.appendGroup(self.pieces[row + 1][column].group)

        # Add the left neighbor if it matches player
        if column != 0 and self.pieces[row][column - 1].player == self.turn:
            newGroup.appendGroup(self.pieces[row][column - 1].group)

        newGroup.calculateLiberties()
        self.groups.append(newGroup)

    def removeGroups(self):
        for group in self.groups:
            if not group.calculateLiberties():
                for piece in group.pieces:
                    piece.player = '-'
                self.groups.remove(group)

    def updateLibsAround(self, row, column):
        # Update upper neighbor
        if row != 0 and self.pieces[row - 1][column].player == self.oppositeTurn():
            self.pieces[row - 1][column].liberties -= 1
            self.pieces[row - 1][column].group.liberties -= 1

        # Update right neighbor
        if column != 18 and self.pieces[row][column + 1].player == self.oppositeTurn():
            self.pieces[row][column + 1].liberties -= 1
            self.pieces[row][column + 1].group.liberties -= 1

        # Update lower neighbor
        if row != 18 and self.pieces[row + 1][column].player == self.oppositeTurn():
            self.pieces[row + 1][column].liberties -= 1
            self.pieces[row + 1][column].group.liberties -= 1

        # Update left neighbor
        if column != 0 and self.pieces[row][column - 1].player == self.oppositeTurn():
            self.pieces[row][column - 1].liberties -= 1
            self.pieces[row][column - 1].group.liberties -= 1

    def outputLibs(self):
        string = ''

        for row in self.pieces:
            for item in row:
                string += str(item.liberties) + ' '
            string += "\n"

        print(string)

    def __str__(self):
        # Iterate over each row and then iterate over the items in each row, 
        # keeping spaces between each item and newlines between each row.

        string = ''
        
        for row in self.pieces:
            for item in row:
                string += str(item) + ' '
            string += "\n"

        return string