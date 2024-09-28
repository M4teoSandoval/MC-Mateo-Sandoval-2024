import math
import tkinter as tk
from tkinter import messagebox


def factorial(n):
    return math.prod(range(1, n + 1)) if n > 0 else 1


def sen_maclaurin(x, terms=20):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n
        sine += sign * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return round(sine, 8)

def cos_maclaurin(x, terms=20):
    cosine = 0
    for n in range(terms):
        sign = (-1) ** n
        cosine += sign * (x ** (2 * n)) / factorial(2 * n)
    return round(cosine, 8)


def tan_maclaurin(x, terms=20):
    try:
        return round(sen_maclaurin(x, terms) / cos_maclaurin(x, terms), 8)
    except ZeroDivisionError:
        return "Error"

def cot_maclaurin(x, terms=20):
    try:
        return round(1 / tan_maclaurin(x, terms), 8)
    except ZeroDivisionError:
        return "Error"

def sec_maclaurin(x, terms=20):
    try:
        return round(1 / cos_maclaurin(x, terms), 8)
    except ZeroDivisionError:
        return "Error"

def csc_maclaurin(x, terms=20):
    try:
        return round(1 / sen_maclaurin(x, terms), 8)
    except ZeroDivisionError:
        return "Error"

def parse_expression(expression):
    try:

        result = eval(expression, {"sen": sen_maclaurin, "cos": cos_maclaurin, 
                                   "tan": tan_maclaurin, "cot": cot_maclaurin, 
                                   "sec": sec_maclaurin, "csc": csc_maclaurin, "math": math})
        return result
    except Exception as e:
        return f"Error: {e}"

def reemplazar_comas(expresion):
    return expresion.replace(',', '.')

def calcular():
    expresion = entrada.get()
    expresion = reemplazar_comas(expresion) 
    resultado = parse_expression(expresion)
    if "Error" in str(resultado):
        messagebox.showerror("Error", resultado)
    else:
        salida.config(text=f"Resultado: {resultado}")

ventana = tk.Tk()
ventana.title("Calculadora Trigonométrica")
ventana.configure(bg="lightblue")  

tk.Label(ventana, text="CALCULADORA", 
         bg="lightblue", fg="darkgreen", font=("Arial", 14,"bold")).pack(pady=9)  


tk.Label(ventana, text="Ingrese la expresión trigonométrica (En radianes):", 
         bg="lightblue", fg="black", font=("Arial", 12)).pack(pady=1)  

entrada = tk.Entry(ventana, bg="white", fg="black", font=("Arial", 12))
entrada.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular, 
          bg="green", fg="white", font=("Arial", 12), activebackground="darkgreen", activeforeground="white").pack(pady=10)

salida = tk.Label(ventana, text="Resultado: ", bg="lightblue", fg="darkgreen", font=("Arial", 12, "bold"))
salida.pack(pady=10)


ventana.mainloop()
