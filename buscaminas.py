# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:51:29 2023

@author: Seba
"""
import numpy as np
import random

def cradora(n,m):
    tablero = np.zeros(n*n, dtype = int)
    tablero[:m] = -1
    random.shuffle(tablero)
    return tablero.reshape((n,n))



def buscadora(tabla):
    medida = len(tabla)
    for i in range(medida):
        for e in range(medida):
            if(tabla[i][e] == 0):
                
                if(i > 0):
                    x = e if e-1 < 0 else e-1
                    y = e+2
                    tabla[i][e] = tabla[i][e] + sum(num == -1 for num in tabla[i-1][x:y])
                    
                if(i+1 <= medida-1):
                    x = e if e-1 < 0 else e-1
                    y = e+2
                    tabla[i][e] = tabla[i][e] + sum(num == -1 for num in tabla[i+1][x:y])
                
                x = e if e-1 < 0 else e-1
                y = e+2
                tabla[i][e] = tabla[i][e] + sum(num == -1 for num in tabla[i][x:y])
                    
    return tabla
print(buscadora(cradora(4,12)))