var assert = require('assert');
var compareMains = require('../src/mainPoker.js');

describe('Poker', function (){
	

	it("Sans combinaisons, l'As gagne sur le roi", function (){
		var mainNoir = ['2Coeur', '3Carreau', '5Pique', '9Coeur', 'RCarreau'];
		var mainBlanche = ['2Carreau', '3Coeur', '4Pique', '8Coeur', 'ACoeur'];
		var resultatAttendu = mainBlanche;

		var resultat = compareMains(mainNoir, mainBlanche);  

		assert.equal(resultatAttendu, resultat)

	});

	it("Sans combinaisons, le roi gagne sur la dame", function (){
		var mainNoir = ['2Coeur', '3Carreau', '5Pique', '9Coeur', 'RCarreau'];
		var mainBlanche = ['2Carreau', '3Coeur', '4Pique', '8Coeur', 'DCoeur'];
		var resultatAttendu = mainNoir;

		var resultat = compareMains(mainNoir, mainBlanche);  

		assert.equal(resultatAttendu, resultat)

	});

});