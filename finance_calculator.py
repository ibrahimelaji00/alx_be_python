# Demande des revenus et dépenses mensuels
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calcul des économies mensuelles
monthly_savings = income - expenses

# Projection des économies annuelles avec intérêt en une seule ligne
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Affichage du résultat
print(f"\nYour monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
