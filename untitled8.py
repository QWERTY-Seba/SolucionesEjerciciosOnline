n = 11

inc = 1
i = 0
x = n
while True:
    i += 1
    if(n > inc):
        inc += inc + 1
        continue
    if(n == inc):
        print("si",i)
        break
    elif(n < inc):
        print("no", n,inc,i)
        break
    
   