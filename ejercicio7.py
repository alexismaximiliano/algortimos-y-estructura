# nombre: Alexis Cañete
# ejercicio 7: Calculadora de area de un rectangulo

# Solicitar la base y la altura de un rectángulo, calcular y mostrar el área. 
# Validar que los valores ingresados sean positivos.

# Solicitar la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Validar que los valores sean positivos
if base > 0 and altura > 0:
    # Calcular el área del rectángulo
    area = base * altura
    # Mostrar el resultado
    print(f"El área del rectángulo es: {area}")
else:
    print("Ingrese valores positivos para la base y la altura.")