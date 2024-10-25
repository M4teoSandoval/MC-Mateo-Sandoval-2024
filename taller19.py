import math
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]
y = [0.8, 1.2, 1.7, 2.2, 3.2, 4.5]

ln_y = [math.log(value) for value in y]

mean_x = sum(x) / len(x)
mean_ln_y = sum(ln_y) / len(ln_y)

numerador = sum((xi - mean_x) * (ln_y[i] - mean_ln_y) for i, xi in enumerate(x))
denominador = sum((xi - mean_x) ** 2 for xi in x)
b = numerador / denominador

a = math.exp(mean_ln_y - b * mean_x)

y_adjusted = [a * math.exp(b * xi) for xi in x]
ss_total = sum((yi - mean_ln_y) ** 2 for yi in ln_y)
ss_residual = sum((math.log(yi) - math.log(y_adj)) ** 2 for yi, y_adj in zip(y, y_adjusted))
r_squared = 1 - (ss_residual / ss_total)

print(f"Modelo: y = {a:.4f} * e^({b:.4f} * x)")
print(f"R^2: {r_squared:.4f}")

for xi, yi, y_adj in zip(x, y, y_adjusted):
    print(f"x = {xi}, y = {yi}, y ajustado = {y_adj:.4f}")

x_fit = [i / 10 for i in range(10, 61)] 
y_fit = [a * math.exp(b * value) for value in x_fit]


plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x_fit, y_fit, color='red', label='Modelo ajustado')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste de modelo exponencial')
plt.legend()
plt.grid()
plt.show()
