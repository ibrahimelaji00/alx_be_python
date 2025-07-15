# Demander un nombre à l'utilisateur
number = int(input("Enter a number to see its multiplication table: "))

# Afficher la table de multiplication de 1 à 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
