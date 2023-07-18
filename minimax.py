import chess
from algorithm import *

def minimax(board: chess.Board, depth, maximizing):
    if maximizing:
        best_score = -800
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score = algorithm(board, False)
            board.pop()
            if score > best_score:
                best_score = score
                best_move = move

    else:
        best_score = 800
