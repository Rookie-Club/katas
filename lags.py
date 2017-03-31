def optimisation_revenu(vols):
    optimum = 0
    for vol in vols:
        for vol_compare in vols:
            if compatibilite(vol, vol_compare):
                optimum = max(vol[3] + vol_compare[3], optimum)

    return optimum

def compatibilite(vol, vol_compare):
    duree = vol[1] + vol[2]
    return duree < vol_compare[1]
