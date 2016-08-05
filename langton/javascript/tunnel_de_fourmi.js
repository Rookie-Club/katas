window.onload = function (){
  console.log('je suis chargee !');
  var contexte = terrain.getContext("2d");

  avance.onclick = function () {
    fourmi.avance();
  };
  dessineTerrain(contexte, fourmi);
}
var dessineTerrain = function (contexte, fourmi){
  contexte.fillStyle = "purple";
  contexte.fillRect(0 + (terrain.width / 2), 0 + (terrain.height / 2), 20, 20);
}
