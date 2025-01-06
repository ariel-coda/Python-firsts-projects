import random

class personnage:
    def __init__(self,role,nom,HP,DP,ATK):
        self.role = role
        self.nom = nom
        self.HP = HP
        self.DP = DP
        self.ATK = ATK

    def defense(self,attaquant):
        print(f'{self.nom} est en mode défense 🚩 \n')
        for attaque,valeur in attaquant.ATK.items():
            if valeur > self.DP:
                excedent = valeur - self.DP
                self.HP -= excedent
                self.DP = 0
                print(f"Aie! {self.nom} a été touché et perd {excedent} HP. Ripostez maintenant🧨")
            else:
                attaquant.DP -= valeur
                print(f"{attaquant.nom} a été touché sur le bouclier et perd {valeur} DP.")
                print(f"DP restants : {self.DP} et HP restants : {self.HP}.")


    def attaquer(self,cible):
        try:
            print(f"c'est à {self.nom} de jouer ",end = "")
            lancer = int(input("Appuyez 0 pour lancer le dé \n"))
            while lancer != 0:
                lancer = int(input("Appuyez 0 pour lancer le dé \n"))
            if lancer == 0:
                dé = random.randint(1,6)
                print("Le resultat du dé est ",dé) 
                print("-"*40)
            if dé == 1 and self.DP > 0:
                self.defense(cible)
            elif 2 <= dé <= 6:
                attaques_possibles = [atk for atk in self.ATK if self.ATK[atk] <= dé * 100]
                if attaques_possibles:
                    print(f"{self.nom} peut attaquer 🏹. Choisissez une attaque :")
                for i, attaque in enumerate(attaques_possibles, 1):
                    print(f"{i}. {attaque} (Puissance: {self.ATK[attaque]})")
                choix = int(input("Entrez le numéro de votre choix : "))
                attaque_choisie = attaques_possibles[choix - 1]
                cible.HP -= self.ATK[attaque_choisie]
                print(f"{self.nom} utilise {attaque_choisie}! {cible.nom} perd {self.ATK[attaque_choisie]} HP.")
                print(f"{cible.HP} et {self.HP}")
            else:
                print(f"Aucune attaque possible pour {self.nom}.")
                self.defense(cible)
        except:
            print("Vous avez quitté le jeu")


Archer = personnage("archer","Clairmont",1200,500,ATK={"Défense":0,"tir à l'arc":100, "fleches enflammées":400})
Gladiateur = personnage("Gladiateur","Ragnarok",300,500,ATK={"Défense":0,"tir à l'arc":100, "fleches enflammées":400})

while Archer.HP > 0 or Gladiateur.HP > 0: 
    Archer.attaquer(Gladiateur)
    Gladiateur.attaquer(Archer)