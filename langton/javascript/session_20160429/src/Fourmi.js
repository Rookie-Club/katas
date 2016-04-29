window.nouveauMonde = function (dimension) {
    var position = {x: dimension/2, y: dimension/2};

    var positionFourmi = function () {
        return position;
    };

    var bougeFourmi = function () {
        var decalage = {dx: 0, dy: -1};
        position.x += decalage.dx;
        position.y += decalage.dy;

        return position
    };

    return {
        positionFourmi: positionFourmi,
        bougeFourmi: bougeFourmi
    };
};
