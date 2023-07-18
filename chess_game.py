import pygame
from pygame import *
from minimax_new import minimax
import chess

pygame.init()

app = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Chess with AI")

board = chess.Board()
board.apply_mirror()
board1 = pygame.transform.scale(pygame.image.load("board1.png").convert_alpha(), (64, 64))
board2 = pygame.transform.scale(pygame.image.load("board2.png").convert_alpha(), (64, 64))
pawn = pygame.transform.scale(pygame.image.load("pawn.png").convert_alpha(), (64, 64))
pawn2 = pygame.transform.scale(pygame.image.load("pawn2.png").convert_alpha(), (64, 64))
knight = pygame.transform.scale(pygame.image.load("knight.png").convert_alpha(), (64, 64))
knight2 = pygame.transform.scale(pygame.image.load("knight2.png").convert_alpha(), (64, 64))
bishop = pygame.transform.scale(pygame.image.load("bishop.png").convert_alpha(), (64, 64))
bishop2 = pygame.transform.scale(pygame.image.load("bishop2.png").convert_alpha(), (64, 64))
rook = pygame.transform.scale(pygame.image.load("rook.png").convert_alpha(), (64, 64))
rook2 = pygame.transform.scale(pygame.image.load("rook2.png").convert_alpha(), (64, 64))
queen = pygame.transform.scale(pygame.image.load("queen.png").convert_alpha(), (64, 64))
queen2 = pygame.transform.scale(pygame.image.load("queen2.png").convert_alpha(), (64, 64))
king = pygame.transform.scale(pygame.image.load("king.png").convert_alpha(), (64, 64))
king2 = pygame.transform.scale(pygame.image.load("king2.png").convert_alpha(), (64, 64))

currentx = 0
currenty = 0


def draw_board():
    for i in range(4):
        currentx = 0
        currenty = i * 128
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
    for i in range(0, 64):
        piece = board.piece_at(i)
        if piece is not None:
            piece = piece.symbol()
            position = ((i % 8) * 64, (i // 8) * 64)
            if piece.upper() == "K":
                if board.color_at(i) == chess.BLACK:
                    app.blit(king, position)
                else:
                    app.blit(king2, position)
            if piece.upper() == "Q":
                if board.color_at(i) == chess.BLACK:
                    app.blit(queen, position)
                else:
                    app.blit(queen2, position)
            if piece.upper() == "R":
                if board.color_at(i) == chess.BLACK:
                    app.blit(rook, position)
                else:
                    app.blit(rook2, position)
            if piece.upper() == "B":
                if board.color_at(i) == chess.BLACK:
                    app.blit(bishop, position)
                else:
                    app.blit(bishop2, position)
            if piece.upper() == "N":
                if board.color_at(i) == chess.BLACK:
                    app.blit(knight, position)
                else:
                    app.blit(knight2, position)
            if piece.upper() == "P":
                if board.color_at(i) == chess.BLACK:
                    app.blit(pawn, position)
                else:
                    app.blit(pawn2, position)
        else:
            continue

def get_square_from_click(x, y):
    if x > 512 or x < 0 or y > 512 or y < 0:
        return None
    rows = list("abcdefgh")
    square = f"{rows[x // 64]}{(y // 64) + 1}"
    return square

def computer(depth=3):
    _, move3 = minimax(board, depth, True)
    board.push(move3)
    
move = []
running = True
while running:
    app.fill((0, 0, 0))
    draw_board()
    update_chess_pieces()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                move.append(get_square_from_click(x, y))
                try:
                    if len(move) == 2:
                        move2 = chess.Move.from_uci(f"{move[0]}{move[1]}")
                        if board.is_legal(chess.Move.from_uci(f"{move[0]}{move[1]}")):
                            board.push(move2)
                            computer(2)
                        move = []
                except chess.InvalidMoveError:
                    move = []
                    continue

pygame.quit()
