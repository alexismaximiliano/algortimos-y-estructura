# ejercicio 6: Adivina el numero secreto
# alumno: Alexis Cañete

import random

# determinar el numero que "elije" la computadora y inicializar el contador
numero=random.randint(0,100)
cont=1

# pedir al usuario un numero y verificar si es el mismo de la computadora
usuario=int(input("Ingrese numero: "))
if(numero==usuario):    
    print("el numero es correcto")

# inciar bucle con la logica del juego 
while(usuario!=numero):
    cont+=1
    if(usuario<numero):
        print("el numero es MAYOR")
    else:
        print("el numero es MENOR")
    if(cont==6):
        print("ULTIMO INTENTO")
    if(cont==7):
        print("Perdiste!")
        break
    usuario=int(input("Ingrese numero: "))
    if(numero==usuario):    
        print("el numero es correcto")
print("Numero de intentos: ",cont)