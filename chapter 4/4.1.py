"""
Цикл while
Выполняется пока условие истинно
Алгоритм работы:
1. Проверяет условие
2. Если условие истинно, то переходит в тело цикла. Если условие ложно, то тело цикла пропускается
3. После выполнения цикла опять проверяет условие
"""

keep_going = 'да'

while keep_going == 'да':
    sales = float(input('Введите объем продаж: '))
    comm_rate = float(input('Введите ставку комиссионных: '))

    commission = sales * comm_rate

    print(f"Комиссионное вознаграждение составляет: {commission:,.2f}")
    keep_going = input('Если хотите вычислить еще одно - напишите да: ')