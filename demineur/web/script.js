var bombOnCase = function () {
  return (new Date() % 3) == 0;
};

var revealCase = function () {
  if (this.classList.contains("revealedCase")) { return; }

  this.classList.add("revealedCase");
  if(bombOnCase()) {
    this.classList.add("bomb");
  }
};

window.onload = function () {
  var tds = document.getElementsByTagName("td");
  for (var i = 0; i < tds.length; i++) {
    tds[i].onclick = revealCase;
  }
};
