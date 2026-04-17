import math
# nombre: Alexis Cañete
# ejercicio 14: Ecuacion de segundo grado

# Resolver una ecuacion de segundo grado A*X²+B*X+C=0.
# Solicitar A, B, C. Calcular discriminante =B²-4AC.Mostrar:
#     si discriminante >0:dos soluciones reales
#     si discriminante =0:una solucion real
#     si discriminante <0:no hay soluciones reales
# en caso de haber solucion, mostralas.

# pedir al usuario tres valores
A=float(input("Ingresar valor de A: "))
B=float(input("Ingresar valor de B: "))
C=float(input("Ingresar valor de C: "))

# calcular la discrimante y mostrar las posibles soluciones
D=B**2-4*A*C
print(f"el discrimante es: ",D)
if(D>0):
    print("Hay dos soluciones reales")
    
    X1=(-B+(math.sqrt(B**2-4*A*C)))/2*A
    X2=(-B-(math.sqrt(B**2-4*A*C)))/2*A
    print(f"primera solucion: ",X1)
    print(f"segunda solucion: ",X2)

elif(D==0):
    print("hay una solucion real.")
    X=(-B+(math.sqrt((B**2)-4*A*C)))/2*A
    print(f"la solucion es: ",X)
    
else:
    print("no hay soluciones reales.")

