import chess
from algorithm import *

def minimax(board: chess.Board, depth, maximizing, team, alpha=-float('inf'), beta=float('inf')):

    if depth == 0:
        best_score = -800
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score2 = algorithm(board, team)
            board.pop()
            if score2 > best_score:
                best_score = score2
                best_move = move
        return best_score, best_move

    if maximizing:
        best_score = -800
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score3, move2 = minimax(board=board, depth=depth - 1, maximizing=False, team=team, alpha=alpha, beta=beta)
            score2 = algorithm(board, team)
            if board.is_check():
                score2 -= 1
            board.pop()
            if score2 is None:
                return 0
            if score2 > best_score and score2 > score3:
                best_score = score2
                best_move = move
            alpha = max(alpha, score2)
            if beta <= alpha:
                break

    else:
        best_score = 800
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score3, move2 = minimax(board, depth - 1, True, team, alpha=alpha, beta=beta)
            score2 = algorithm(board, team)
            if board.is_into_check(move):
                score2 += 0.5
            board.pop()
            if score2 < best_score and score2 < score3:
                best_score = score2
                best_move = move
            beta = min(beta, score2)
            if beta <= alpha:
                break

    # Check if no legal moves were found
    if best_move is None:
        return (0, None)

    return best_score, best_move

if __name__ == '__main__':
    board = chess.Board()
    print(minimax(board=board, depth=3, maximizing=True, team=chess.BLACK))
