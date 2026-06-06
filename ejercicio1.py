# ejercicio 1: liquidacion de sueldos con retenciones
# alumno: Alexis Cañete

# solicitar los datos al usuario
sueldoBrutoMensual=float(input("Ingrese su sueldo bruto mensual: "))
añosAntiguedad=int(input("Ingrese sus años de antiguedad: "))
turnoNocturno=bool(input("trabajas turno noche(1=si 0=no): "))

# verificacion para que no sean negativos
if(sueldoBrutoMensual<0 or añosAntiguedad<0):
    print("ERROR: no puedes tener un sueldo o años de antiguedad negativo")

# calcular los distintos bonos y retenciones
if(3<añosAntiguedad<5):
    bonoAños=0.8
elif(6<añosAntiguedad<10):
    bonoAños=0.15
elif(añosAntiguedad>10):
    bonoAños=0.22

if(turnoNocturno):
    bonoTurno=0.30

if(sueldoBrutoMensual>800000):
    retencion=0.09
elif(sueldoBrutoMensual>500000):
    retencion=0.05

# calcular el sueldo total
total=sueldoBrutoMensual+sueldoBrutoMensual*bonoAños+sueldoBrutoMensual*bonoTurno-sueldoBrutoMensual*retencion

# mostrar en pantalla todos los resultados
print("")
print("bruto mensual: $",sueldoBrutoMensual)
print("bono de antiguedad: +$",sueldoBrutoMensual*bonoAños)
print("adicional nocturno: +$",sueldoBrutoMensual*bonoTurno)
print("retencion de ganancias: -$",sueldoBrutoMensual*retencion)
print(f"SUELDO NETO: ${total:.2f}")