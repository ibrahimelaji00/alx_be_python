# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Divise numerator par denominator en gérant les erreurs :
    - conversion non numérique
    - division par zéro
    Retourne une chaîne descriptive en cas d'erreur ou le résultat.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    return f"The result of the division is {result}"
