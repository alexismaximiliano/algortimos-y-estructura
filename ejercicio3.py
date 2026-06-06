# ejercicio 3: tarifa de estacionamiento
# alumno: Alexis Cañete

# pedir los datos de entrada
tipoVehiculo=int(input("ingrese su tipo de vehiculo (1=auto 2=moto 3= camioneta): "))
horaEntrada=int(input("ingrese la hora de entrada: "))
estadia=int(input("ingrese la cantidad de horas que se va quedar: "))

# verificar los errores
if(1<tipoVehiculo<3):
    print("ERROR: tipo de vehiculo no correcto")
if(0<horaEntrada<23 or estadia<0):
    print("ERROR: horas ingresadas incorrectas")

# determinar la tarifa segun el vehiculo seleccionado
if(tipoVehiculo==1): #moto
    tarifa=8000
elif(tipoVehiculo==2): #auto
    tarifa=500
elif(tipoVehiculo==3): #camioneta
    tarifa=1200

tarifaBase=tarifa*estadia

# calcular la recarga segun la hora y el descuento segun la estadia
if(22<=horaEntrada<=23 or 0<=horaEntrada<=6): #nocturno
    recarga=0.40
elif(7<=horaEntrada<=9 or 17<=horaEntrada<=19): #pico
    recarga=0.20
else:
    recarga=0

recargaTotal=tarifaBase*recarga

if(estadia>8):
    descuento=0.15
descuentoTotal=tarifaBase*descuento

# motrar los resultados
print("")
print("Tarifa base: $",tarifaBase)
print("descuento permanencia: -$",descuentoTotal)
print("recargo nocturno: +$",recargaTotal)
print("TOTAL A PAGAR: $",tarifaBase+recargaTotal-descuentoTotal)
