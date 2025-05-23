import tkinter as tk
from tkinter import messagebox
import random

# Definición del nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Clase del Árbol Binario de Búsqueda
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregarValor(self, valor):
        self.raiz = self._agregarRecursivo(self.raiz, valor)

    def _agregarRecursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._agregarRecursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._agregarRecursivo(nodo.derecho, valor)
        return nodo

    def buscarValor(self, valor):
        return self._buscarRecursivo(self.raiz, valor)

    def _buscarRecursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscarRecursivo(nodo.izquierdo, valor)
        else:
            return self._buscarRecursivo(nodo.derecho, valor)

    def imprimirValores(self):
        valores = []
        self._inOrden(self.raiz, valores)
        return valores

    def _inOrden(self, nodo, valores):
        if nodo:
            self._inOrden(nodo.izquierdo, valores)
            valores.append(nodo.valor)
            self._inOrden(nodo.derecho, valores)

# Interfaz Gráfica
class Aplicacion:
    def __init__(self, root):
        self.arbol = ArbolBinario()
        self.numeros = random.sample(range(1, 101), 20)
        for num in self.numeros:
            self.arbol.agregarValor(num)

        self.root = root
        self.root.title("Árbol Binario de Búsqueda")

        self.label = tk.Label(root, text="Ingrese número a buscar:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.btn_buscar = tk.Button(root, text="Buscar", command=self.buscar)
        self.btn_buscar.pack()

        self.btn_imprimir = tk.Button(root, text="Imprimir en orden", command=self.imprimir)
        self.btn_imprimir.pack()

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()

    def buscar(self):
        try:
            valor = int(self.entry.get())
            encontrado = self.arbol.buscarValor(valor)
            if encontrado:
                messagebox.showinfo("Resultado", f"El número {valor} SÍ está en el árbol.")
            else:
                messagebox.showinfo("Resultado", f"El número {valor} NO está en el árbol.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def imprimir(self):
        valores = self.arbol.imprimirValores()
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, "Valores en orden ascendente:\n")
        self.text_area.insert(tk.END, ", ".join(map(str, valores)))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
