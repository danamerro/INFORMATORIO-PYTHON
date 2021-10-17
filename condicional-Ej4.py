receta=int(input("porfavor ingrese una de las opciones: op1:receta1 op2:receta2 \t"))

if receta==1:
    ingrediente=int(input("porfavor ingrese una de los siguientes ingredientes: op1:verduras op2:berenjena \t"))
    if ingrediente==1:
        print("usted eligió la receta 1, que cuenta con: lentejas, apio y verduras.")
    if ingrediente==2:
        print("usted eligió la receta 1, que cuenta con: lentejas, apio y berenjena.")

if receta==2:
    ingrediente=int(input("porfavor ingrese una de los siguientes ingredientes: op1:verduras op2:berenjena"))
    if ingrediente==1:
        print("usted eligió la receta 2, que cuenta con: morron, cebolla y verduras.") 
    if ingrediente==2:
        print("usted eligió la receta 2, que cuenta con: morron, cebolla y berenjena.")