#Wilson Andres Suarez Mantilla - Keiner Mateo Sandoval Barreto

import numpy as np
import scipy.stats as stats
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funciones de regresión
def linear_regression(x, y):
    slope, intercept, r_value, _, std_err = stats.linregress(x, y)
    function_str = f"y = {slope:.4f}x + {intercept:.4f}"
    return (lambda x: slope * x + intercept), slope, intercept, r_value ** 2, std_err, function_str

def exponential_regression(x, y):
    x, y = np.array(x), np.array(y)
    y_log = np.log(y)
    slope, intercept, r_value, _, std_err = stats.linregress(x, y_log)
    function_str = f"y = {np.exp(intercept):.4f} * e^({slope:.4f}x)"
    return (lambda x: np.exp(intercept) * np.exp(slope * x)), np.exp(intercept), slope, r_value ** 2, std_err, function_str

def power_regression(x, y):
    x, y = np.array(x), np.array(y)
    x_log = np.log(x)
    y_log = np.log(y)
    slope, intercept, r_value, _, std_err = stats.linregress(x_log, y_log)
    function_str = f"y = {np.exp(intercept):.4f} * x^{slope:.4f}"
    return (lambda x: np.exp(intercept) * x ** slope), np.exp(intercept), slope, r_value ** 2, std_err, function_str

def growth_rate_regression(x, y):
    x, y = np.array(x), np.array(y)
    growth_rate = (y[1:] - y[:-1]) / y[:-1]
    avg_growth_rate = np.mean(growth_rate)
    function_str = f"y = {y[0]:.4f} * (1 + {avg_growth_rate:.4f})^t"
    return (lambda t: y[0] * (1 + avg_growth_rate) ** t), avg_growth_rate, function_str

def polynomial_regression(x, y):
    coeffs = np.polyfit(x, y, 2)
    r_value = np.corrcoef(y, np.polyval(coeffs, x))[0, 1] ** 2
    function_str = f"y = {coeffs[0]:.4f}x² + {coeffs[1]:.4f}x + {coeffs[2]:.4f}"
    return (lambda x: coeffs[0] * x ** 2 + coeffs[1] * x + coeffs[2]), coeffs, r_value, function_str

def calculate_standard_deviation(y, y_pred):
    return np.sqrt(np.mean((y - y_pred) ** 2))

# Interfaz gráfica mejorada
class RegressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Regresiones por Mínimos Cuadrados")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")
        
        # Crear barra de navegación
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)
        
        # Crear pestañas
        self.points_tab = tk.Frame(self.notebook, bg="#f0f0f0")
        self.results_tab = tk.Frame(self.notebook, bg="#f0f0f0")
        self.notebook.add(self.points_tab, text="Ingresar Puntos")
        self.notebook.add(self.results_tab, text="Resultados")
        
        # Contenido de la pestaña "Ingresar Puntos"
        points_frame = tk.LabelFrame(self.points_tab, text="Número de Puntos", padx=10, pady=10, bg="#4CAF50", fg="white", font=("Arial", 12))
        points_frame.pack(pady=10, fill="x")
        
        tk.Label(points_frame, text="Ingrese el número de puntos (mínimo 5):", bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side="left")
        self.num_points_entry = tk.Entry(points_frame, width=5, font=("Arial", 12))
        self.num_points_entry.pack(side="left", padx=5)
        tk.Button(points_frame, text="Confirmar", command=self.confirm_points, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side="left", padx=5)
        
        self.entry_frame = tk.Frame(self.points_tab, bg="#f0f0f0")
        self.entry_frame.pack(pady=10, fill="x")
    
    def confirm_points(self):
        try:
            num_points = int(self.num_points_entry.get())
            if num_points < 5:
                raise ValueError("El número de puntos debe ser al menos 5.")
            self.create_point_entries(num_points)
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
    
    def create_point_entries(self, num_points):
        for widget in self.entry_frame.winfo_children():
            widget.destroy()
        
        self.entries = []
        
        tk.Label(self.entry_frame, text="Ingrese los puntos (x, y):", bg="#f0f0f0", font=("Arial", 12)).pack()
        
        for i in range(num_points):
            frame = tk.Frame(self.entry_frame, bg="#f0f0f0")
            frame.pack(pady=2)
            tk.Label(frame, text=f"Punto {i+1} - x:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0)
            entry_x = tk.Entry(frame, width=8, font=("Arial", 12))
            entry_x.grid(row=0, column=1, padx=5)
            tk.Label(frame, text="y:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=2)
            entry_y = tk.Entry(frame, width=8, font=("Arial", 12))
            entry_y.grid(row=0, column=3, padx=5)
            self.entries.append((entry_x, entry_y))
        
        tk.Button(self.entry_frame, text="Calcular Regresiones", command=self.calculate_regressions, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)
    
    def calculate_regressions(self):
        try:
            points = [(float(e[0].get()), float(e[1].get())) for e in self.entries if e[0].get() and e[1].get()]
            if len(points) < 5:
                raise ValueError("Debe ingresar al menos 5 puntos.")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
            return
        
        x, y = zip(*points)
        
        # Crear un Canvas con Scrollbar en la pestaña de resultados
        canvas = tk.Canvas(self.results_tab)
        scrollbar = tk.Scrollbar(self.results_tab, orient="vertical", command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)
        
        results_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=results_frame, anchor="nw")
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        regressions = {
            "Lineal": linear_regression,
            "Exponencial": exponential_regression,
            "Potencias": power_regression,
            "Razón de Crecimiento": growth_rate_regression,
            "Polinomial grado 2": polynomial_regression
        }
        
        for name, func in regressions.items():
            result_frame = tk.LabelFrame(results_frame, text=f"Regresión {name}", padx=10, pady=5, bg="#e0f7fa", fg="black", font=("Arial", 12))
            result_frame.pack(fill="x", pady=5)
            
            model, *params = func(x, y)
            y_pred = [model(xi) for xi in x]
            std_dev = calculate_standard_deviation(np.array(y), np.array(y_pred))
            
            tk.Label(result_frame, text=f"Función obtenida: {params[-1]}", bg="#e0f7fa", font=("Arial", 10)).pack(anchor="w")
            tk.Label(result_frame, text=f"Desviación estándar: {std_dev:.4f}", bg="#e0f7fa", font=("Arial", 10)).pack(anchor="w")
            
            # Mostrar R² de forma segura
            r_squared = params[-3] if len(params) > 3 else "N/A"
            tk.Label(result_frame, text=f"Coeficiente de determinación (r²): {r_squared:.4f}" if r_squared != "N/A" else "Coeficiente de determinación (r²): N/A", bg="#e0f7fa", font=("Arial", 10)).pack(anchor="w")
            
            tk.Button(result_frame, text="Mostrar Gráfica", command=lambda m=model, n=name: self.create_plot_window(x, y, [m(xi) for xi in x], n), bg="#4CAF50", fg="white", font=("Arial", 10)).pack(anchor="w", pady=5)
        
        # Actualizar el área de resultados para que se ajuste al tamaño del contenido
        results_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
    def create_plot_window(self, x, y, y_pred, title):
        plot_window = tk.Toplevel(self.root)
        plot_window.title(f"Gráfica de la Regresión {title}")
        
        fig, ax = plt.subplots()
        ax.scatter(x, y, color='blue', label='Puntos originales')
        ax.plot(x, y_pred, color='red', label='Ajuste de la regresión')
        
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(f"Gráfica de la Regresión {title}")
        ax.legend()
        
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

# Crear la ventana principal
root = tk.Tk()
app = RegressionApp(root)
root.mainloop()
