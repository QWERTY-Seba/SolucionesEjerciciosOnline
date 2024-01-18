# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 02:04:55 2023

@author: Seba
"""

n = 2
tuneles = n-1
k = 5

costos = [5,10,3,4]
costos_r = [1,5,2,2]

conexiones = [[1,2],[2,3],[3,4]]
conexiones_vecinas = []
import numpy as np

arr = np.array([[1, 2], [2, 3], [5, 4]])

unique_elements = np.unique(arr)
result = []
for elem in unique_elements:
    matching_rows = np.any(arr == elem, axis=1)
    combined_row = np.concatenate(arr[matching_rows])
    result.append(combined_row)

print(result)


