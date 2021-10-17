barrio=str(input("porfavor ingrese el nombre del barrio: \n"))
tipo=int(input("porfavor ingrese el tipo de barrio \n op1:centrico \n op2: no centrico \n"))
if barrio.lower()[0]<"m"and tipo==1:
    print("usted se encuentra en la sección A, es un barrio centrico.")
elif barrio.lower()[0]>"m" and tipo==2:
    print("usted se encuentra en la sección A, es un barrio no centrico.")
else: 
    print("usted se encuentra en la sección B ")