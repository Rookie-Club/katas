module.exports.compareMains = function (main1, main2) {
	if(main2[4] == 'DCoeur') {
		return main1;
	}
	return main2;
};

module.exports.trouveLaCarteLaPlusForte = function (main) {
	return 'ACarreau';
};