var calcul_score = function (quilles_tombees) {
  return somme(points_par_lance(regroupe_par_manche(quilles_tombees)));
};

var regroupe_par_manche = function (quilles_tombees) {
  return quilles_tombees;
};

var points_par_lance = function (quilles_tombees) {
  return quilles_tombees.reverse().map(function (current, index, array) {
    var next = array[index - 1];
    var next_next = array[index - 2];
    var prev = array[index + 1];

    if (real_position(array, index) % 2 == 0 && current == 10) {
      return current + next + next_next;
    }

    if (real_position(array, index) % 2 == 1 && current + prev == 10) {
      return current + next;
    }

    if (real_position(array, index) < 20) {
      return current;
    }

    return 0;
  });
};

var somme = function (points) {
  return points.reduce(function(a, b) {
    return a + b;
  }, 0);;
};

var real_position = function (reversed_array, index) {
  return reversed_array.length - index - 1;
};
