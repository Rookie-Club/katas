var Nim = function (batons_au_depart) {
  return {
    batons_restants: batons_au_depart,
    joueur_courant : "joueur 1",
    retire: function (batons_a_retirer) {
      if (batons_a_retirer > 3) { return false; };
      this.batons_restants = this.batons_restants - batons_a_retirer;
      this.joueur_courant = this.joueur_courant == "joueur 2" ? "joueur 1" : "joueur 2";
      return true;
    }
  };
};
