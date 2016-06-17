window.onload = function () {
  console.log("loaded");
  var tds = document.getElementsByTagName('td');
  console.log(tds);
  for(var i in tds) {
    tds[i].onclick = function () {
      this.classList.add("boom");
    }
  };
}
