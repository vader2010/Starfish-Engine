import chess


def algorithm(board: chess.Board, team):
    score = 0
    # VALUATING PIECES
    board2 = str(board).replace(" ", "").split("\n")
    pieces = []
    for i in range(8):
        for i2 in range(8):
            if team:
                if board2[i][i2].isupper():
                    pieces.append(board2[i][i2])
            else:
                if board2[i][i2].islower():
                    pieces.append(board2[i][i2])

    print(pieces)

    for i in range()

board = chess.Board()

algorithm(board, chess.WHITE)
