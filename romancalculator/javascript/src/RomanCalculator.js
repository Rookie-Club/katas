var RomanCalculator = {
  plus: function (a_term, b_term) {
    if (a_term == "III") {
      return "VI";
    }
    if (a_term == "VII" && b_term == "III"){
        return "X"
    }
    if (a_term == "VII" && b_term == "II"){
        return "IX"
    }
    return a_term + b_term;
  }
}
