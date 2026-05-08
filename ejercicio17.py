# ejercicio 17: Fecha valida

dia=int(input("ingresar un dia a la semana en forma numerica: "))
mes=int(input("ingresar un mes del año en forma numerica: "))
año=int(input("ingresar un año: "))

if(1>dia>31 or 1>mes>12):
    print("la fecha ingresada no existe")

if(año%4==0 and año%100!=0) or (año%400==0):
    bisiesto=True
else:
    bisiesto=False

if(mes==1 or mes==3):
    diaDelMes=31
elif(mes==4):
    diaDelMes=30
elif(mes==2):
    if(bisiesto):
        diaDelMes=29
    else:
        diaDelMes=28
