producto=str(input("porfavor ingrese el nombre del producto: \n"))
precio=int(input("porfavor ingrese el costo del producto: \n"))
clave=int(input("porfavor ingrese que clave va a ser CLAVE 1 O CLAVE 2: \n"))

if clave==1:
    descuento= precio-(precio*0.10)
    print(f"usted compró \t {producto}, con la clave 1, con el precio {precio}, con un descuento de 15% con el total de: {descuento}")

elif clave==2:
    descuento=precio-(precio*0.20)
    print(f"usted compró \t {producto}, con la clave 2, con el precio {precio}, con un descuento de 20% con el total de: {descuento}")
    