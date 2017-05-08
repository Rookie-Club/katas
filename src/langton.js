function Fourmi (position_initiale, direction_initiale, cases_noires) {
  this.position_actuelle = position_initiale;
  this.direction_actuelle = direction_initiale;
  this.cases_noires = cases_noires;

  this.avance = function () {
        this.position_actuelle = [3, 5];
        this.direction_actuelle = "Est";
        this.cases_noires = [[3, 4]];
  };

  this.change_couleur = function () {
    if (is_in_array(this.cases_noires, this.position_actuelle)){
      this.cases_noires.pop(this.position_actuelle);
    } else {
      this.cases_noires.push(this.position_actuelle);
  }
  };
};

var is_in_array = function(array, element){
    var string_of_array = JSON.stringify(array);
    return string_of_array.includes(element)
};
