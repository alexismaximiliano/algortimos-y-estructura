# nombre: Alexis Cañete
# ejercicio 10: Dia de la semana

# Solicitar un número del 1 al 7 y mostrar el día de la semana correspondiente
# (1 = Lunes, 2 = Martes, ..., 7 = Domingo). 
# Validar que el número esté en el rango correcto.

dia=int(input("Ingrese un número del 1 al 7 para conocer el día de la semana: "))
if dia == 1:
    print("el dia seleccionado es lunes")
elif dia == 2:
    print("el dia seleccionado es martes")
elif dia == 3:
    print("el dia seleccionado es miércoles")
elif dia == 4:
    print("el dia seleccionado es jueves")
elif dia == 5:
    print("el dia seleccionado es viernes")
elif dia == 6:
    print("el dia seleccionado es sábado")
elif dia == 7:
    print("el dia seleccionado es domingo")
else:
    print("Numero invalido. ingrese un numero del 1 al 7.")