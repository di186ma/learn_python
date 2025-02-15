# Валидация данных
score = int(input("Enter your score: "))
while score < 0 or score > 5:
    score = int(input("Enter your score: "))

print("Your score is:", score)