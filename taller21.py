import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos de la tabla
x = np.array([1, 3, 5, 7, 9, 11, 13])
y = np.array([14.9, 3.6, -2, -3.6, -2.4, 4.4, 14.4])

# Ajuste del polinomio de segundo grado
coefficients = np.polyfit(x, y, 2)
polynomial = np.poly1d(coefficients)

# Valores ajustados
y_fit = polynomial(x)

# Cálculo del coeficiente de correlación (r)
r_value = np.corrcoef(y, y_fit)[0, 1]

# Mostrar resultados
print("Coeficientes del polinomio ajustado: ")
print("a =", coefficients[0])
print("b =", coefficients[1])
print("c =", coefficients[2])
print("Coeficiente de correlación (r):", r_value)

# Gráfica
plt.scatter(x, y, label='Datos originales', color='green')
plt.plot(x, y_fit, label='Ajuste cuadrático', color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste de polinomio cuadrático')
plt.legend()
plt.show()
