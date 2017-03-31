def optimisation_revenu(vols):
    optimum = 0
    for vol in vols:
        optimum = max(vol[2], optimum)
        for vol_compare in vols:
            if duree_compatible(vol, vol_compare):
                optimum = max(vol[2] + vol_compare[2], optimum)
    return optimum

def duree_compatible(vol, vol_compare):
    duree = vol[0] + vol[1]
    return duree <= vol_compare[0]
