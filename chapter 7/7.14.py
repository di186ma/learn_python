# гистограммы

import matplotlib.pyplot  as plt # импортирование модуля для создания графиков и его сокращение до plt

left_edges = [0, 10, 20, 30, 40] # устанавливаем координаты X для левого нижнего угла столбика

heights = [100, 200, 300, 400, 500] # устанавливаем высоту столбика по Y

bar_width = 5 # устанавливаем ширину столбика

"""
Цветовые коды для гистограммы
'b' - синий
'g' - зеленый
'r' - красный
'c' - голубой
'm' - сиреневый
'y' - желтый
'k' - черный
'w' - белый
"""

plt.title("bar chart")

plt.xlabel("left")
plt.ylabel("height")

plt.xticks([5, 10, 15], ['five', 'ten', 'fifty'])
plt.yticks([50, 100, 150], ['половина handreed', 'one handreed', 'полторы handreed'])

# создает гистограмму в оперативной памяти с нужной шириной и цветом для каждого столбика
plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))
plt.show() # выводит созданный график