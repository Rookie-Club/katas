def score(quilles):
    score = 0

    for index, quille in enumerate(quilles):
        if not lancer_bonus(index):
            score += quille

        if cas_du_spare(index, quilles):
            score += quille

    return score

def lancer_bonus(index):
    return index >= 20

def cas_du_spare(index, quilles):
    return debut_de_manche(index) and dix_tombe_en_deux_coups(index, quilles)

def debut_de_manche(index):
    return index % 2 == 0

def dix_tombe_en_deux_coups(index, quilles):
    return index >= 2 and quilles[index - 2] + quilles[index - 1] == 10
