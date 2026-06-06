# ejercicio 5: simulador de semaforo
# alumno: Alexis Cañete

# inicializacion de variables
tiempoBase=20
tiempoTotal=0
extra=0

# pedir los datos y verificarlos sin son correctos
horaActual=int(input("Ingrese la hora actual:"))
if(0<horaActual>23):
    print("ingrese hora correcta")
    exit()
lluvia=int(input("Esta lloviendo?(1==SI ; 0==NO)"))
if(0>lluvia<1):
    print("ingrese datos correctos")
    exit()
obras=int(input("Hay obras en la calzada (1==si ; 0==NO)"))
if(0>obras<1):
    print("ingrese datos correctos")
    exit()
peatones=int(input("Numero de peatones esperando: "))
if(peatones<0):
    print("no hay peatones esperando")
    exit()

print("")

# determinar los diferentes estados del semaforo y el tiempo total 
if(obras==1):
    if(lluvia==1):
        print("estado: ROJO TOTAL")
    if(lluvia==0):
        print("estado: VERDE REDUCIDO")
        print("tiempo base: 15 seg")

elif(22<horaActual<23 or 0<horaActual<6):
    print("estado: AMARILLO INTERMITENTE ")

else:
    print("estado: VERDE NORMAL")
    print("TIEMPO BASE: ",tiempoBase," seg")
    if(lluvia==1):
        print("extra por lluvia: +10 seg")
        extraLluvia=+10
    if(peatones>10):
        print("extra por flujo: +15 seg")
        extraPeatones=+15
    tiempoTotal=tiempoBase+extraLluvia+extraPeatones
    if(tiempoTotal>40):
        print("estado:TIEMPO EXTENDIDO")
    print("TIEMPO TOTAL= ",tiempoTotal," seg")


