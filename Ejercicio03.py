#Desarrolle un programa que encuentre el primer y último digito de cualquier número entero positivo.    
#Ejemplo: Si se ingresa 9403, mostrar:El primer dígito es 9El último dígito es 3

#Entrada
while True:
    numero = int(input("Ingrese un numero: "))
    if numero>0:
        break

# Proceso
cont = 0
for letra in str(numero):
    if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9":
        cont += 1

cien = "1"+"0"*(cont-1)
primero = numero//int(cien)

n=[str(numero)]
for i in range(cont-1):
    n.remove(str(i))



# Salida
print("El primer digito es: ",primero)
print("El ultimo digito es: ",n[0])



