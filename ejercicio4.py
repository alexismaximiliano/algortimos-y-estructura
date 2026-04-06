# nombre:Alexis Cañete
# ejercicio 4: Conversor de grados

# Solicitar una temperatura en grados Celsius y convertirla a Fahrenheit
# usando la fórmula: °F = (°C × 9/5) + 32. Mostrar ambos valores.

# solicitar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# convertir a Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# mostrar los resultados
print(f"La temperatura en grados Celsius es: {celsius}")
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")