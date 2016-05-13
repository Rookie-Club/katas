window.creeUnAutreMonde = function (dimension) {

  var milieu = dimension / 2;
  var orientations = [{x: 0, y: -1}, {x: 1, y: 0}, {x: 0, y: 1}, {x: -1, y: 0}];

  var pointInitial = {x: milieu, y: milieu};
  var orientationInitiale = 0;

  var nouveauMonde = {
    positionFourmi: pointInitial,
    _orientationFourmi: orientationInitiale,

    faitTournerLaFourmiAGauche: function () {
      var nouvelleOrientation = this._orientationFourmi - 1;
      if (nouvelleOrientation < 0) {
        nouvelleOrientation = orientations.length - 1;
      }
      this._orientationFourmi = nouvelleOrientation;
    },
    faitAvancerLaFourmi: function () {
      var nouvellePosition;
      var modifications = this.prochainMouvement();
      nouvellePosition = {x: this.positionFourmi.x + modifications.x, y: this.positionFourmi.y + modifications.y};
      this.positionFourmi = nouvellePosition;
    },
    prochainMouvement: function () {
      return orientations[this._orientationFourmi];
    }
  };

  return nouveauMonde;
}
