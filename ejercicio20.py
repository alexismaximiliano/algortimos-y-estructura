# ejercicio 20: sistema de becas
# alumno: Alexis Cañete

# solicitar los datos al usuario
promedio=float(input("ingresar promedio: "))
ingresos=float(input("ingresar ingresos familiares: "))

# calular el valor de la beca segun el promedio
if(promedio>=9):
    beca=15000
elif(7<promedio<8.99):
    beca=5000
elif(4<promedio<6.99):
    beca=1000
else:
    beca=0

# calcular el porcentaje adicional que pueden obtener
if(15000<ingresos<30000):
    porcentaje=beca*0.20
elif(ingresos>15000):
    porcentaje=beca*0.40
else:
    porcentaje=0

# calcular el valor total de la beca obtenida y mostrarla en pantalla
total=beca+porcentaje
print(beca)
print(porcentaje)
print("el monto total de su beca es: $",total)