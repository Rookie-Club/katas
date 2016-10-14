window.onload = function () {
  console.log("ici c'est chargé");
  var canvas = document.getElementById("canvas");
  var context = canvas.getContext("2d");
  context.fillStyle = "red";
  context.fillRect(140, 140, 20, 20);
};


