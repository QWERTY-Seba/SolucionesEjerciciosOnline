while True:    
    numero_input = input("ingrese n")
    if(numero_input == ""):
        print("Porfavor ingrese un numero")
        continue
    numero_input = int(numero_input)
    
    if(numero_input <= 0):
        print("Valor ingresado no valido, ingrese Mayor a 0")
        continue
    break

respuestas = []

incremento_acumulado = 0
for valor_incremento in range(1,numero_input+1):
    incremento_acumulado = incremento_acumulado + valor_incremento
    respuestas.append(incremento_acumulado)


#Aca para imprimir como lo pide 
respuestas.reverse()
for valor in respuestas:
    print(valor, end=" ")
