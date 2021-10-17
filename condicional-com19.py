opción=int(input("porfavor introduzca una de las siguientes opciones  L=1 o P=2 para elegir entre LIBRERÍA o PARTICULARES: \n "))
libro=int(input("escriba la cantidad de libros por favor: \n"))
precio=int(input("escriba el precio: \n"))

if (opción==1) and libro<24:
    descuento=precio-(precio*0.20) 
    print(f"usted pagó {precio}, y obtuvo un descuento de 20%, esto quedaría en: {descuento}.")

elif (opción==1)and(libro>=24):
    descuento=precio-(precio*0.25)
    print(f"usted pagó {precio}, y obtuvo un descuento de 25%, esto quedaría en: {descuento}.")

elif (opción==2) and (libro<6):
    print("nada")

elif (opción==2) and (libro<=18) and (libro>=6):
    descuento=precio-(precio*0.5)
    print(f"usted pagó {precio}, y obtuvo un descuento de 5%, esto quedaría en: {descuento}.")

elif (opción==2) and (libro>18):
    descuento=precio-(precio*0.10)
    print(f"usted pagó {precio}, y obtuvo un descuento de 10%, esto quedaría en: {descuento}.")

else:
    print("selección equivocada")
    





