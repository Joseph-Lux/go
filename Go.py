from Board import Board
import GoGUI 

gameBoard = Board()
gameBoard.setPiecesBoard()

gameBoard.addPiece(2, 5)
gameBoard.addPiece(2, 6)
gameBoard.addPiece(2, 7)
gameBoard.addPiece(4, 7)
gameBoard.addPiece(3, 7)
gameBoard.addPiece(16, 16)
gameBoard.addPiece(12, 18)
gameBoard.addPiece(0, 1)
gameBoard.addPiece(0, 0)
gameBoard.addPiece(1, 0)
gameBoard.addPiece(0, 2)
gameBoard.addPiece(1, 1)
gameBoard.addPiece(17, 2)

GoGUI.runGame(gameBoard)