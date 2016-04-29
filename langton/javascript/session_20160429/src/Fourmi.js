window.nouveauMonde = function (dimension) {
    var position = {x: dimension/2, y: dimension/2};
    var direction = {dx: 0, dy: -1};
    var positionFourmi = function () { return position; };
    var directionFourmi = function () { return direction; };

    var construisGrille = function () {
        var i, j;
        var resultat = new Array(dimension);
        for (i = 0; i < dimension; i++) {
            resultat[i] = new Array(dimension);
            for (j = 0; j < dimension; j++) resultat[i][j] = "blanc";
        }
        return resultat;
    };

    var grille = construisGrille();

    var couleurCase = function(x, y) {
        return grille[x][y];
    };

    var tourneAGauche = function () {
        var nouvelleDirection = {};
        nouvelleDirection.dx = direction.dy;
        nouvelleDirection.dy = 0 - direction.dx;
        direction = nouvelleDirection;
    };

    var tourneADroite = function () {
        var nouvelleDirection = {};
        nouvelleDirection.dx = 0 - direction.dy;
        nouvelleDirection.dy = direction.dx;
        direction = nouvelleDirection;
    };

    var bougeFourmi = function () {
        position.x += direction.dx;
        position.y += direction.dy;

        if (couleurCase(position.x, position.y) === "noir") tourneAGauche(); else tourneADroite();

        grille[position.x][position.y] = "noir";
    };


    return {
        positionFourmi: positionFourmi,
        bougeFourmi: bougeFourmi,
        directionFourmi: directionFourmi,
        couleurCase: couleurCase
    };
};
