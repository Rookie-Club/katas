window.onload = function () {

  var generateGrid = function (gridSize) {
    var table = document.createElement("table");
    document.body.appendChild(table);

    for (var i = 0; i < gridSize; i++) {
      var tr = document.createElement("tr");
      table.appendChild(tr);

      for (var k = 0; k < gridSize; k++) {
        var td = document.createElement("td");
        td.onclick = revealCase;
        tr.appendChild(td);
      }
    }
  }

  var revealCase = function () {
    this.classList.add("mine");
  }

  var createBomb = function () {
    var newCase = [];
    var numberOfMine = 10;
    var random = randomBomb();
    for (var i = 0; i < numberOfMine; i++) {
      newCase.push(random);
    }
  }

  var randomBomb = function () {
    return Math.floor(Math.random() * 64);
  }

  generateGrid(8);
  createBomb();
  randomBomb();
}
