num1= int(input("porfavor ingrese un numero"))
num2= int(input("porfavor ingrese un numero"))
num3= int(input("porfavor ingrese un numero"))
if ((num1>num2) and (num1>num3)) and (num2>num3):
    print(f"{num1},{num2},{num3}")

if ((num2>num1) and (num2>num3)) and (num3>num1):
    print(f"{num2},{num3},{num1}")

if ((num3>num1) and (num3>num2)) and (num1>num2):
    print(f"{num3},{num1},{num2}")

if ((num1>num2) and (num1>num3)) and (num3>num2):
    print(f"{num1},{num3},{num2}")

if ((num2>num1) and (num2>num1)) and (num1>num3):
    print(f"{num2},{num1},{num3}")

if ((num3>num1) and (num3>num2)) and (num2>num1):
    print(f"{num3},{num2},{num1}")