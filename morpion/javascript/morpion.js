var lastPlayer = "";

var isWinner = function () {
    console.log("pas de gagnant")
}

var insert = function () {
    if (lastPlayer === "X") {
        lastPlayer = "0";
        return "O";
    } else {
        lastPlayer = "X";
        return "X";
    }
}
window.onload = function () {

    document.getElementById("New_Game").onclick = function (e) {
        document.location.reload();
    }
    var cases = document.getElementsByTagName("td");
    console.log(cases);
    for (var i = 0; i < cases.length; i++){
        cases[i].onclick = function (e) {
            console.log(this);
            this.innerHTML = insert();
            isWinner();
        };
    };
}
