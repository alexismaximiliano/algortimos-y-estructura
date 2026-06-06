# ejercicio 8: menu de operaciones
# alumno: Alexis Cañete

resultado=1
cont=1

print("OPCIONES:")
print("(1) -Cuadrado de un numero")
print("(2) -Par o impar")
print("(3) -Factorial iterativo")
print("(4) -Salir")

opcion=int(input("Ingrese opcion: "))


if(opcion>4):
    print("Opcion seleccionada incorrecta")

elif(opcion==1):
    numero=int(input("Ingrese numero para realizar la operacion: "))
    resultado=numero*numero
    print("RESULTADO:",numero,"^2=",resultado)

elif(opcion==2):
    numero=int(input("Ingrese numero para realizar la operacion: "))
    resultado=numero%2
    if(resultado==0):
        print("RESULTADO:su numero es par")
    else:
        print("RESULTADO:su numero es impar")

elif(opcion==3):
    numero=int(input("Ingrese numero para realizar la operacion: "))
    original=numero
    while(numero>1):
        resultado*=numero
        numero-=1
    print("RESULTADO:",original,"!=",resultado)




while(opcion!=4):
    if(opcion>4):
        print("Opcion seleccionada incorrecta")
    
    # elif(opcion==4):
    #     print("Hasta luego")
    
    elif(opcion==1):
        numero=int(input("Ingrese numero para realizar la operacion: "))
        resultado=numero*numero
        print("RESULTADO:",numero,"^2=",resultado)
    
    elif(opcion==2):
        numero=int(input("Ingrese numero para realizar la operacion: "))
        resultado=numero%2
        if(resultado==0):
            print("RESULTADO: su numero es par")
        else:
            print("RESULTADO: su numero es impar")
    
    elif(opcion==3):
        numero=int(input("Ingrese numero para realizar la operacion: "))
        original=numero
        while(numero>1):
            resultado*=numero
            numero-=1
        print("RESULTADO:",original,"!=",resultado)

    print("")
    print("OPCIONES:")
    print("(1) -Cuadrado de un numero")
    print("(2) -Par o impar")
    print("(3) -Factorial iterativo")
    print("(4) -Salir")

    opcion=int(input("Ingrese opcion: "))

print("Hasta luego")