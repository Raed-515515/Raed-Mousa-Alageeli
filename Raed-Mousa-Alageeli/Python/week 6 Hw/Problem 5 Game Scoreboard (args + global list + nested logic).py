high_score_board = []

def record_game(player, *scores, bonus=0, multiplier=1.0):
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")

    for s in scores:
        if s < 0:
            return (player, 0, 0, "negative score not allowed")

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)
    rank = sorted_board.index((player, total)) + 1

    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return (player, rounds, total, status)


print(record_game("Raed", 10, 20, 30, bonus=5, multiplier=1.2))
print(record_game("Sara", 50, 40))
print(record_game("Omar", 100, 20, 10, 5))

print(high_score_board)
