# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:18:38 2023

@author: Seba
"""
import os
ruta = r"C:/Users/Seba/Documents/valores_carga_datos_20062023.csv"
csvDatos = """indice_excel;rut cas 213;caso;fecha;respuesta;insert
E28;41;nose;44950;44950;HHHH
E27;;nose;44950;44950;HHHHas
E26;39;nose;44950;aaa;HHHH
E25;38;nose;44950;aaa;HHHH"""


if os.path.isfile(ruta):
    fin_encabezado = csvDatos.find("\n")
    csvDatos = csvDatos[fin_encabezado:]
    print("ya existe")

with open(ruta, 'a') as f:
    f.write(csvDatos)

# import win32gui
# import win32con
# import win32api
# import ctypes
# import time

# new_text = r"C:\Users\Seba\Desktop\ExtensionChrome\TestExcelAddIn\manifest.xml"

# def buscar_ventana_AbrirUbicacion():
#     hwnd_resp = 0
    

#     def buscar_ventana_AbrirUbicacion_callback(hwnd, _):
#         nonlocal hwnd_resp
#         if win32gui.IsWindowVisible(hwnd):
#             window_class = win32gui.GetClassName(hwnd)
#             if(window_class == "#32770"): #Codigo de Clase de Ventanas Guardar como, Abrir Ubicacion, ETC
#                 window_parent = win32gui.GetParent(hwnd)
#                 window_parent_title = win32gui.GetWindowText(window_parent)
#                 if("Google Chrome" in window_parent_title):
#                     print(hwnd, window_parent_title)
#                     hwnd_resp = hwnd
#                     ctypes.set_last_error(win32con.ERROR_SUCCESS)
#                     return False 
        
#     win32gui.EnumWindows(buscar_ventana_AbrirUbicacion_callback, None)
#     return hwnd_resp
#     # return dialogs

# def set_dialog_text(hwnd, text):
#     win32api.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)

# def print_dialog_children(hwnd):
#     def enum_child_windows_callback(child_hwnd, _):
#         window_class = win32gui.GetClassName(child_hwnd)
        
#         if window_class == "Edit":
#             # Modify the text in the path input box
#             set_dialog_text(child_hwnd, new_text)
#             print("Text set successfully")
            
#             # Find the "Open" button control in the dialog
#             open_button_hwnd = win32gui.FindWindowEx(hwnd, 0, "Button", "&Abrir")

#             if open_button_hwnd:
#                 # Click the "Open" button
#                 win32api.SendMessage(open_button_hwnd, win32con.BM_CLICK, 0, 0)
                
#                 print("Button clicked successfully")
#             else:
#                 print("Failed to find the 'Open' button")
            
#             return False #EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE. https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-enumchildwindows
            

    
#     win32gui.EnumChildWindows(hwnd, enum_child_windows_callback, None)
   

# # Get the list of dialogs with window IDs and titles
# save_as_hwnd = buscar_ventana_AbrirUbicacion()

# if(save_as_hwnd == 0):
#     print("No se ha encontrado la ventana de windows")    
# else:    
#     print_dialog_children(save_as_hwnd)





