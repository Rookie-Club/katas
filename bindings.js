const sizeAnt = 20;
var worldWidth, worldHeight;

window.onload = function () {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  worldWidth = canvas.width;
  worldHeight = canvas.height;
  drawAnt(0, 0, context);

  move.onclick = function () {
    drawAnt(0, -1, context);
  };
}

const drawAnt = function (antX, antY, context) {
  context.fillStyle = "black";
  context.fillRect(positionAntX(antX), positionAntY(antY), sizeAnt, sizeAnt);
}

const positionAntX = function (oldPositionX) {
  return (oldPositionX * sizeAnt) + (worldWidth/2) - (sizeAnt/2);
}

const positionAntY = function (oldPositionY) {
  return (oldPositionY * sizeAnt) + (worldHeight/2) - (sizeAnt/2);
}
