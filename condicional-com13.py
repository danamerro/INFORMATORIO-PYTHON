numero=int(input("porfavor ingrese un numero al azar: \n"))
precio=int(input("porfavor ingrese el precio de su producto: \n"))

if numero<74:
    descuento= precio-(precio*0.15)
    print(f"el precio final es de {descuento}")

elif numero>=74:
    descuento= precio-(precio*0.20)
    print(f"el precio final es de {descuento}")

