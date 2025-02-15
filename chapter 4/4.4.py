# Условие выполнения
weight = int(input("Enter your weight: "))
total = 0
while weight != 0:
    total += weight
    weight = int(input("Enter your weight or 0 for end: "))

print(total)