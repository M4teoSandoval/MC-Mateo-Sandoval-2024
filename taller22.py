import matplotlib.pyplot as plt



"""# Datos de la tabla
x1 = [0, 2, 2.5, 1, 4, 5]
x2 = [0, 1, 2, 3, 6, 1]
y = [1.2, 2.7, 2.5, 0, 0.8, 6]"""

# Datos de la tabla
x1 = [1, 1, 2, 3, 1, 2, 3, 3]
x2 = [0, 0.5, 0.5, 1, 4.5, 1.5, 1.5, 0.5]
y = [1.2, 4, 0.2, 0.6, 4.5, 4.6, 1.5, -2]

# Número de datos
n = len(y)

# Sumas necesarias para las ecuaciones
sum_x1 = sum(x1)
sum_x2 = sum(x2)
sum_y = sum(y)
sum_x1x1 = sum(xi ** 2 for xi in x1)
sum_x2x2 = sum(xi ** 2 for xi in x2)
sum_x1x2 = sum(x1[i] * x2[i] for i in range(n))
sum_x1y = sum(x1[i] * y[i] for i in range(n))
sum_x2y = sum(x2[i] * y[i] for i in range(n))

# Matriz aumentada para el sistema de ecuaciones
A = [
    [n, sum_x1, sum_x2, sum_y],
    [sum_x1, sum_x1x1, sum_x1x2, sum_x1y],
    [sum_x2, sum_x1x2, sum_x2x2, sum_x2y]
]

# Función de eliminación de Gauss-Jordan
def gauss_jordan(m):
    # Aplicar eliminación Gaussiana
    for i in range(len(m)):
        # Hacer el pivote igual a 1
        pivot = m[i][i]
        for j in range(len(m[i])):
            m[i][j] /= pivot
        
        # Hacer ceros en la columna actual para todas las filas menos la del pivote
        for k in range(len(m)):
            if k != i:
                factor = m[k][i]
                for j in range(len(m[i])):
                    m[k][j] -= factor * m[i][j]
    
    # Los resultados están en la última columna
    return [row[-1] for row in m]

# Resolver el sistema de ecuaciones
result = gauss_jordan(A)

# Valores de los coeficientes
a0, a1, a2 = result

# Mostrar resultados
print("Coeficientes del modelo:")
print("a0 =", a0)
print("a1 =", a1)
print("a2 =", a2)


