window.onload = function (){
  console.log('je suis chargee !');
  var contexte = terrain.getContext("2d");

  avance.onclick = function () {
    fourmi.avance();
  };
  dessineTerrain(contexte, fourmi);
}
