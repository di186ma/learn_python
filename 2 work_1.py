price = float(input("Введите сумму покупки: "))

federal = price * 0.05
regional = price * 0.025
print(f"Налоги: {federal + regional:.2f}")

