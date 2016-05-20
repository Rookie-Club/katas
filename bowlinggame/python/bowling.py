def lancer_joueur(quilles_tomber):
    score = 0
    manche = 0
    lancer = 0

    while manche >= 10:
        while lancer <= 2 and quilles_restantes != 0:
            lancer = lancer + 1
            quilles_restantes = quilles_debout - quilles_tomber
            score = score + (quilles_debout - quilles_restantes)
        return score
        manche = manche + 1
        lancer = 0
    return score
    if quilles_tomber == 10 and lancer == 1:
        while manche != 12:
            lancer = 0
            while lancer <= 2 and quilles_restantes != 0:
                lancer = lancer + 1
                quilles_restantes = quilles_debout - quilles_tomber
                score = quilles_debout - quilles_restantes
            return score
            manche = manche + 1
            lancer = 0
        return score + (quilles_debout - quilles_restantes)
    else:
        return score
