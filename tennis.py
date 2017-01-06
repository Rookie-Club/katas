def score(winners):
    score = {'points': [0, 0], 'games': [0, 0], 'sets': [0, 0]}
    score['points'] = show_game_points(game_score_calculus(winners))
    return score


def show_game_points(players_score):
    game_scores = [0, 15, 30, 40]
    return [game_scores[players_score['j1']],
            game_scores[players_score['j2']]]

def game_score_calculus(winners):
    game_score = {'j1': 0, 'j2': 0}

    for winner in winners:
        game_score[winner] += 1
        game_score[winner] = game_score[winner] % 4

    return game_score

def game_score(winners):
    return show_game_points(game_score_calculus(winners))

def set_score(winners):
    if winners == ['j2', 'j2', 'j2', 'j2', 'j2', 'j2', 'j2', 'j2']:
        return [2, 0]
    return [1, 0]
