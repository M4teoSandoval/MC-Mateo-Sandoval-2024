import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7,8])
y = np.array([15, 11, 13, 7, 9, 6, 5,2])

# Cálculo de los coeficientes de la regresión lineal
sumatoriaX = 0
sumatoriaY = 0
xy = 0
xcuadrado = 0

for i in x:
    sumatoriaX+=i
    xcuadrado += i*i
promedioX =sumatoriaX/len(x)
for i in y:
    sumatoriaY += i
promedioY=sumatoriaY/len(y)
for i in range(len(x)):
    xy += x[i]*y[i]


a1 = (len(x)*xy-sumatoriaX*sumatoriaY)/(len(x)*xcuadrado-sumatoriaX*sumatoriaX)
a0 = promedioY-a1*promedioX 
print(sumatoriaX,sumatoriaY,xy,xcuadrado)
print(a1)
print(a0)

    



# Mostrar los resultados
print(f"La ecuación de la línea recta es: y = {a1:.2f}x + {a0:.2f}")

# Graficar los datos y la línea de ajuste
plt.plot(x, y, 'o', label='Datos originales', markersize=10)
plt.plot(x, a1*x + a0, 'r', label='Línea de ajuste')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()
