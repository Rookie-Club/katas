describe("romain", function (){
    it("renvoi 0", function (){
        expect(romain()).toEqual(0)
    });
    it("renvoi 1 pour I", function (){
        expect(romain("I")).toEqual(1)
    });
    it("renvoi 5 pour V", function (){
        expect(romain("V")).toEqual(5)
    });
});
