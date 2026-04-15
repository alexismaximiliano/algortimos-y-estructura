# nombre:Alexis cañete
# ejercicio 8: Promedio simple

# Solicitar tres notas (números del 0 al 10) y calcular su promedio. 
# Mostrar si el promedio es aprobado (>= 4) o desaprobado.

# solicitar notas al usuario
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
# calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3
# mostrar si la materia está aprobada o desaprobada
if promedio >= 4:
    print("La materia está aprobada.")   
else:
    print("La materia está desaprobada.")