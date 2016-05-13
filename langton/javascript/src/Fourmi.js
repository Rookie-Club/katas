window.creeUnAutreMonde = function (dimension) {

  var milieu = dimension / 2;

  var point_initial = {x: milieu, y: milieu};
  var au_nord = {x: milieu - 1, y: milieu};

  return {
    positionFourmi: point_initial,
    orientationFourmi: au_nord
  };
}
