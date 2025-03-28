import numpy as np
import tkinter as tk
from tkinter import messagebox

def swap_rows(mat, vec, row1, row2):
    """Intercambia dos filas en una matriz y un vector."""
    mat[[row1, row2]] = mat[[row2, row1]]
    vec[[row1, row2]] = vec[[row2, row1]]

def gauss_jordan(a, b):
    """Resuelve un sistema de ecuaciones usando eliminación de Gauss-Jordan."""
    n = len(b)
    a = a.astype(float)
    b = b.astype(float)
    
    for i in range(n):
        if a[i, i] == 0:
            for j in range(i + 1, n):
                if a[j, i] != 0:
                    swap_rows(a, b, i, j)
                    break
        
        pivot = a[i, i]
        if pivot == 0:
            raise ValueError("El sistema no tiene solución única.")
        
        a[i] /= pivot
        b[i] /= pivot
        
        for j in range(n):
            if i != j:
                factor = a[j, i]
                a[j] -= factor * a[i]
                b[j] -= factor * b[i]
    
    return b

def resolver_sistema():
    a = np.array([[2, 0, 2],
                  [4, 0, -1],
                  [3, 2, -2]], dtype=float)

    b = np.array([7, 18, 16], dtype=float)
    
    try:
        solucion = gauss_jordan(a, b)
        resultado = f"Solución del sistema:\n x1 = {solucion[0]:.2f}\n x2 = {solucion[1]:.2f}\n x3 = {solucion[2]:.2f}"
    except ValueError as e:
        resultado = str(e)
    
    messagebox.showinfo("Resultado", resultado)


root = tk.Tk()
root.title("Resolución de Sistema de Ecuaciones")

tk.Label(root, text="Sistema de ecuaciones:", font=("Arial", 14)).pack()
tk.Label(root, text="2x1 + 2x3 = 7\n4x1 - x3 = 18\n3x1 + 2x2 - 2x3 = 16", font=("Arial", 12)).pack()

tk.Button(root, text="Resolver", command=resolver_sistema).pack()

root.mainloop()
