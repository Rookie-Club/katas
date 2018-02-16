

def potter(panier)
  prixUnitaire = 8
  reductions = [1, 0.95, 0.90, 0.80, 0.75]
  prixDuPanier = 0

  copieDuPanier = panier

  while copieDuPanier.sum != 0
    tailleSousFamille = 0
    copieDuPanier.each_with_index do |nbTomes, index|
      if nbTomes != 0
        copieDuPanier[index] -= 1
        tailleSousFamille += 1
      end
    end
    prixDuPanier += tailleSousFamille * prixUnitaire * reductions[tailleSousFamille - 1]
  end

  prixDuPanier
end