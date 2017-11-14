On c'est basé sur [exercism](http://exercism.io) pour savoir comment faire des tests en C++. Du coup on a toute leur infrastructure.

Pour lancer les tests:

`mkdir build && cd build && cmake -G "Unix Makefiles" ..`

puis (dans le repertoire build)

`make clean && make`

_attention, le build construit est en fait un jeu de test, pas un programme `main`_
