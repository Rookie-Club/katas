require_relative '../roman_to_number'

RSpec.describe "Une fonction de conversion de nombre romain en nombre arabe" do
  it "transforme I en 1 " do
    valeur = 'I'
    valeur_attendue = 1
    resultat = transforme(valeur)
    expect(resultat).to eq(valeur_attendue)
  end

  it "transforme V en 5 " do
    valeur = 'V'
    valeur_attendue = 5
    resultat = transforme(valeur)
    expect(resultat).to eq(valeur_attendue)
  end
end