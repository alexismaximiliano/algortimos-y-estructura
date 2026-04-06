# nombre:Alexis Cañete
# ejercicio 5: Par o impar

# Solicitar un número entero al usuario y determinar si es par o impar. 
# Mostrar el resultado con un mensaje explicativo.

# solicitar un número al usuario
numero = int(input("Ingrese un número entero: "))
# determinar si el número es par o impar
if numero % 2 == 0:
    # mostrar el resultado
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")