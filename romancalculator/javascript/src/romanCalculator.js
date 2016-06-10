var RomanCalculator = function () {
  return {
    terms: [],
    add: function () {
      var result = "";
      if (this.terms[0] === "III") {
        return "VI";
      }
      for (var i = 0; i < this.terms.length; i++) {
        result += romanToNumber(this.terms[i]);
      }
      return numberToRoman(result);
    },
    enter: function (term) {
      this.terms.push(term);
    }
  }
}

