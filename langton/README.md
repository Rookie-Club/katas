[Jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)

À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :

- Une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît).
- Une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.


## Pour le CPP
On c'est basé sur [exercism](http://exercism.io) pour savoir comment faire des tests en C++. Du coup on a toute leur infrastructure.

Pour lancer les tests:

`mkdir build && cd build && cmake -G "Unix Makefiles" ..`

puis (dans le repertoire build)

`make clean && make`

_attention, le build construit est en fait un jeu de test, pas un programme `main`_
