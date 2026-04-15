# nombre: Alexis Cañete
# ejercicio 2: Calculadora de Masa Corporal

# Solicitar peso (kg) y altura (m). Calcular IMC = peso / altura². Clasificar según:
# IMC < 18.5: Bajo peso
# 18.5 <= IMC < 25: Normal
# 25 <= IMC < 30: Sobrepeso
# IMC >= 30: Obesidad

peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:    
    print("Obesidad")