describe('La Fourmi de Langton', function() {
  it('a une position', function () {
    var fourmi = new Fourmi({width: 20, heigth: 20});
    expect(fourmi.position).toEqual({x: 10, y:10});
  });
});

