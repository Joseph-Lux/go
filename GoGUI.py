##################################
# Made by Joseph Lux             #
##################################

##################################
# Important initializing things  #
##################################

import pygame, sys
from pygame.locals import *

pygame.init() # Initialize pygame
FPS = 50 # Frame rate for the game
fpsClock = pygame.time.Clock() # Clock 

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0, 40)
YELLOW = (255, 255, 0, 30)
BLUE = (0, 0, 255)

# Make display surface
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Go')

# Load images 
BACKGROUNDIMAGE = pygame.image.load('ash.jpg')
BLACKPIECE = pygame.transform.scale(pygame.image.load('1024px-Realistic_Go_Stone.svg.png'), (40, 40))
WHITEPIECE = pygame.transform.scale(pygame.image.load('1024px-Realistic_White_Go_Stone.svg.png'), (40, 40))
HL_BLACKPIECE = BLACKPIECE.copy()
HL_WHITEPIECE = WHITEPIECE.copy()
HL_BLACKPIECE.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
HL_WHITEPIECE.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)

##################################
# Event Handling                 #
##################################
# Check if move can be made and make it if it can
def handleClick(box, board):
    if not box[0] or not box[1]:
        return 
    column = (box[0] - 20) // 40
    row = (box[1] - 20) // 40
    if board.checkMove(row, column):
        board.addPiece(row, column)

# Returns a tuple with the x and y position of 
# the box where the mouse is hovering
def getBoxAtMousePos(mousex, mousey):
    for boxx in range(20, 780, 40):
        for boxy in range(20, 780, 40):
            boxRect = pygame.Rect(boxx, boxy, 40, 40)
            if boxRect.collidepoint(mousex, mousey):
                return (boxx, boxy)
    return (None, None)


##################################
# Drawing methods                #
##################################

# Draws the board onto DISPLAYSURF
def drawBoard(box, board):
    # Background image
    DISPLAYSURF.blit(BACKGROUNDIMAGE, (0, 0))

    # Lines 
    for x in range(1, 20):
        pygame.draw.line(DISPLAYSURF, BLACK, (40 * x, 40), (40 * x, 760))

    for y in range(1, 20):
        pygame.draw.line(DISPLAYSURF, BLACK, (40, 40 * y), (760, 40 * y))

    # Circles for star points
    for x in range(3):
        for y in range(3):
            pygame.draw.circle(DISPLAYSURF, BLACK, (160 + x * 240, 160 + y * 240), 3)

    drawPieces(board)

    # Draw cursor on the board
    if box[0] and box[1] and board.checkMove((box[1] - 20) // 40, (box[0] - 20) // 40):
        if board.turn == 'O':
            DISPLAYSURF.blit(HL_WHITEPIECE, box)
        else:
            DISPLAYSURF.blit(HL_BLACKPIECE, box)

# Draw pieces
def drawPieces(board):
    for row in board.pieces:
        for piece in row:
            if piece.player == 'X':
                DISPLAYSURF.blit(BLACKPIECE, (20 + 40 * piece.column, 20 + 40 * piece.row))
            elif piece.player == 'O':
                DISPLAYSURF.blit(WHITEPIECE, (20 + 40 * piece.column, 20 + 40 * piece.row))

##################################
# Main game loop                 #
##################################

def runGame(board):
    while True:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            elif event.type == KEYUP:
                if event.key == K_k:
                    print(board)
                    board.outputLibs()
        
        mousedBox = getBoxAtMousePos(mousex, mousey)
        if mouseClicked:
            handleClick(mousedBox, board)
        drawBoard(mousedBox, board)

        pygame.display.update()
        fpsClock.tick(FPS) 

