MAX = 5

total = 0

for count in range(MAX):
    number = int(input("Enter a number: "))
    total += number

print(total)

"""
x += 5 <=> x = x + 5
y -= 2 <=> y = y - 2
z *= 2 <=> z = z * 2
a / b <=> a = a / b
c %= 3 <=> c = c % 3
x /= 3 <=> x = x / 3
y **= 2 <=> y = y ** 2
"""