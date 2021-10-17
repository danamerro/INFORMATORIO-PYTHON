nota1=int(input("porfavor ingrese una calificación: \n"))
nota2=int(input("porfavor ingrese una calificación: \n"))
nota3=int(input("porfavor ingrese una calificación: \n"))
nota=(nota1+nota2+nota3)/3
if nota>=70:
    print(f"usted aprobó con una nota de {nota}")
else:
    print(f"usted no aprobó ya que sacó {nota}")


