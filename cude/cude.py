import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

# ������� ����� ������
fig = plt.figure()

# ��������� ���������� ���
ax = fig.add_subplot(111, projection='3d')

# ������ ��������� ���������� ������ ����
x = np.array([0, 1, 1, 0, 0, 1, 1, 0], dtype=float)
y = np.array([0, 0, 1, 1, 0, 0, 1, 1], dtype=float)
z = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)

# ������ ���
ax.plot(x, y, z)

# ������������� ������� ����
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# ��������� ������ � �������� �������
plt.ion()

try:
    while True:
        # ��������� ��������� �������� � ������ ���������� ����
        x += np.random.uniform(-0.01, 0.01, size=8)
        y += np.random.uniform(-0.01, 0.01, size=8)
        z += np.random.uniform(-0.01, 0.01, size=8)

        # ������� ������� ������
        ax.cla()

        # ������ ��� � ������ ������������
        ax.plot(x, y, z)

        # ������������� ������� ����
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.set_zlim([0, 1])

        # ��������� 
        plt.draw()
        plt.pause(0.01)
except KeyboardInterrupt:
    pass
