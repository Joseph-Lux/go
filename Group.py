 # A group is just a list of pieces (assumably that are all connected)

class Group:
    def __init__ (self, player, board):
        self.pieces = []
        self.liberties = 0
        self.player = player
        self.board = board

    def appendPiece(self, piece):
        self.pieces.append(piece)
        piece.group = self
    
    # Append an entire group 
    def appendGroup(self, group):
        for piece in group.pieces:
            self.appendPiece(piece)
            piece.group = self
        self.board.groups.remove(group)

    # A method that sums all the liberties of the pieces in the group list
    def calculateLiberties(self):
        liberties = 0
        for piece in self.pieces:
            piece.calculateLiberties()
            liberties += piece.liberties
        return liberties 