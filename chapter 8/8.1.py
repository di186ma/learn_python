# Строковые операции
# Строка это немутируемая последовательность
# При попытке изменения строки (например конкатенации) переменная просто теперь будет ссылаться на другое значение

name = 'Julian'
for ch in name: # обход строкового значений
    print(ch)
    ch = 'x' # не влияет на слово
print(name)


count = 0
my_string = input('Enter a string: ')
for ch in my_string:
    if ch == 'T' or ch =='t':
        count += 1
print("Number of times 'T' appears: ", count)


my_str = 'Ромашки белые'
ch2 = my_str[6] # возвращает копию символа из слова, изменения символа не влияют на слово
ch3 = my_str[-2]
print(ch2, ch3)

city = 'Boston'
# print(city[6]) # вызовет исключение IndexError
size = len(city)
print(size)

letters = 'abc'
letters += 'def' # конкатенация строк, обязательно прочитать заголовок
print(letters)

# letters[0] = 'h' # вызовет ошибку, обязательно прочитать заголовок