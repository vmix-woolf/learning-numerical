import matplotlib.pyplot as plt
import numpy as np


# Вектор v1
v1 = np.array([3, 4])
v2 = np.array([-1, 2])
v3 = np.array([-2, -4])

# Создание новой фигуры
plt.figure(figsize=(12, 8))  # Опционально можно задать размер

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='gray', label='Vec v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Vec v2')
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='violet', label='Vec v3')


# Создание осей (графика)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('axis X')
plt.ylabel('axis Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.grid(color = 'olive', linestyle = '--', linewidth = 0.4)

plt.legend(
    loc='upper left',         # Размещение легенды
    fontsize=9,              # Размер шрифта
    title="Vectors",          # Заголовок легенды
    title_fontsize=10,        # Размер шрифта заголовка
    frameon=True,             # Рамка вокруг легенды
    framealpha=0.7,           # Прозрачность рамки (0 - полностью прозрачная, 1 - непрозрачная)
    edgecolor='gray',         # Цвет границы рамки
    facecolor='fuchsia',   # Цвет фона легенды
    shadow=True               # Добавляем тень
)

# Показать график
plt.show()

# Все названные цвета
colors = plt.colormaps

# Выводим их
print(list(colors.keys()))
