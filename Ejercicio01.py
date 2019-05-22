contador = 0
while True:
    numero = 1
    for i in range(2,1001):
        if i%numero==0:
            print(numero)
            contador= contador+1
        else:
            numero+=1
        


