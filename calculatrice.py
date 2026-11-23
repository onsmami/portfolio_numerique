a = float(input("Entrez le premier nombre : "))
op = input("Choisissez une opération (+, -, *, /) : ")
b = float(input("Entrez le deuxième nombre : "))

if op == "+":
    resultat = a + b
elif op == "-":
    resultat = a - b
elif op == "*":
    resultat = a * b
elif op == "/":
    if b != 0:
        resultat = a / b
    else:
        print("Erreur : division par zéro impossible")
        resultat = None
else:
    print("Opération invalide")
    resultat = None

if resultat is not None:
    print("Résultat :", resultat)
