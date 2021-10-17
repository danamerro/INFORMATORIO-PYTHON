camisas=int(input("cantidad de camisas: \n"))
precio=int(input("porfavor ingrese el monto: \n"))
if camisas >=3:
    descuento= precio-(precio*0.20)
    print(f"el total a pagar {descuento}")

elif camisas<3:
    descuento= precio-(precio*0.10)
    print(f"el total a pagar {descuento}")
