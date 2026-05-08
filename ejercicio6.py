# nombre: Alexis Cañete
# ejercicio 6: mayor de edad

# Solicitar la edad de una persona y determinar si es mayor de edad (18 años o más). 
# Mostrar "Eres mayor de edad" o "Eres menor de edad" según corresponda.

# solicitar la edad al usuario
edad = int(input("¿Cuántos años tienes? "))
# determinar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")