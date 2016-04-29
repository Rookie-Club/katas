describe("La Fourmi de Langton", function () {
    it("est au milieu", function () {
        var monde = nouveauMonde(20);
        expect(monde.positionFourmi).toEqual({x: 10, y: 10});
    });

    it("au debut se deplace au nord", function () {
        var monde = nouveauMonde(20);
        monde.bougeFourmi();
        expect(monde.positionFourmi).toEqual({x: 10, y: 9});
    });

    it("color la case", function () {
        var monde = nouveauMonde(20);
        expect(monde.couleurCase(10, 9)).toEqual("blanc");
        monde.bougeFourmi();
        expect(monde.couleurCase(10, 9)).toEqual("noir");
    });
});
