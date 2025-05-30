# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eg5ztQ65j9rlKkG9_18SuQPXELRmjFXv
"""

import random
def generar_conjunto(cardinalidad):
    vacio = set()
    while len(vacio) < cardinalidad:
        numero = random.randint(1, 40)
        vacio.add(numero)
    return vacio


cardinalidad_a = int(input("Ingrese la cardinalidad del conjunto A: "))
conjunto_a = generar_conjunto(cardinalidad_a)
print("Conjunto A:", conjunto_a)

cardinalidad_b = int(input("Ingrese la cardinalidad del conjunto B: "))
conjunto_b = generar_conjunto(cardinalidad_b)
print("Conjunto B:", conjunto_b)

a_union_b = conjunto_a.union(conjunto_b)
print("Unión de A y B:", a_union_b)
a_interseccion_b = conjunto_a.intersection(conjunto_b)
print("Intersección de A y B:", a_interseccion_b)
a_diferencia_b = conjunto_a.difference(conjunto_b)
print("Diferencia de A y B:", a_diferencia_b)
b_diferencia_a = conjunto_b.difference(conjunto_a)
print("Diferencia de B y A:", b_diferencia_a)
a_diferencia_simetrica_b = conjunto_a.symmetric_difference(conjunto_b)
print("Diferencia simétrica de A y B:", a_diferencia_simetrica_b)