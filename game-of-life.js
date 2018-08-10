const avance = (univers) => {
  univers[0].vivant = false

  return univers
}

const recenseVoisins = (univers, cellule) => {
  const enleveCelluleCourante = (celluleScrutee) =>
    !(celluleScrutee.x == cellule.x && celluleScrutee.y == cellule.y)

  const selectionneVoisins = (celluleScrutee) =>
    celluleScrutee.x <= (cellule.x + 1) &&
    celluleScrutee.x >= (cellule.x - 1) &&
    celluleScrutee.y <= (cellule.y + 1) &&
    celluleScrutee.y >= (cellule.y - 1)

  return univers.filter(selectionneVoisins).filter(enleveCelluleCourante)
}

module.exports = {avance, recenseVoisins}
