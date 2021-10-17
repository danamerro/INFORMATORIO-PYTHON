compra=int(input("porfavor ingrese el costo del producto: \n"))
if compra >1000:
    descuento= compra-(compra*0.15)
    print(f"usted deberá pagar {descuento}, ya que tuvo un descuento de 15%.")