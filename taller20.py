#Ecuacion de potencias
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.2, 3.3, 3.7, 4, 4.2, 4.4, 4.5, 4.7])

# Definir el modelo de potencia
def power_model(x, a, b):
    return a * np.power(x, b)

# Ajustar el modelo de potencia a los datos
params_power, _ = curve_fit(power_model, x, y)
a_power, b_power = params_power

# Calcular el ajuste
power_fit = power_model(x, a_power, b_power)

# Graficar los datos y el ajuste del modelo de potencia
plt.scatter(x, y, label='Datos originales', color='black')
plt.plot(x, power_fit, label=f'Ajuste Potencia: y = {a_power:.2f} * x^{b_power:.2f}', color='green')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Modelo de Ecuación de Potencias')
plt.show()
