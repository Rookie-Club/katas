function Dessiner (afficher) {

  if(afficher =='B'){
    console.log(' A ');
    console.log('B B');
    console.log(' A ');
  }

  if(afficher == 'A'){
    console.log(afficher)
    return afficher;
  }
}

Dessiner(" A \nB B\n A ");

module.exports = Dessiner;
