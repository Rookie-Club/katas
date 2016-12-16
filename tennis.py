def show_points(players_score):
    score_range = [0, 15, 30, 40]
    return [score_range[players_score['j1']],
            score_range[players_score['j2']]]

def score_calculus(winners):
    score = {'j1': 0, 'j2': 0}

    for winner in winners:
        score[winner] += 1

    return score

def score(winners):
   return show_points(score_calculus(winners))
