# nombre: Alexis Cañete
# ejercicio 11: Descuento en tienda

# Una tienda ofrece descuentos según el monto de compra:
# Menos de $1000: sin descuento
# De $1000 a $4999: 5% de descuento
# De $5000 a $9999: 10% de descuento
# $10000 o más: 15% de descuento
# Solicitar el monto de compra y mostrar el monto final con el descuento aplicado.

# solicitar el monto de compra
compra=float(input("Ingrese el monto de su compra: "))
# aplicar los descuentos segun el monto ingresado
if compra < 1000:
    descuento = 0
elif compra < 5000:   
    descuento = 5*compra/100
elif compra < 10000:
    descuento = 10*compra/100
else:
    descuento = 15*compra/100
# calcular el monto final con el descuento ya aplicado    
final = compra-descuento
print(f"El monto final con descuento aplicado es: ${final}")