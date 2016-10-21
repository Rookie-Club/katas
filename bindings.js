const taille_fourmi = 20;
var world_width, world_height;

window.onload = function () {
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  world_width = canvas.width;
  world_height = canvas.height;

  var fourmi = new Ant();
  dessine_fourmi(fourmi, context);

  btn_avancer.onclick = function () {
    fourmi.forward(taille_fourmi);
    dessine_fourmi(fourmi, context);
  }
};

const dessine_fourmi = function (fourmi, context) {
  context.fillStyle = "black";
  position = decalage_position(fourmi);
  context.fillRect(position.x, position.y, taille_fourmi, taille_fourmi);
}

const decalage_position = function (fourmi) {
  return {
    x: fourmi.position.x - (taille_fourmi / 2) + (world_width / 2),
    y: fourmi.position.y - (taille_fourmi / 2) + (world_height / 2)
  };
}
