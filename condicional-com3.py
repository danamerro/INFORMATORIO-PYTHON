num1=int(input("porfavor ingrese un numero: \t"))
num2=int(input("porfavor ingrese un numero: \t"))
num3=int(input("porfavor ingrese un numero: \t"))

if ((num1<num2) and (num1<num3)) and (num2>num3):
    print(f"{num2},{num3},{num1}")

if ((num1<num3) and (num1<num2)) and (num3>num2):
    print(f"{num3},{num2},{num1}")