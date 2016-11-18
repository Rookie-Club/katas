const Ant = function () {

  this.position = {x: 0, y: 0};
  this.direction = "North";
  this.colorCase = "white";

  this.move = function () {
    if (this.position.x == 1) {
      this.position.y += 1;
      this.direction = "West";
    } else if (this.position.y == -1) {
      this.position.x += 1;
      this.direction = "South";
    } else {
      this.position.y -= 1;
      this.direction = "East";
    }
  }

}
