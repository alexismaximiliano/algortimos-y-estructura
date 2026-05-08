# nombre: Alexis Cañete
# ejercicio 12:Calculadora de sueldo

# Solicitar horas trabajadas y tarifa por hora. 
# Calcular el sueldo considerando que las horas extras (más de 40) se pagan al doble. 
# Mostrar sueldo base, horas extras y sueldo total.

horas=float(input("Ingrese las horas trabajadas: "))
tarifa=float(input("Ingrese la tarifa por hora: "))

sueldo_base = horas * tarifa
if (horas > 40):
    horas_extras = horas - 40
    sueldo_total = sueldo_base + (horas_extras * tarifa * 2)
    print(f"Sueldo base: {sueldo_base}")
    print(f"Horas extras: {horas_extras}")
    print(f"Sueldo total: {sueldo_total}")
else:
    print(f"Sueldo total: {sueldo_base}")
