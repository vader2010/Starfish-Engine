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

    score2 = 0
    for piece in pieces:
        piece = piece.lower()
        if piece == "q":
            score2 += 90
        if piece == "r":
            score2 += 50
        if piece == "b":
            score2 += 35
        if piece == "n":
            score2 += 30
        if piece == "p":
            score2 += 10

    score += (score2 / 100)
    count = 0
    board2 = list(str(board).replace(" ", "").replace("\n", ""))
    attacks = []
    attack_total = 0

    for i in range(0, 64):
        if team:
            if str(board2[i]).isupper():
                for attack in board.attacks(i):
                    count += 1
        else:
            if str(board2[i]).islower():
                for attack in board.attacks(i):
                    count += 1
                    attacks.append(f"{board.piece_at(i)}")

    for i in range(len(attacks)):
        new = attacks[i].split("-")
        piece = new[0].lower()
        if piece == "q":
            attack_total += 0.05
        if piece == "r":
            attack_total += 0.035
        if piece == "b":
            attack_total += 0.025
        if piece == "n":
            attack_total += 0.02
        if piece == "p":
            attack_total += 0.005

    score += (count / 50) + attack_total
    return score


board = chess.Board()
score = algorithm(board, chess.WHITE)
