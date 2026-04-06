# nombre:Alexis Cañete
# ejercicio 3:suma de dos numeros

# Crear un programa que pida dos números al usuario y muestre su suma, resta, multiplicación y división.
# Asegurarse de que el segundo número no sea cero para la división.

# solicitar los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
# si el segundo número es cero, solicitar otro número
while num2 == 0:
    num2 = int(input("Ingrese un segundo número diferente de cero: "))
# realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
# mostrar los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")
