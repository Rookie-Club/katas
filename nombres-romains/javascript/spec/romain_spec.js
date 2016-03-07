describe("romain", function (){
    assertRomain = function (nombre_romain, entier) {
        if (nombre_romain === undefined) {
            expect(romain()).toEqual(entier);
            expect(romain_recursif()).toEqual(entier);
        } else {
            expect(romain(nombre_romain)).toEqual(entier);
            expect(romain_recursif(nombre_romain)).toEqual(entier);
        }
    }

    it("renvoi 0", function (){
        assertRomain(undefined, 0);
    });
    it("renvoi 1 pour I", function (){
        assertRomain("I", 1);
    });
    it("renvoi 5 pour V", function (){
        assertRomain("V", 5);
    });
    it("renvoi 10 pour X", function (){
        assertRomain("X", 10);
    });
    it("renvoi 2 pour II", function (){
        assertRomain("II", 2);
    });
    it("renvoi 7 pour VII", function (){
        assertRomain("VII", 7);
    });
});
