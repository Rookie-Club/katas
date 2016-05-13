
describe("La Fourmi de Langton", function () {
    it("est au milieu", function () {
        var monde = autreMonde(20);
        expect(monde.positionFourmi()).toEqual({x:10, y:10});
    });
});
