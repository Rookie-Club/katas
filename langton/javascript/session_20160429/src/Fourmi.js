window.nouveauMonde = function (dimension) {
    var position = {x: dimension/2, y: dimension/2};
    var couleur = "blanc";
    var direction = {dx: 0, dy: -1};

    var couleurCase = function(x, y) {
        return couleur;
    };

    var positionFourmi = function () { return position; };
    var directionFourmi = function () { return direction; };

    var tourneADroite = function () {
        var nouvelleDirection = {};
        nouvelleDirection.dx = 0 - direction.dy;
        nouvelleDirection.dy = direction.dx;
        direction = nouvelleDirection;
    };

    var bougeFourmi = function () {
        var decalage = {dx: 0, dy: -1};
        position.x += decalage.dx;
        position.y += decalage.dy;

        tourneADroite();

        couleur = "noir";
    };


    return {
        positionFourmi: positionFourmi,
        bougeFourmi: bougeFourmi,
        directionFourmi: directionFourmi,
        couleurCase: couleurCase
    };
};
