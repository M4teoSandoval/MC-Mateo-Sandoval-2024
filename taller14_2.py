matriz1 = []
matriz2 = []
resultadoA = []
resultadoB = []
resultadoC = []
resultadoD = []

filas1 = int(input("Ingrese el numero de filas de la matriz 1 >>> "))
columnas1 = int(input("Ingrese el numero de columnas de la matriz 1 >>> "))
print()
for i in range(filas1):
    fila = []
    filaA = []
    for j in range(columnas1):
        numero = int(input(f"Ingrese el valor de la fila {i+1} y columna {j+1} de la matriz 1 >>> "))
        operacionA = 2 * numero
        fila.append(numero)
        filaA.append(operacionA)
    matriz1.append(fila)
    resultadoA.append(filaA)

print("Matriz A creada: ", matriz1)
print()


filas2 = int(input("Ingrese el numero de filas de la matriz 2 >>> "))
columnas2 = int(input("Ingrese el numero de columnas de la matriz 2 >>> "))
print()
for i in range(filas2):
    fila = []
    filaB = []
    for j in range(columnas2):
        numero = int(input(f"Ingrese el valor de la fila {i+1} y columna {j+1} de la matriz 2 >>> "))
        operacionB = 3 * numero
        fila.append(numero)
        filaB.append(operacionB)
    matriz2.append(fila)
    resultadoB.append(filaB)

print("Matriz B creada: ", matriz2)
print()
print("**** RESULTADOS OPERACIONES ****")
print()

print(f"- 2A: {resultadoA}")
print()
print(f"- 3B: {resultadoB}")
print()


if filas1 == filas2 and columnas1 == columnas2:
    for i in range(filas1):
        filaC = []
        for j in range(columnas1):
            operacionC = matriz1[i][j] + matriz2[i][j]
            filaC.append(operacionC)
        resultadoC.append(filaC)
    print(f"- A + B: {resultadoC}")
else:
    print(f"- A + B: No se puede realizar ya que la matriz A y B tienen diferentes tamaños.")


print()
if columnas1 == filas2:  
    for i in range(filas1):
        filaD = []
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1): 
                suma += matriz1[i][k] * matriz2[k][j]
            filaD.append(suma)
        resultadoD.append(filaD)
    print(f"- A x B: {resultadoD}")
else:
    print(f"- A x B: No se puede realizar ya que el número de columnas de A no coincide con el número de filas de B.")
