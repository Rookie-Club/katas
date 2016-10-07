var Nim = function (batons_au_depart) {
  return {
    batons_restants: batons_au_depart,
    retire: function (batons_a_retirer) {
      if (batons_a_retirer > 3) { return false; };
      this.batons_restants = this.batons_restants - batons_a_retirer;
      return true;
    }
  };
};
