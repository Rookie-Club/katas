const sizeAnt = 20;
var worldWidth, worldHeight;

window.onload = function () {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  worldWidth = canvas.width;
  worldHeight = canvas.height;
  drawAnt(context);

  move.onclick = function () {
    drawAnt(context);
  };
}

const drawAnt = function (context) {
  context.fillStyle = "black";
  context.fillRect(positionAntX(positionX(0)), positionAntY(positionY(0)), sizeAnt, sizeAnt);
}

const positionAntX = function (oldPositionX) {
  return (oldPositionX * sizeAnt) + (worldWidth/2) - (sizeAnt/2);
}

const positionAntY = function (oldPositionY) {
  return (oldPositionY * sizeAnt) + (worldHeight/2) - (sizeAnt/2);
}
