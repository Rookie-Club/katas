var assert = require("assert");
var compareMains = require('./pokerhand.js');

describe("pokerhand test", function(){
	it("Comparer deux cartes", function(){
		var carteUn = "roiCarreau";
		var carteDeux = "asCoeur";
		var resultatAttendu = "asCoeur";

		var resultat = compareMains(carteUn, carteDeux);
		
		assert.equal(resultat, resultatAttendu);
	});
})