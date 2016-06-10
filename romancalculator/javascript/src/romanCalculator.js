var RomanCalculator = function () {
  return {
    terms: [],
    add: function () {
      var result = "";
      for (var i = 0; i < this.terms.length; i++) {
        result += this.terms[i];
      }
      return result;
    },
    enter: function (term) {
      this.terms.push(term);
    }
  }
}
