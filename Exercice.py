class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = int(pages)

    def Afficher(self):
        print("Nom du livre : ", self.titre, "\n Ecrit par : ", self.auteur, "\n nombre de pages : ", self.pages)

    def Verifier(self):
        volume = "Trop volumineux" if self.pages >= 300 else "Pas volumineux"
        print(volume)

    def Changer(self):
        change = input("Voulez-vous changer le nombre de pages ?")

        try:

            if change == "oui" or change == "yes" :
                nbre = int(input("Entrez le nouveau nombre de page "))
                self.pages = nbre
                self.Afficher()
        
        except(ValueError):
            print("Veuillez entrer un entier valide.")


Kirikou = Livre("Kirikou et la sorcière", "Michel Ocelot", 300)

Kirikou.Afficher()
Kirikou.Changer()
Kirikou.Verifier()