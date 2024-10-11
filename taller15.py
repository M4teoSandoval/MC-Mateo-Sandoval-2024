import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)
    n = len(b)
    
    imprimirSistema(a, b, "Matriz inicial")
    
    for i in range(n):
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    print(f"Intercambio de fila {i+1} con fila {k+1}")
                    imprimirSistema(a, b, "Después del intercambio")
                    break
            else:
                raise ValueError(f"No se puede resolver el sistema, pivote cero en la columna {i+1}.")

        pivote = a[i][i]
        
        # Dividir la fila por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        # Reducción
        for k in range(n):
            if i != k:
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

a = [[1, 1, 0], [3, 3, 4], [4, 1, 0]]
b = [2.5, 11.5, 15]
x = gaussJordan(a, b)

print("Respuesta:")
for i in range(len(x)):
    print("x" + str(i+1), "=", x[i])

# Pruebas 
print("\nPruebas:")
ao = [[1, 1, 0], [3, 3, 4], [4, 1, 0]]
bo = [2.5, 11.5, 15]
for i in range(len(bo)):
    valorAux = bo[i]
    for j in range(len(bo)):
        valorAux -= ao[i][j] * x[j]
    print("Test", i + 1, "=", valorAux)
