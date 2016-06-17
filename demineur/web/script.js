window.onload = function () {
  var tds = document.getElementsByTagName('td');
  for (var i in tds) {
    tds[i].onclick = function () {
      this.classList.add("boom");
    };
  }

  starter.onclick = function () {
    grid.innerHTML = "";
    var cell = document.createElement("td");
    cell.className = "base";
    var row = document.createElement("tr");
    row.appendChild(cell);
    var table = document.createElement("table");
    table.appendChild(row);
    grid.appendChild(table);

    tds = document.getElementsByTagName('td');
    for (var i in tds) {
      tds[i].onclick = function () {
        this.classList.add("boom");
      };
    }
  };
};
