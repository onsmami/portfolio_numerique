notes = []
nombre = int(input("Combien de notes voulez-vous saisir ? "))
for i in range(nombre):
    note = float(input("Entrez la note : "))
    notes.append(note)
moyenne = sum(notes) / nombre
print("Les notes sont :", notes)
print("La moyenne est :", moyenne)
