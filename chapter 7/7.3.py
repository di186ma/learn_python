# срезы

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
mid_days = days[2:5] # срез со второго по пятый элементы (исключая последний), отсчет с нуля
print(mid_days)

mid_days = days[:5] # срез с нулевого по пятый элементы (исключая последний)
print(mid_days)

mid_days = days[2:] # срез со второго по последний элементы, отсчет с нуля
print(mid_days)

mid_days = days[:] # просто копия всего списка
print(mid_days)

mid_days = days[1:6:2] # срез с первого по шестой элементы (исключая последний), отсчет с нуля, с шагом 2,
# выбирается каждый второй элемент
print(mid_days)

mid_days = days[-2:] # срез с минус второго (предпоследнего) по последний элементы
print(mid_days)


mid_days = days[-100:100] # в срезах разрешены недопустимые индексы
print(mid_days)

mid_days = days[100:-100] # если начало больше конца, то вернется пустой список
print(mid_days)