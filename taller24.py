def multiplicar(a, b):
    longitud = len(a) + len(b) - 1
    resultado = [0] * longitud
    for i in range(len(a)):
        for j in range(len(b)):
            resultado[i + j] += a[i] * b[j]
    return resultado

def lagrange(x, y):
    n = len(x)
    polinomio = [0] * n  # Inicializamos el polinomio en cero
    for i in range(n):
        term = [1]
        for j in range(n):
            if i != j:
                # L_i(x) = (x - x_j) / (x_i - x_j)
                term = multiplicar(term, [-x[j] / (x[i] - x[j]), 1 / (x[i] - x[j])])
        term = [coef * y[i] for coef in term]  # Multiplicamos L_i por f(x_i)
        for k in range(len(term)):
            if k < len(polinomio):
                polinomio[k] += term[k]
            else:
                polinomio.append(term[k])
    return polinomio

def main():
    x = [0, 1, 2, 3, 4]
    y = [1, 0.9, -1, -2.3, 1.8]
    polinomio = lagrange(x, y)
    print("Polinomio de interpolación de Lagrange:", polinomio)
    print(f"Ecuacion: {polinomio[4]}x^4 + {polinomio[3]}x^3 + {polinomio[2]}x^2 + {polinomio[1]}x + {polinomio[0]} ")

main()