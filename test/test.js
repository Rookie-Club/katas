var assert = require('assert');
var Poker = require('../src/mainPoker.js');

describe('Poker', function (){
	
	describe('Compare mains', function (){
		it("Sans combinaisons, l'As gagne sur le roi", function (){
			var mainNoire = ['2Coeur', '3Carreau', '5Pique', '9Coeur', 'RCarreau'];
			var mainBlanche = ['2Carreau', '3Coeur', '4Pique', '8Coeur', 'ACoeur'];
			var resultatAttendu = mainBlanche;

			var resultat = Poker.compareMains(mainNoire, mainBlanche);  

			assert.equal(resultatAttendu, resultat)

		});

		it("Sans combinaisons, le roi gagne sur la dame", function (){
			var mainNoire = ['2Coeur', '3Carreau', '5Pique', '9Coeur', 'RCarreau'];
			var mainBlanche = ['2Carreau', '3Coeur', '4Pique', '8Coeur', 'DCoeur'];
			var resultatAttendu = mainNoire;

			var resultat = Poker.compareMains(mainNoire, mainBlanche);  

			assert.equal(resultatAttendu, resultat)
	 
		});
	});
	describe('Trouve la carte la plus forte', function (){
		it("L'as est le plus fort", function (){
			var main = ['2Coeur', 'ACarreau', '5Pique', '9Coeur', 'RCarreau'];
			var resultatAttendu = 'ACarreau';

			var resultat = Poker.trouveLaCarteLaPlusForte(main);  

			assert.equal(resultatAttendu, resultat)
	 
		});
	});

 
});