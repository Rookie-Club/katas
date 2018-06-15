var assert = require('assert');
var compareMains = require('../src/mainPoker.js');

describe('Poker', function (){
	
	it('Sans combinaisons, la carte la plus forte gagne', function (){
		var mainNoir = ['2Coeur', '3Carreau', '5Pique', '9Coeur', 'RCarreau'];
		var mainBlanche = ['2Coeur', '3Coeur', '4Pique', '8Coeur', 'ACoeur'];
		var resultatAttendu = mainBlanche;

		var resultat = compareMains(mainNoir, mainBlanche);  

		assert.equal(resultatAttendu, resultat)

	});
});