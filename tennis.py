def point(index):
    score_range = [0, 15, 30, 40]
    return score_range[index]

def score(winners):
    score = [point(len(winners)), 0]
    if winners == ["j2"]:
        score.reverse()
    return score
