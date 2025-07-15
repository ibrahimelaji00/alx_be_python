# Demande à l'utilisateur de saisir deux nombres
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Demande le type d'opération
operation = input("Choose the operation (+, -, *, /): ")

# Match-case pour exécuter l'opération choisie
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")
