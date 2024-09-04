import math
x=float(input("Ingrese el valor de x (En radianes) <<< "))
sumadorNumero = 0
errorEsperado = (0.5 * 10**-8)*100
errorAprox = 100
contador= 0
potencia=0
puerta = True
while errorAprox >= errorEsperado:
    anterior = sumadorNumero
    operacion= x**potencia/math.factorial(potencia)
    if puerta:
        sumadorNumero += operacion
    else:
        sumadorNumero -= operacion            
    errorAprox = abs(((sumadorNumero - anterior)/sumadorNumero))*100
    contador += 1
    potencia +=2
    puerta = not puerta
print(f"Cos({x}): {sumadorNumero}\nError aproximado: {errorAprox}\nIteraciones: {contador}")
    

