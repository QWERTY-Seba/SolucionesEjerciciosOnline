import numpy as np

#Formula que entrega el caso
def calcular_pasos(r1,c1,r2,c2):
    return ((r1 - r2) ** 2) + ((c1 - c2) ** 2)


def calcular_pasos_minimos(L_puntos_interes, celda_comienzo ):
    #resultado de formula por cada punto_interes
    resultado_pasos = []
    celda_actual = celda_comienzo   
    
    puntos_interes = L_puntos_interes
    L_puntos_interes.append([5,5])
    while len(puntos_interes) > 0:
        #Todos los resultados de la formula para los puntos de interes disponibles
        #2 5 10 4
        lista_pasos = []
        
        
        for celda_destino in puntos_interes:
            
            resultado = calcular_pasos(celda_actual[0],celda_actual[1],celda_destino[0],celda_destino[1])
            lista_pasos.append(resultado)       
        
        paso_mas_corto = min(lista_pasos)        
        indice_paso_mas_corto = lista_pasos.index(paso_mas_corto)   
        #Cambia la posicion del caballo por la posicion de la celda interesante mas cercana
        celda_actual = puntos_interes[indice_paso_mas_corto]        
        #Cuando se obtiene la celda mas cercana se borra
        #Pop funciona con el indice
        puntos_interes.pop(indice_paso_mas_corto)
        
        resultado_pasos.append(paso_mas_corto)   
    resultado_pasos.append(calcular_pasos(celda_actual[0],celda_actual[1],celda_comienzo[0],celda_comienzo[1]))
    return resultado_pasos       

def calcular_tablero(n,k, celdas):
    #Lista con la cantidad de pasos necesarios de todas las celdas del tablero
    #64 valores
    totales = []
    for fila in range(1,n+1):
        for columna in range(1,n+1):
            
            celdas_visitar = celdas
            celda_comienzo = [fila,columna]
            #[1,2,3]
            resultado_pasos_de_celda = calcular_pasos_minimos(celdas_visitar, celda_comienzo)     
            print(f"fila {fila} columna {columna} cantidad de pasos {resultado_pasos_de_celda} total pasos {sum(resultado_pasos_de_celda)}")
            
            totales.append(sum(resultado_pasos_de_celda))          
    return min(totales)

def main():
    #3 2 8 3 2 3 9 1 8 3 2 3 4 5 6 7
    n_casos = input('Ingresar Numero de Casos, puede ser vacio, no se ocupa')
    entrada = input("Ingrese Entrada: ")
    
    #Truco para evitar dobles saltos de linea

    entrada = ' '.join(entrada.split()).replace("\n"," ").split(' ')
    try:
        entradas = np.asarray(entrada, dtype=int).reshape((-1,2))
    except:
        print("Error al registrar la entrada")
        #Googleaste para que el programa no continue si hay un error
        raise
        
    indice_caso = 0  
    tamano_tablero , cantidad_celdas_descatadas = 0,0
    
    celdas_descatadas = []  
    
    #Validaciones no realizadas 
    #   cantidad de casos de prueba valido
    #   cantidad de celdas interesadas
    reasignar_valores_tablero = True
    
    # entradas = [10 2.5 3 455 5 6 ]
    # for indice in range(10):
    # indice = 10 2.5 3 455
    # entradas[1] = 2.5
    
    for fila_entrada in entradas:   
        #Si reasignar_valores_tablero es Verdadero, Crea un nuevo tablero
        if(reasignar_valores_tablero):         
            tamano_tablero , cantidad_celdas_descatadas = fila_entrada
            celdas_descatadas = []
            indice_caso += 1               
            
            if(tamano_tablero < 4 or tamano_tablero > 1000):
                
                print(f"caso {indice_caso} Error tamano fuera de lo permitido {tamano_tablero}")       
                reasignar_valores_tablero = True
            else:
                reasignar_valores_tablero = False
            continue            
        #Validar filas destacadas, asegurar de que no sean mayores al tablero
        if(fila_entrada[0] > tamano_tablero or fila_entrada[0] < 0 or fila_entrada[1] > tamano_tablero or fila_entrada[1] < 0):
            print(f"caso {indice_caso} Error indice fuera de rango {fila_entrada}")
            reasignar_valores_tablero = True
            continue
        celdas_descatadas.append(fila_entrada)
   
        if(len(celdas_descatadas) == cantidad_celdas_descatadas):
            pasos_totales = calcular_tablero(tamano_tablero, cantidad_celdas_descatadas, celdas_descatadas )
            reasignar_valores_tablero = True
            print(f"caso {indice_caso} {pasos_totales} movimientos")
        

main()