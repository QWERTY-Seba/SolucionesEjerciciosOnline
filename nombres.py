# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:50:29 2023

@author: Seba
"""

import numpy as np

#filas
f = int(input("cantidad_nombres"))
c = 3
initial_array = np.empty((0,3), dtype=object)
for i in range(f):
    nombre = input()
    longitud = len(nombre)
    cantidad_vocales = np.char.count(nombre, "a" ) + np.char.count(nombre, "e" ) + np.char.count(nombre, "i" ) + np.char.count(nombre, "o" ) + np.char.count(nombre, "u" )
    initial_array = np.append(initial_array, np.array([[nombre, longitud, cantidad_vocales]]), axis = 0)
    
indice = np.argmin(initial_array[:, 2].astype(int))
print(initial_array[indice])