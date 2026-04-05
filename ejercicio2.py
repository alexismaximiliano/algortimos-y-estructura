# autor: alexis cañete
# ejercicio 2: calculadora de edad

# Solicitar al usuario su año de nacimiento y calcular su edad aproximada (considerando el año actual 2024).
# Mostrar un mensaje con la edad calculada.

# pide edad por teclado al usuario
año= int(input("ingrese su año de nacimiento: ")) 
# hace el calculo restando el año ingresado al año actual(2024)
edad=2024-año
# muestra por consola el resultado 
print(f"tienes {edad} años")