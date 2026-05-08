# ejercicio 19: piedra, papel o tijera
# alumno: Alexis Cañete

import random

# reglas del juego
print("1=piedra, 2=tijera 3=papel")

# mano del jugador
jugador=int(input("jugar tu mano(elijiendo un numero) : "))

# mano de la cpu
cpu=random.randint(1,3)
print("eleccion de cpu",cpu)

# evaluar quien es el ganador
if(jugador==cpu):
    print("empate")
elif(jugador==1 and cpu==2)or(jugador==2 and cpu==3)or(jugador==3 and cpu==1):
    print("gana jugador")
else:
    print("gana la cpu")