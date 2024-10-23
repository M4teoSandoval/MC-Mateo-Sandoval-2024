import numpy as np
import matplotlib.pyplot as plt

# Nuevos datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])

# Inicialización de variables
sumatoriaX = 0
sumatoriaY = 0
xy = 0
xcuadrado = 0

# Sumar X, Y y calcular productos y cuadrados
sumatoriaX = np.sum(x)
sumatoriaY = np.sum(y)
xy = np.sum(x * y)
xcuadrado = np.sum(x ** 2)

# Promedios
promedioX = sumatoriaX / len(x)
promedioY = sumatoriaY / len(y)

# Calcular los coeficientes de regresión lineal
a1 = (len(x) * xy - sumatoriaX * sumatoriaY) / (len(x) * xcuadrado - sumatoriaX ** 2)
a0 = promedioY - a1 * promedioX

# Mostrar los resultados de la regresión lineal
print(f"La ecuación de la línea recta es: y = {a1:.2f}x + {a0:.2f}")

# Calcular la desviación estándar de Y (sy)
st = np.sum((y - promedioY) ** 2)
sy = np.sqrt(st / (len(y) - 1))

# Calcular la suma de los residuos (sr) y el error estándar de la estimación (syx)
sr = np.sum((y - (a1 * x + a0)) ** 2)
syx = np.sqrt(sr / (len(x) - 2))

# Calcular el coeficiente de determinación (r^2) y el coeficiente de correlación (r)
r2 = (st - sr) / st
r = np.sqrt(r2) * 100  # Multiplicar por 100 para convertirlo en porcentaje

# Mostrar los resultados adicionales
print(f"Desviación estándar (sy): {sy:.4f}")
print(f"Error estándar de la estimación (syx): {syx:.4f}")
print(f"Coeficiente de determinación (r^2): {r2:.4f}")
print(f"Coeficiente de correlación (r) en porcentaje: {r:.2f}%")

# Graficar los datos y la línea de ajuste
plt.plot(x, y, 'o', label='Datos originales', markersize=10)
plt.plot(x, a1 * x + a0, 'r', label='Línea de ajuste')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()