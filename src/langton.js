function Fourmi (position_initiale, direction_initiale, cases_noires) {
  this.position_actuelle = position_initiale;
  this.direction_actuelle = direction_initiale;
  this.cases_noires = cases_noires;

  this.avance = function () {
        this.change_couleur();
        this.position_actuelle = [3, 5];
        this.direction_actuelle = [1, 0];
  };

  this.change_couleur = function () {
    if (is_in_array(this.cases_noires, this.position_actuelle)){
      this.cases_noires.pop(this.position_actuelle);
    } else {
     this.cases_noires.push(this.position_actuelle);
  }
  };

  this.change_direction = function () {
    var tableau_conversion = {
      "Ouest" : [-1, 0],
      "Nord": [0, 1],
      "Est": [1, 0],
      "Sud": [0, -1]
    };
    if (is_in_array(this.cases_noires, this.position_actuelle)){
      this.direction_actuelle =[this.direction_actuelle[1]*-1, this.direction_actuelle[0]*1];
    } else {
      this.direction_actuelle = [this.direction_actuelle[1]*1, this.direction_actuelle[0]*-1];
    }
  };
};


var is_in_array = function(array, element){
    var string_of_array = JSON.stringify(array);
    return string_of_array.includes(element)
};
