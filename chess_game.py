import pygame
from pygame import *
import chess

pygame.init()

app = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Chess with AI")


board = chess.Board()
board1 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\board1.png").convert()
board2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\board2.png").convert()
pawn = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\pawn.png").convert()
pawn2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\pawn2.png").convert()
knight = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\knight.png").convert()
knight2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\knight2.png").convert()
bishop = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\bishop.png").convert()
bishop2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\bishop2.png").convert()
rook = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\rook.png").convert()
rook2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\rook2.png").convert()
queen = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\queen.png").convert()
queen2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\queen2.png").convert()
king = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\king.png").convert()
king2 = pygame.image.load("C:\\Users\\Student\\Desktop\\Michael C\\Chess Engine\\pieces\\king2.png").convert()

currentx = 0
currenty = 0

def draw_board():
    for i in range(4):
        currentx = 0
        currenty = i*128
        index = 0
        for i2 in range(0, 16):
            index += 1
            if index > 8:
                currenty += 64
                currentx = 0
                index = 0
            if index % 2 == 0:
                app.blit(board1, (currentx, currenty))
            else:
                app.blit(board2, (currentx, currenty))
            currentx += 64

def update_chess_pieces():
    currentx = 0
    currenty = 0
    board2 = str(board).replace(" ", "").split("\n")
    for i in range(8):
        currentx = 0
        for i2 in range(8):
            if board2[i][i2] == "p":
                app.blit(pawn2, (currentx, currenty))
            if board2[i][i2] == "P":
                app.blit(pawn, (currentx, currenty))
            if board2[i][i2] == "n":
                app.blit(knight2, (currentx, currenty))
            if board2[i][i2] == "N":
                app.blit(knight, (currentx, currenty))
            if board2[i][i2] == "b":
                app.blit(bishop2, (currentx, currenty))
            if board2[i][i2] == "B":
                app.blit(bishop, (currentx, currenty))
            if board2[i][i2] == "r":
                app.blit(rook2, (currentx, currenty))
            if board2[i][i2] == "R":
                app.blit(rook, (currentx, currenty))
            if board2[i][i2] == "q":
                app.blit(queen2, (currentx, currenty))
            if board2[i][i2] == "Q":
                app.blit(queen, (currentx, currenty))
            if board2[i][i2] == "k":
                app.blit(king2, (currentx, currenty))
            if board2[i][i2] == "K":
                app.blit(king, (currentx, currenty))
        currenty += 64

running = True
while running:
    draw_board()
    update_chess_pieces()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
