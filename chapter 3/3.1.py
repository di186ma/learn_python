from calendar import month

x=0
y=1
print(x<y)
print(x<=y)
print(x==y)

sales = 6000
bonus = 0
if sales > 5000:
    bonus = 500
    print(sales+bonus)

temperature = 6
if temperature < 5:
    print("холодновато")
else:
    print("хорошая погода")

name1 = 'mark'
name2 = 'mary'
if name1 == name2:
    print('Имена одинаковые')
else:
    print('имена разные')

month = 'january'
if month == 'january':
    print('январь')

if 'a' < 'b': # где больше код, тот и больше
    print('a меньше b')
else:
    print('первый вариант неправильный')

if 'aaa' < 'aab': # сравниваются буквы поочередно
    print('a меньше b')
else:
    print('второй вариант неправильный')

if 'aaa' < 'aa': # важна длина, отсутствие буквы значит меньше
    print('a меньше b')
else:
    print('третий вариант неправильный')

name3 = 'Коста'
name4 = 'Джонс'

if name3 < name4:
    print(name3, name4)
else:
    print(name4, name3)


MIN_SALARY = 30000
MIN_YEARS = 2
salary = int(input('Введите Ваш годовой доход: '))
years_on_job = int(input("Сколько лет Вы работали на этом месте? "))
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print("Ваша ссуда одобрена")
    else:
        print(f"Вы должны отработать не менее {MIN_YEARS} лет")
else:
    print(f"Вы должны зарабатывать не менее {MIN_SALARY}")


A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

score = int(input('Введите ваши баллы: '))
if score >= A_SCORE:
    print("У Вас оценка: A")
elif score >= B_SCORE:
    print("У Вас оценка: B")
elif score >= C_SCORE:
    print("У Вас оценка: C")
elif score >= D_SCORE:
    print("У Вас оценка: D")
else:
    print("У Вас оценка: F")

mark = 5
gap = 3
if mark <= 5 and gap <= 5:
    print('right')

if mark < 6 or mark > 10:
    print('right')

if not(mark < 4):
    print('right')

if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print("Ваша ссуда одобрена")
else:
    print("Ваша ссуда не одобрена")

num = 30
if num > 20 and num < 40:
    print('good')

sales = 300
if sales > 200:
    sales_quota_met = True
else:
    sales_quota_met = False

if sales_quota_met:
    print('you are good')