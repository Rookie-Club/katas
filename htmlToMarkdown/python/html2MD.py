import os


def fintor(balise):
    return balise[0] + "/" + balise[1:]

def extract(html):

    dico_balises = {"<h1>":"# ", "<p>":"", "<h3>": "### "}

    for balise in dico_balises.keys():

        if html.find(balise) > -1:
            position_balise_debut = html.find(balise)
            position_balise_fin = html.find(fintor(balise))
            contenu_balise = dico_balises[balise] +  html[position_balise_debut+len(balise):position_balise_fin]
            return contenu_balise


def lector(filename):
    with open(filename, "r") as fichier:
       return  fichier.readlines()

def ecritor(content):
    if "result.md":
        os.remove("result.md")
    with open("result.md", "a") as fichier:
        for ligne in content:
            if extract(ligne) != None:
                fichier.write(extract(ligne) + "\n")


if __name__ == "__main__":
    ecritor(lector("index.html"))
