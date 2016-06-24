var startNewGame = function () {
  location.reload();
};

var bombOnCase = function (on_case) {
  return on_case.getAttribute('mine');
};

var clickableCase = function () {
  return function () {
    return (!this.classList.contains("revealedCase") && !this.classList.contains("flag"))
  }
}

var canReveal = function (element) {
  return !(element.hasAttribute("mine"));
}

var revealAdjCases = function (case_position, element) {
  if(canReveal(element)) {
    element.classList.add("revealedCase");
  }
};


var revealCase = function () {
  return function () {
    if (!clickableCase().bind(this)()) { return; }

    this.classList.add("revealedCase");
    if(bombOnCase(this)) {
      this.classList.add("bomb");
    }
  }
};

var putFlag = function () {
  return function () {
    this.classList.toggle("flag");
  }
};

var clueCase = function () {
  //this.classList.add("clue_plus_1");
  //clue = this.classList.contains("clue_plus_1");
  //if (this.classList.contains("clue_plus_1")) { return clue.innerHTML = "1"; }
}

var random_case = function () {
  return Math.floor(Math.random() * 64);
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

var revealCaseOrPutFlag = function () {
  if (flag.checked) {
    putFlag().bind(this)();
  } else {
    revealCase().bind(this)();
  }
}

window.onload = function () {
  newgame.onclick = startNewGame;

  var tds = document.getElementsByTagName("td");
  var number_of_mines = 10;
  var cases_with_mine = makeCasesWithMineList(number_of_mines);
  var clue_plus_1 = clueCase(number_of_mines);
  total.innerHTML = number_of_mines;
  founded.innerHTML = 0;

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

  document.addEventListener('keydown', function (event) {
    const keyName = event.key;
    if (event.key == 'o') {
      for (var i = 0; i < tds.length; i++) {
        revealAdjCases(i, tds[i]);
      }
    }
  })
};

