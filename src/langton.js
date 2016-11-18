const Ant = function () {

  this.position = {x: 0, y: 0};
  this.direction = {x: 0, y: -1};
  this._orientation = "North";
  this.colorCase = "white";

  this.move = function () {
    this.position.x += this.direction.x;
    this.position.y += this.direction.y;
    this.tourne_a_droite();
  }

  this.tourne_a_droite = function () {
    if (this.direction.x == 0 && this.direction.y == -1) {
      this._orientation = "East";
      this.direction = {x: 1, y: 0};
    } else if (this.direction.x == 1 && this.direction.y == 0) {
      this._orientation = "South";
      this.direction = {x: 0, y: 1};
    } else if (this.direction.x == 0 && this.direction.y == 1) {
      this._orientation = "West";
      this.direction = {x: -1, y: 0};
    } else if (this.direction.x == -1 && this.direction.y == 0) {
      this._orientation = "North";
      this.direction = {x: 0, y: -1};
    }
  }

  this.orientation = function () {
    return this._orientation;
  }
}
