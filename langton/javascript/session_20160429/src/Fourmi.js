window.nouveauMonde = function () {
    var position = {x: 10, y: 10};

    var positionFourmi = function () {
        return position;
    };

    var bougeFourmi = function () {
        return position = {x: 10, y: 9};
    };

    return {
        positionFourmi: positionFourmi,
        bougeFourmi: bougeFourmi
    };
};
