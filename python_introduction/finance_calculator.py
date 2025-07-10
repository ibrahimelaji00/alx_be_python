# Demande des revenus et dépenses mensuels
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calcul des économies mensuelles
monthly_savings = income - expenses

# Calcul des économies annuelles et de l’intérêt
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Affichage des étapes intermédiaires
print(f"\nYour monthly savings are ${monthly_savings}.")
print(f"Annual savings without interest: ${annual_savings}")
print(f"Interest earned at 5%: ${interest}")
print(f"Projected savings after one year, with interest: ${projected_savings}")
