# ejercicio 4:determinacion de cuadrante,eje y distancia al origen
# alumno: Alexis Cañete

x=int(input("ingrese valor de coordenada X: "))
y=int(input("ingrese valor de coordenada Y: "))

print("")

if(x==0 and y==0):
    print("Las coordenadas estan en el punto de origen")
else:
    if(x>0):
        if(y>0):
            print("UBICACION: Cuadrante I")
        else:
            print("UBICACION: Cuadrante IV")
    else:
        if(y<0):
            print("UBICACION: cuadrante III")
        else:
            print("UBICACION: cuadrante II")

distancia=(x**2+y**2)**0.5
print(f"DISTANCIA AL ORIGEN: {distancia :.4f}")

print("SIMETRIA CON EL EJE X: (",x,",",y*-1,")")
print("SIMETRIA CON EL EJE Y: (",x*-1,",",y,")")
print("SIMETRIA CON EL ORIGEN: (",x*-1,",",y*-1,")")