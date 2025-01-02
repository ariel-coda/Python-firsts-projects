note = float(input("Quelle est ta note ?"))

if note >= 12 and note < 14 :
    print("Assez bien")

elif note >= 14 and note < 16 :
    print("Bien")

elif note >= 16 and note < 18 :
    print("Très bien")

elif note >= 18 :
    print("Mes Félicitations du Jury")

else:
    print("Vous pouvez faire mieux avec unpeu plus d'effort")