# Fourmi de langton

L'idée est de construire un automate cellulaire, [La fourmi de Langton](https://fr.wikipedia.org/wiki/Fourmi_de_Langton).

Les regles:


> Les cases d'une grille bidimensionnelle peuvent être blanches ou noires. On considère arbitrairement l'une de ces cases comme étant l'emplacement initial de la fourmi. Dans l'état initial, toutes les cases sont de la même couleur.

> La fourmi peut se déplacer à gauche, à droite, en haut ou en bas d'une case à chaque fois selon les règles suivantes :

> - Si la fourmi est sur une case noire, elle tourne de 90° vers la droite, change la couleur de la case en blanc et avance d'une case.

> - Si la fourmi est sur une case blanche, elle tourne de 90° vers la gauche, change la couleur de la case en noir et avance d'une case.

> Il est également possible de définir la fourmi de Langton comme un automate cellulaire où la plupart des cases de la grille sont blanches ou noires et où la case de la fourmi peut prendre huit états différents, codant à la fois sa couleur et la direction de la fourmi.
