# Demande des revenus et dépenses mensuels
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calcul des économies mensuelles
monthly_savings = income - expenses

# Calcul des économies annuelles avec intérêt (5%)
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Affichage des résultats
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
