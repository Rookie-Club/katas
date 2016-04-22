window.autreMonde = function (dimension) {
    var laDeclarationDePositionFourmi = function () {
        return {x: dimension / 2, y: dimension / 2};
    };

    return {
        positionFourmi: laDeclarationDePositionFourmi
    };
};

describe("La Fourmi de Langton", function () {
    it("est au milieu", function () {
        var monde = autreMonde(20);
        expect(monde.positionFourmi()).toEqual({x:10, y:10});
    });
});
