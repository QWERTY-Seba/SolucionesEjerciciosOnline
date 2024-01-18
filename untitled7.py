

def crear_matriz(x ,y):
    respuesta = []

    for y_ in range(y):
        respuesta.append([0] * x)
    return respuesta



def imprimir_lista_deptos(matriz):
    print("top")
    for y_ in range(len(matriz)-1,-1,-1):
        temp_texto = str(y_+1) + " "
        for x_ in range(len(matriz[y_])):
            if(matriz[y_][x_] == 0):
                temp_texto += " |"
                continue
            temp_texto += "X |"
        print(temp_texto)


def seleccionar_deptos():
    if(todo_ocupado):
        print("todo ocupado")
        return;


    imprimir_lista_deptos(matriz)



    while True:
        print("""Tipo A, 3.800 UF
Tipo B, 3.000 UF
Tipo C, 2.800 UF
Tipo D, 3.500 UF""")
        tipo_depa = input("Tipo de Piso \n")
        tipo_depa = tipo_depa.upper()
        try:
            index_tipo_depa = "ABCD".index(tipo_depa)
            print(index_tipo_depa)
        except:
          print("tipo de depa no existente")
          continue
        
        piso_depa = int(input("Seleccione piso"))-1
                       
        if(piso_depa < 0 or piso_depa >= d_y):
            print("piso fuera de limite")
            continue
            
        if(matriz[piso_depa][index_tipo_depa] != 0):
            print("Sitio ocupado")
            continue

        rut = int(input("Ingrese Rut"))
        matriz[piso_depa][index_tipo_depa] = True

        lista_rut.append([rut,tipo_depa+ str(piso_depa+1)])
        totales[index_tipo_depa] += 1
        break
    if(len(lista_rut) == d_y * d_x):
        print("Todos los espacios ocupados")
        return;



def menu():
    while True:
        opcion  = int(input("1.Departamentos disponibles \n 2.Información \n 3.Totales \n 4.Salir \n"))
        if(opcion == 1):
            seleccionar_deptos()
        elif(opcion == 2):
            print(sorted(lista_rut, key = lambda x: x[0],reverse = True))
        elif(opcion == 3):
            
            print("Tipo de Departamento Cantidad Total")
            print("Tipo A 3.800 UF",totales[0], totales[0] * 3800)
            print("Tipo B 3.000 UF ",totales[1],totales[1] * 3000)
            print("Tipo C 2.800 UF",totales[2], totales[2] * 2800)
            print("Tipo D 3.500 UF",totales[3], totales[3] * 3500)
            print((totales[0] * 3800)+(totales[1] * 3000)+(totales[2] * 2800)+(totales[3] * 3500))
        elif(opcion == 4):
            print("cerrando", "Tomas Catalan Madariaga 10/07/2023")
            break
        else:
            print("opcion no valida" )

d_x = 4
d_y = 10
matriz = crear_matriz(d_x, d_y)
lista_rut = []
global todo_ocupado 
todo_ocupado = False
totales = [0] * d_x
menu()
