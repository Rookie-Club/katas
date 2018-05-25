require "minitest/autorun"

if ARGV[0] 
  lettre = ARGV[0]
else
  puts 'Entrez un paramètre'
  return
end

@plateau_de_jeu = ["  #{lettre}  ", " #{lettre} #{lettre} ", "#{lettre}   #{lettre}", " #{lettre} #{lettre} ", "  #{lettre}  "]
alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def taille_un_diamant(lettre)
  @plateau_de_jeu.each do |ligne|
    puts ligne
  end
end

taille_un_diamant(lettre)

describe "Diamond kata" do
  it "affiche une pyramide de la lettre passé en paramètre" do
    parametre = ARGV[0]
    resultat_attendu = taille_un_diamant(parametre)
    assert_equal(parametre, resultat_attendu)
  end
end

