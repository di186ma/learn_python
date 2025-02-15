print()

'''-123875655698498 int
-167867.578768768 float
"fgгшап . 578648 ?*&&^_=341`" str
'fgгшап . 578648 ?*&&^_=341`' str
True False bool'''

print('''Hello,
"world!"''')    # это вывод в две строки
print('"Hello, world!"') # вывод с кавычками

'''Важное примечание! Переменная ссылается на ячейку со значением'''
age = 23
print('мне', age, 'года') # разделитель пробел

age = 25

print(type(age))
print(type(age+0.5))

name = 'dima'
print(name)
print(type(name))

x = 'hi'
print(type(x))
print(x)
x = 5
print(type(x))
print(x)

# name2 = str(input('Введите ваше имя: '))
# print(type(name2))
# print(name2)

salary = 20000
bonus = 10
sum = salary + \
      bonus # перевод строки

print(sum)
print(sum/bonus) # число с плавающей точкой (при отрицательном значении округляется в большую сторону по модулю),
                 # в положительных числах просто отбрасывается дробная часть
print(sum//bonus) # целое число
print(sum**bonus) # возведение в степень
print(sum%bonus) # остаток от деления

summury = 1000
new_summury = summury - (summury / 100 * 20) + 10000000
print(new_summury)

print('Hello' + " world!") # явная конкатенация строк
print('Hello' +
      ' world!') # явная конкатенация строк с разделением на строки

my_str = 'one' 'two' 'three' # неявная конкатенация без разделения

print(my_str, end='!!!!!\n')
print('Hello'
      ' world!') # неявная конкатенация без разделения и перевода каретки

print('one', 'two', 'three', sep='*') # неявная конкатенация с разделением *
print('one\ntwo\nthree') # с переводом каретки
print('one\t\ttwo\t\tthree') # с табуляцией
print('one\\two\\three') # с обратной чертой
print('one\'two\'three') # с апострофом
print('one\"two\"three') # с двойными кавычками

print(f'hello, world!') # f-строка или отформатированный строковый литерал

print(f'hello {name}') # использование место-заполнителей
print(f'hello {'дорогой ' + name}')

print(f'{new_summury / 2 :,.2f}')
print(f'{0.656:%}')
print(f'{0.656:.0%}')
print(f'{0.656:.2e}')
print(f'{1473:,d}')
print(f'{1473:,}')
print(f'{1473:10}')
print(f'{14738743654375463:10}')
print(f'{1473874365589435786.4375463:40,.2f}{1473874365589435786.4375463:40,.2f}')
print(f'hello {name:10} дорогой')
print(f'{1473:<10}')
print(f'{1473:^10}')
print(f'{1473:>10}')

print(f'привет {name}' +
      f'\nпока {name}')
print(f'привет {name}'
      f'\nпока {name}')

# порядок следования условных обозначений
# [:][выравнивание][ширина (количество места)][разделитель][точность][тип]
# [:][<^>][1-99][,][.nf][d/f]
# [:][слева, по центру, справа][пиксели][разделитель - ','][n - количество знаков после точки и f][целое или вещественное]

IMPORTAL_IN = 4.54 # именованная константа
