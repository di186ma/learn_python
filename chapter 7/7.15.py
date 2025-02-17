# круговые диаграммы

import matplotlib.pyplot  as plt # импортирование модуля для создания графиков и его сокращение до plt

values = [20, 60, 80, 40] # список значений
slice_labels = ['20', '60', '80', '40'] # список меток долей

plt.title("Круговая диаграмма")

# вычисляет каждое значение как процентное соотношений от общей суммы, выводит метки (labels) и окрашивает доли (colors)
plt.pie(values, labels=slice_labels, colors=('r', 'g', 'b', 'm'))

plt.show() # выводит созданный график