import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

# Создаем новый график
fig = plt.figure()

# Добавляем трехмерную ось
ax = fig.add_subplot(111, projection='3d')

# Задаем начальные координаты вершин куба
x = np.array([0, 1, 1, 0, 0, 1, 1, 0], dtype=float)
y = np.array([0, 0, 1, 1, 0, 0, 1, 1], dtype=float)
z = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)

# Рисуем куб
ax.plot(x, y, z)

# Устанавливаем пределы осей
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Обновляем график в реальном времени
plt.ion()

try:
    while True:
        # Добавляем случайное значение к каждой координате куба
        x += np.random.uniform(-0.01, 0.01, size=8)
        y += np.random.uniform(-0.01, 0.01, size=8)
        z += np.random.uniform(-0.01, 0.01, size=8)

        # Очищаем текущий график
        ax.cla()

        # Рисуем куб с новыми координатами
        ax.plot(x, y, z)

        # Устанавливаем пределы осей
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.set_zlim([0, 1])

        # Обновляем 
        plt.draw()
        plt.pause(0.01)
except KeyboardInterrupt:
    pass
