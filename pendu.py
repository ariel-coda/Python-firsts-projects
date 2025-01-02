vies = 7
mot = "tapis"
devine = "_"*len(mot)

while vies > 0  and devine != mot:
    letter = input("Entrer une lettre : ")
    if vies == 4:
        print("Voici un indice : ", end=" ")
        print("c'est le cousin de la moquette.")
    if letter in mot:
        for i in range(len(mot)):
            if mot[i] == letter:
                devine = devine[:i] + letter + devine[i+1:]
                print(devine)
    else:
        print("Haha tu as raté", end=" ")
        vies = vies - 1
        print("il te reste", vies, "chances")
        print(devine)
if mot == devine:
    print("Woaaaaouh! tu as trouvé le mot mystère.😎")
elif vies == 0:
    print("Dommage peut-etre une prochaine fois.")
