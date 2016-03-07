romain = function (){
    if (!arguments.length || arguments[0] === "") { return 0 }

    var nombre_romain = arguments[0].split(""); // ["I"]
    var dico = {"I":1, "V":5, "X":10};

    var result = 0;
    for(var i = 0; i < nombre_romain.length; i++) {
        result += dico[nombre_romain[i]]
    }
    return result;
};

romain_recursif = function (){
    if (!arguments.length || arguments[0] === "") { return 0 }
    var nombre_romain = arguments[0];
    var dico = {"I":1, "V":5, "X":10};
    romain_array = nombre_romain.split("").reverse(); //=> ["I", "I"]
    return dico[romain_array.pop(0)] + romain(romain_array.join(""))
};
