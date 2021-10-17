sueldo= int(input("porfavor ingrese su salario: \n"))
if sueldo <=6000: 
    sueldoActual= sueldo+(sueldo*0.15)
    print(f"su sueldo es de {sueldo}, su sueldo actual {sueldoActual} es de se aumentó un %15 de su sueldo")

elif (sueldo>6000) and (sueldo<=7900):
    sueldoActual= sueldo+(sueldo*0.10)
    print(f"su sueldo es de {sueldo},su sueldo actual es de {sueldoActual}, se aumentó un %10 de su sueldo")

elif (sueldo<7900) and (sueldo<=12000):
    sueldoActual=sueldo+(sueldo*0.6)
    print(f" su sueldo es de {sueldo},su sueldo actual es de {sueldoActual}, se aumentó un 6%.")

elif sueldo>=12000:
     sueldoActual= sueldo+(sueldo*0)
     print(f" su sueldo es de {sueldo},su sueldo actual es de {sueldoActual}, se aumentó un 0%.")