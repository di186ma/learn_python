# кортеж - это неизменяемый список
# Преимущества кортежа:
# - обработка кортежа происходит быстрее
# - можно использовать как константы
# - некоторые функции требуют именно кортеж, а не список

my_tuple = (1,2,3,4,5) # кортеж заключается в круглые скобки
print(my_tuple)

for item in my_tuple:
    print(item)

for i in range(len(my_tuple)):
    print(my_tuple[i])

value = (1) # создает целочисленное значение
value2 = (1,) # кортеж с одним элементом

print(value)
print(value2)

number_tuple = (1,2,3,4,5)
number_list = list(number_tuple) # преобразует кортеж в список
print(number_list)

str_list = ['a','b','c','d','e','f']
str_tuple = tuple(str_list)
print(str_tuple)