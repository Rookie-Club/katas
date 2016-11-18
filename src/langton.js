const Ant = function () {

  this.position = {x: 0, y: 0};
  this.direction = {x: 0, y: -1};
  this.colorCase = "white";

  this.move = function () {
    if (this.position.x == 1) {
      this.position.x += this.direction.x;
      this.position.y += this.direction.y;
      this.direction = {x: -1, y: 0};
    } else if (this.position.y == -1) {
      this.position.x += this.direction.x;
      this.position.y += this.direction.y;
      this.direction = {x: 0, y: 1};
    } else {
      this.position.x += this.direction.x;
      this.position.y += this.direction.y;
      this.direction = {x: 1, y: 0};
    }
  }

  this.orientation = function () {
    if (this.direction.x == 0 && this.direction.y == -1) {
      return "North";
    }
    if (this.direction.x == 1 && this.direction.y == 0) {
      return "East";
    }
    if (this.direction.x == 0 && this.direction.y == 1) {
      return "South";
    }
    if (this.direction.x == -1 && this.direction.y == 0) {
      return "West";
    }
  }
}
