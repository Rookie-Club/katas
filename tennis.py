def point(index):
    score_range = [0, 15, 30, 40]
    return score_range[index]

def score(winners):
    score = [0, 0]

    for winner in winners:
        if winner == "j1":
            score[0] += 1
        else:
            score[1] += 1

    return [point(score[0]), point(score[1])]
