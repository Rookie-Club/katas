const addEventOnCell = function () {
  tds = document.getElementsByTagName('td');
  for (var i in tds) {
    tds[i].onclick = function () {
      this.classList.add("boom");
    };
  }
};

const buildCells = function (quantity, row) {
  var cell;
  for (var i = 0; i < quantity; i++) {
    cell = document.createElement("td");
    cell.className = "base";
    row.appendChild(cell);
  };
};

const buildRows = function (quantity, table) {
  var row;
  for (var i = 0; i < quantity; i++) {
    row = document.createElement("tr");
    buildCells(quantity, row);
    table.appendChild(row);
  };
};

window.onload = function () {

  starter.onclick = function () {
    grid.innerHTML = "";
    var table = document.createElement("table");
    buildRows(3, table);
    grid.appendChild(table);
    addEventOnCell();
  };
};
