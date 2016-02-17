batons = int(raw_input("Avec combien de batons voulez vous jouer ? "))
print "Vous jouez avec %d batons !" % batons

count = 0

while batons > 0:
    joueur = (count % 2) + 1
    batons_retirer = int(raw_input("joueur %d combien voulez vous retirez de batons ? " % joueur))
    batons = batons - batons_retirer
    print "il reste %d batons" % batons
    count += 1
