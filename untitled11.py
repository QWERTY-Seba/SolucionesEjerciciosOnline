
#01:35 10:20 04:08 06:36 09:57 00:00
input_llamadas = input("ingrese las duraciones separadas por espacios").split(' ')
#llamadas = ["01:35","10:20","04:08","06:36","09:57","00:00"]



total_minutos = 0
total_segundos = 0
cantidad_llamadas = 0

for llamada in input_llamadas:
    minutos,segundos = llamada.split(":")
    
    if(minutos == "00" and segundos == "00"):
        continue
    
    total_minutos += int(minutos)
    total_segundos += int(segundos)
    cantidad_llamadas += 1
    

minutos_extras = round(total_segundos / 60)
total_minutos += minutos_extras

print(cantidad_llamadas * 3 + total_minutos * 5)