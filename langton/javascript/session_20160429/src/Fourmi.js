window.nouveauMonde = function (dimension) {
    var positionFourmi = {x: dimension/2, y: dimension/2};
    var couleur = "blanc";

    var couleurCase = function(x, y) {
        return couleur;
    };

    var bougeFourmi = function () {
        var decalage = {dx: 0, dy: -1};
        positionFourmi.x += decalage.dx;
        positionFourmi.y += decalage.dy;

        couleur = "noir";
    };

    return {
        positionFourmi: positionFourmi,
        bougeFourmi: bougeFourmi,
        couleurCase: couleurCase
    };
};
