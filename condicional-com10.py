primerPersona=int(input("porfavor introduzca el monto de su dinero"))
segundaPersona=int(input("porfavor introduzca el monto de su dinero"))
terceraPersona=int(input("porfavor introduzca el monto de su dinero"))

total=primerPersona+segundaPersona+terceraPersona

porcentaje= int(100*primerPersona/total)
porcentaje2= int(100*segundaPersona/total)
porcentaje3=int(100*terceraPersona/total)

print(f"la cantidad total invertida es de {total} de pesos, de los cuales \n la primer persona tiene {porcentaje}% \n la segunda persona tiene: {porcentaje2}% \n la tercer persona tiene un: {porcentaje3}%")