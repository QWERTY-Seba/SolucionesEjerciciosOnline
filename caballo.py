def calcular_pasos(r1,c1,r2,c2):
    return ((r1 - r2) ** 2) + ((c1 - c2) ** 2)

# para cada inicio , calcular pasos contra distancia, extraer el menor de la lista, calcular puntos entre si hasta acabar, calcular ultima contra origen
def calcular_pasos_minimos(restantes,actual,pasos):
    #Devolver cuando no quede niuno por iterar
    
    # print(f"debug restantes {restantes}, actual {actual},pasos {pasos}")
    if(len(restantes) == 0):
        return restantes,actual,pasos
    
    
    menor = calcular_pasos(actual[0],actual[1],restantes[0][0],restantes[0][1])
    if(len(restantes) == 1):
        pasos.append(menor)
        return calcular_pasos_minimos([],restantes[0],pasos) 
    
    #Calcular los pasos para todos los destinos
    lista_pasos = []
    for i in range(1,len(restantes)):
        lista_pasos.append(calcular_pasos(actual[0],actual[1],restantes[i][0],restantes[i][1]))
    
    # print(menor, lista_pasos)
    #Buscar el valor menor, guardarlo como actual, eliminarlo de restantes y almacenar los pasos   
    menor_lista = min(lista_pasos)
    
    if(menor_lista < menor):
        ind = lista_pasos.index(menor_lista)+1
        # print(ind)
        actual = restantes[ind]
        pasos.append(menor_lista)
        del restantes[ind]
    else:
        ind = 0
        actual = restantes[0]
        pasos.append(menor)
        del restantes[0]
        
    return calcular_pasos_minimos(restantes,actual,pasos) 
        

def calcular_tablero(n,k, celdas):
    resultado_formula_tablero = []
    
    #Recorra todas las tablero en base a la dimesion
    for i in range(1,n+1):
        for e in range(1,n+1):
           
            
            #A1 B1 .. 1:1 1:2 1:3 
            actual = [i,e]
            pasos = []
            
            celdas , actual, pasos = calcular_pasos_minimos(celdas, actual, [])
            pasos.append(calcular_pasos(actual[0],actual[1],i,e))
            resultado_formula_tablero.append(sum(pasos))
            # print(f"origen {i}:{e} pasos {sum(pasos)}")
    return min(resultado_formula_tablero)
def main():
    n_casos = 3
    
    entradas = [[3,2],[8,3],[2,3],[9,1],[8,3],[2,3],[4,5],[6,7]]
    
    
    
    #tamaño tablero = 8 cantidad_celdas = 3
    index = 0
    for i in range(n_casos): #i = 1
        
        tamano_tablero , cantidad_celdas_descatadas = entradas[index]
        index += 1 # 2
        if(tamano_tablero <= 4 or tamano_tablero > 1000):
            print(f"caso {i+1} Error tamaño fuera de lo permitido {index}")
            continue
        lista_descatadas = []
        saltar_caso = False
        
        #1 hasta 3
        for e in range(index, index+cantidad_celdas_descatadas):
            # [8,3] [2,3]
            #Validar que la celda interesada no sobrepase el tablero
            if(entradas[e][0] > tamano_tablero or entradas[e][0] < 0 or entradas[e][1] > tamano_tablero or entradas[e][1] < 0):
                print(f"caso {i+1} Error indice fuera de rango {entradas[e]}")
                index = e+1
                saltar_caso = True
                break
            lista_descatadas.append(entradas[e])
        if(saltar_caso):
            continue
        
        pasos_totales = calcular_tablero(tamano_tablero, cantidad_celdas_descatadas, lista_descatadas )
        print(f"caso {i+1} {pasos_totales} movimientos")
        
# print("pasos minimos ",min(totales))
main()


