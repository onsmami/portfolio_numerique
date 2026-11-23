nombre_secret = 7
essai = int(input("Devinez le nombre entre 1 et 10 : "))
while essai != nombre_secret:
    if essai < nombre_secret:
        print("Le nombre est plus grand !")
    else:
        print("Le nombre est plus petit !")
    essai = int(input("Essayez encore : "))
print("Bravo ! Vous avez trouvé le nombre !")
