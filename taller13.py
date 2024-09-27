import sympy as sp
xi = 0.4
xi_h = 0.405
x = sp.symbols('x')
funcion = sp.exp(-x)
valor_exacto = funcion.evalf(subs={x: xi_h})
resultados = []
errores = []
for n in range(16):
    serie_taylor = funcion.series(x, xi, n + 1).removeO()
    estimacion = serie_taylor.evalf(subs={x: xi_h})
    error = abs((valor_exacto - estimacion) / valor_exacto) * 100
    resultados.append(estimacion)
    errores.append(error)
for n in range(16):
    print(f"Orden {n}: \tEstimación = {resultados[n]},\t Error aproximado relativo (%) = {errores[n]:.6f}")