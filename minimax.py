import chess
from algorithm2 import *

def minimax(board, depth, alpha, beta, maximizingPlayer):
    best_score = -1000000
    best_move = None
    if depth == 0:
        for move in board.legal_moves:
            board.push(move)
            score = algorithm(board, True)
            board.pop()
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move

        if maximizingPlayer:
            bestScore = -float("inf")
            bestMove = None
            for move in board.legal_moves:
                newBoard = board.copy()
                newBoard.push(move)
                score, _ = minimax(newBoard, depth - 1, alpha, beta, False)
                if score > bestScore:
                    bestScore = score
                    bestMove = move
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
            return bestScore, bestMove
        else:
            bestScore = float("inf")
            bestMove = None
            for move in board.legal_moves:
                newBoard = board.copy()
                newBoard.push(move)
                print(minimax(newBoard, depth - 1, alpha, beta, True))
                score, _ = minimax(newBoard, depth - 1, alpha, beta, True)
                if score < bestScore:
                    bestScore = score
                    bestMove = move
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
            return bestScore, bestMove


def main():
    board = chess.Board()
    alpha = -float("inf")
    beta = float("inf")
    print(minimax(board, 2, alpha, beta, True))

if __name__ == "__main__":
    main()
