const assert = require('assert');
const avance = require('../game-of-life').avance;
const recenseVoisins = require('../game-of-life').recenseVoisins;

describe('Au jeu de la vie,', () => {
  it('1 cellule morte reste une cellule morte !', () => {
    const univers = [
      {
        x: 0,
        y: 0,
        vivant: false,
      },
    ]
    const universObtenu = avance(univers)

    assert.equal(universObtenu[0].vivant, false)
  })

  it('1 cellule vivante devient une cellule morte !', () => {
    const univers = [
      {
        x: 0,
        y: 0,
        vivant: true,
      },
    ]
    const universObtenu = avance(univers)

    assert.equal(universObtenu[0].vivant, false)
  })

  describe('Je connais mes voisins,', () => {
    it('je suis au milieu, j\'ai huit voisins', () => {
      const univers = [
        { x: 0, y: 0, vivant: true },
        { x: 1, y: 0, vivant: true },
        { x: 2, y: 0, vivant: true },
        { x: 0, y: 1, vivant: true },
        { x: 1, y: 1, vivant: true },
        { x: 2, y: 1, vivant: true },
        { x: 0, y: 2, vivant: true },
        { x: 1, y: 2, vivant: true },
        { x: 2, y: 2, vivant: true }

      ]

      const voisins = recenseVoisins(univers, univers[4])
      const voisinsAttendus = [
        { x: 0, y: 0, vivant: true },
        { x: 1, y: 0, vivant: true },
        { x: 2, y: 0, vivant: true },
        { x: 0, y: 1, vivant: true },
        { x: 2, y: 1, vivant: true },
        { x: 0, y: 2, vivant: true },
        { x: 1, y: 2, vivant: true },
        { x: 2, y: 2, vivant: true }

    ]

      assert.equal(JSON.stringify(voisins), JSON.stringify(voisinsAttendus))
    })
  })

  xit('Sur 3 cellules vivantes côte à côte, celle du centre survit et les autres meurent', () => {
    const univers = [
      { x: 0, y: 0, vivant: true },
      { x: 1, y: 0, vivant: true },
      { x: 2, y: 0, vivant: true },
    ]
    const universSuivant = [
      { x: 0, y: 0, vivant: false },
      { x: 1, y: 0, vivant: true },
      { x: 2, y: 0, vivant: false },
    ]
    const universObtenu = avance(univers)

    assert.equal(JSON.stringify(universObtenu), JSON.stringify(universSuivant));
  })
});
