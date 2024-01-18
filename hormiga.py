# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 00:16:45 2023

@author: Seba
"""

n = 3
b = 3

import numpy as np

tablero = np.zeros((n,n), dtype=int)


for i in range(b):
    print(tablero)
    #fila columna
    coordenada = None;
    while 1:
        coordenada = np.asarray(input(f"bomba {i} ").split(' '), dtype=int)
        
        if(coordenada[0] < 0 or coordenada[0] > n or coordenada[1] < 0 or coordenada[1] > n):
            print("coordenada fuera de rango")
            continue
        break
        
            
    tablero[coordenada[0],[coordenada[1]]] += 1
    
    #norte
    norte = coordenada[0] - 1  
    if(norte >= 0):
        
        tablero[norte][coordenada[1]] += 1
    
    #sur
    sur = coordenada[0] + 1  
    if(sur < n):
        
        tablero[sur][coordenada[1]]  += 1
        
      
    #este
    este = coordenada[1] - 1
    if(este >= 0):
        tablero[coordenada[0]][este] += 1
        
    #oeste
    oeste = coordenada[1] + 1
    if(oeste < n):
        tablero[coordenada[0]][oeste] += 1
print(tablero)