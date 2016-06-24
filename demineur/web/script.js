var startNewGame = function () {
  location.reload();
};

var bombOnCase = function (on_case) {
  return on_case.getAttribute('mine');
};

var revealCase = function () {
  if (this.classList.contains("revealedCase")) { return; }

  this.classList.add("revealedCase");
  if(bombOnCase(this)) {
    this.classList.add("bomb");
  }
};

var clueCase = function () {
  //this.classList.add("clue_plus_1");
  //clue = this.classList.contains("clue_plus_1");
  //if (this.classList.contains("clue_plus_1")) { return clue.innerHTML = "1"; }
}

var random_case = function () {
  return Math.floor(Math.random() * 64) + 1;
}

var makeCasesWithMineList = function (number_of_mines) {
  var casesWithMine = [];
  while (casesWithMine.length < number_of_mines) {
    var random = random_case();
    if (!casesWithMine.includes(random)) {
      casesWithMine.push(random);
    }
  }
  return casesWithMine;
}

window.onload = function () {
  newgame.onclick = startNewGame;

  var tds = document.getElementsByTagName("td");
  var number_of_mines = 10;
  var cases_with_mine = makeCasesWithMineList(number_of_mines);
  var clue_plus_1 = clueCase(number_of_mines);

  for (var i = 0; i < tds.length; i++) {

    if (number_of_mines > 0 && cases_with_mine.includes(i)) {
      tds[i].setAttribute('mine', true);
      number_of_mines -= 1;
    }
    
    if (number_of_mines > 0 && cases_with_mine.includes(i+1 && i-1) && !cases_with_mine.includes(i)) {
      console.log("Clue");
      tds[i].setAttribute('clue_plus_1', true);
    }

    tds[i].onclick = revealCase;
    tds[i].onclick = clueCase;
  }
};
