describe("La fourmi de Langton", function () {
    it("est au centre", function () {
        var monde = autreMonde(20);
        expect(monde.positionFourmi()).toEqual({x: 10, y: 10});
    });
    it("orientée vers le nord", function () {
        var monde = autreMonde(20);
        expect(monde.orientationFourmi()).toEqual({x: 10, y: 9});
    });
});
