# ejercicio 7: suma de digitos de un numero
# alumno: Alexis Cañete

# solicitar numero al usuario y verificar si es correcto
numero=int(input("Ingrese un numero entero positivo: "))
numeroOriginal=numero
if(numero<0):
    print("el numero ingresado no es correcto.")
    exit()

# aplicar las operaciones para obtener el resutado
suma=0
while(numero>0):
    digito=numero%10 #seleccionar ultimo digito del numero
    suma+=digito    #sumar ese numero al contador "suma"
    numero=numero//10   #quitar ultimo digito
    
print("suma de los digitos de ",numeroOriginal,": ",suma)