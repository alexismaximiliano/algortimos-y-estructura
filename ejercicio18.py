# ejercicio 18=calculadora de nota final
# alumno: Alexis Cañete

# solicitar las notas de los trabajos y los parciales
practica1=float(input("ingresar nota de la primera practica: "))
practica2=float(input("ingresar nota de la segunda practica: "))
practica3=float(input("ingresar nota de la tercera practica: "))
parcial1=float(input("ingresar nota del primer parcial: "))
parcial2=float(input("ingresar nota del segundo parcial: "))

# calcular los promedios
promParciales=(parcial1+parcial2)/2
promPracticas=(practica1+practica2+practica3)/3

# evaluar si el alumno aprueba la materia o no
if(promParciales<4):
    print("el alumno esta desaprobado")

if(promPracticas<4):
    recuperatorio=float(input("ingresar nota del recuperatorio: "))
    if(recuperatorio>4):
        promPracticas+=2

if(promPracticas>10):
    promPracticas==10

# mostrar la nota final 
notaFinal=(promParciales*0.70)+(promPracticas*0.30)
print("la nota final es:", notaFinal )
    

