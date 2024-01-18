# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:51:17 2023

@author: Seba
"""

import numpy as np
tamano = 3
input_v = "5 1 3 1 8 2 3 2 5".split(' ')

l = np.asarray(input_v).reshape((tamano,tamano))

no_simetrica = False
no_hermitiana = False

for i in range(tamano):
    if(no_simetrica):
        break
    for e in range(i+1,tamano):
        if(i == e):
            print("a")
            continue
        
        if(l[e,i] != l[i,e]):
            no_simetrica = True
    
es_par = tamano % 2 == 0

for e in range(int((tamano - es_par) / 2)):
    if(l[e,e] != l[tamano - e - 1,tamano - e - 1]):
        no_hermitiana = True
        break
        
if(no_simetrica and no_hermitiana):
    print("nada")
elif(no_simetrica == True):
    print("hermitiana")
else:
    print("asimetrica")