window.onload = function () {

    var hiddenBomb = function () {
      var tds = document.getElementsByTagName("td");

      for (var i = 0; i < tds.length; i++) {
        tds[i].onclick = function () {
          return this.style.backgroundColor = "red";
        }
      }
    }

    var generateGrid = function (numberOfTable, numberOfTd) {
      for (var i = 0; i < numberOfTable; i++) {
        var table = document.createElement("table");
        document.body.appendChild(table);

        for (var j = 0; j < 1; j++) {
          var tr = document.createElement("tr");
          table.appendChild(tr);

          for (var k = 0; k < numberOfTd; k++) {
            var td = document.createElement("td");
            tr.appendChild(td.cloneNode(true), document.body.lastChild);
          }
        }
      }
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

    generateGrid(8, 8);
    hiddenBomb();
    createBomb();
    randomBomb();
}
