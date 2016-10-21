const Ant = function () {
  this.position = {x: 0, y: 0};
  this.color = "white";
  this.forward = function (caseInWorld) {
    this.position.y -= caseInWorld;
  };
  this.color = "white" ? "black" : "white";
};
