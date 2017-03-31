def optimise_revenu(vols):
    informations_vols = vols.split()
    if len(informations_vols) < 5:
        return int(informations_vols[3])
    return max( int(informations_vols[3]) + int(informations_vols[7]), int(informations_vols[7]) + int(informations_vols[11]), int(informations_vols[3]) + int(informations_vols[11]) )
