# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:29:11 2023

@author: Seba
"""

n = 8
k = 3

n_1 = sorted([1990,500,2000,5000,1000,400,5500,800], reverse = True)
n_2 = sorted([1995, 4000, 5000],reverse = True)

d_muertos = 0
s_usado = 0

for e in range(len(n_2)):
    for i in range(s_usado,len(n_1)):
        print(n_1[i],  n_2[e])
        if(n_1[i] > n_2[e]):
            d_muertos += 1  
            s_usado += 1
            break


if(d_muertos == len(n_2)):
    print("Luchar")
else:
    print("rendirse")