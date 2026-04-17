# nombre: Alexis cañete
# ejercicio 13:numeros en orden

# Solicitar tres numeros y mostrarlos en orden ascedente.
# Usar comparaciones

numero1=int(input("ingresar un primer numero: "))
numero2= int(input("ingresar un segundo numero: "))
numero3=int(input("ingresar un tercer numero: "))

if(numero1<numero2 and numero1<numero3):
    if(numero2<numero3):
        print(numero1, numero2, numero3)
    else:
        print(numero1,numero3,numero2)

elif(numero2<numero1 and numero2<numero3):
    if(numero1<numero3):
        print(numero2,numero1,numero3)
    else:
        print(numero2,numero3,numero1)
else:
    print(numero3,numero2,numero1)