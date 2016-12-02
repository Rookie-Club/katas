const nouvellePositionFourmi = function (positionFourmi, orientation) {
    return [positionFourmi[0] + orientation[0], positionFourmi[1] + orientation[1]];
}

const nouvelleOrientationFourmi = function (positionCourante, orientation, casesNoires) {
  return [1, 0];
}
