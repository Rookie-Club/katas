var fourmi = {
  avance: function () {
    console.log("coucou j'avance");
  }
};
var dessineTerrain = function (contexte, fourmi){
  contexte.fillStyle = "purple";
  contexte.fillRect(0 + (terrain.width / 2), 0 + (terrain.height / 2), 20, 20);
}
