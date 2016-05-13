window.creeUnAutreMonde = function (dimension) {

  var milieu = dimension / 2;
  var orientations = [{label: "N", modifications: {x: 0, y: -1}},
    {label: "E", modifications: {x: 1, y: 0}},
    {label: "S", modifications: {x: 0, y: 1}},
    {label: "O", modifications: {x: -1, y: 0}}];

  var pointInitial = {x: milieu, y: milieu};
  var orientationInitiale = 0;

  var nouveauMonde = {
    positionFourmi: pointInitial,
    _orientationFourmi: orientationInitiale,
    orientationFourmi: orientations[orientationInitiale].label,
    faitTournerLaFourmiAGauche: function () {
      var nouvelleOrientation = this._orientationFourmi - 1;
      if (nouvelleOrientation < 0) {
        nouvelleOrientation = 3;
      }
      this._orientationFourmi = nouvelleOrientation;
      this.orientationFourmi = orientations[nouvelleOrientation].label;
    },
    faitAvancerLaFourmi: function () {
      var nouvellePosition;
      var modifications = orientations[this._orientationFourmi].modifications;
      nouvellePosition = {x: this.positionFourmi.x + modifications.x, y: this.positionFourmi.y + modifications.y};
      this.positionFourmi = nouvellePosition;
    }
  };

  return nouveauMonde;
}
