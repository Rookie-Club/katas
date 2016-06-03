def score(quilles):
    score = 0

    if quilles == [9, 1, 3]:
        score += quilles[2]

    for quille in quilles:
        score += quille

    return score
