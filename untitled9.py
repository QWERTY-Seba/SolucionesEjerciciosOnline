import math
tamaño_frasco = 750
mermelada_por_fruta = 100

i = 0
r = [5,7,10,2,-1]
restante = 0

for c in r:
    if(c > 0):      
        re_dia = c * mermelada_por_fruta
        rere = (re_dia + restante)%tamaño_frasco
        
        c_frascos = math.floor((re_dia + restante) / tamaño_frasco)
        
        
        if(c_frascos >= 1):
            print(c_frascos)
            restante = rere
            continue
        else:
            restante += re_dia    
            print(0)
print(restante)
    
