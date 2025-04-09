# -*- coding: utf-8 -*-
"""TALLER17_MC

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sjRH-Olea9RRHPU-OTLFAHCURUlJ3l-J
"""

import matplotlib.pyplot as plt


x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1]


n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xx = sum(xi**2 for xi in x)
sum_xy = sum(x[i] * y[i] for i in range(n))


a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
b = (sum_y - a * sum_x) / n

print(f"La recta ajustada es: y = {a:.2f}x + {b:.2f}")


y_pred = [a * xi + b for xi in x]

plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label='Línea ajustada')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()