def creer_diamant(lettre)

  lignes = case lettre
  when 'A'
    [entoure('A', 0)]
  when 'B'
    [entoure('A', 1), entoure(insere(1, 'B'), 0), entoure('A', 1)]
  when 'C'
    [entoure('A', 2), entoure(insere(1, 'B'), 1), entoure(insere(3, 'C'), 0), entoure(insere(1, 'B'), 1), entoure('A', 2)]
  end

  lignes.join("\n")
end

def entoure(lettre, nombre_espaces)
  espace = ' ' * nombre_espaces
  espace + lettre + espace
end

def insere(nombre_espaces, lettre)
  espace = ' ' * nombre_espaces
  lettre + espace + lettre
end
