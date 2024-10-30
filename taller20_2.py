#Razon de crecimiento
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.2, 3.3, 3.7, 4, 4.2, 4.4, 4.5, 4.7])

# Definir el modelo de crecimiento
def growth_model(x, a, b):
    return a * np.exp(b * x)

# Ajustar el modelo de crecimiento a los datos
params_growth, _ = curve_fit(growth_model, x, y)
a_growth, b_growth = params_growth

# Calcular el ajuste
growth_fit = growth_model(x, a_growth, b_growth)

# Graficar los datos y el ajuste del modelo de crecimiento
plt.scatter(x, y, label='Datos originales', color='black')
plt.plot(x, growth_fit, label=f'Ajuste Crecimiento: y = {a_growth:.2f} * e^({b_growth:.2f} * x)', color='green')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Modelo de Razón de Crecimiento')
plt.show()
