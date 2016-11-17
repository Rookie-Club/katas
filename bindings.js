const sizeAnt = 20;
var worldWidth, worldHeight;

window.onload = function () {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  worldWidth = canvas.width;
  worldHeight = canvas.height;
  var ant = new Ant();
  drawAnt(ant, context);

  forward.onclick = function () {
    ant.forward(sizeAnt);
    drawAnt(ant, context);
  };
}

const drawAnt = function (ant, context) {
  var position = positionAnt(ant);
  context.fillStyle = "black";
  context.fillRect(position.x, position.y, sizeAnt, sizeAnt);
}

const positionAnt = function (ant) {
  return {
    x: ant.position.x + (worldWidth/2) - (sizeAnt/2),
    y: ant.position.y + (worldHeight/2) - (sizeAnt/2)
  }
}
