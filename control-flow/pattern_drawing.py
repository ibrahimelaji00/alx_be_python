# Demander la taille du motif
size = int(input("Enter the size of the pattern: "))

# Initialisation de la ligne
row = 0

# Boucle while pour chaque ligne
while row < size:
    # Boucle for pour afficher chaque étoile sur la ligne
    for col in range(size):
        print("*", end="")
    print()  # Aller à la ligne suivante
    row += 1
