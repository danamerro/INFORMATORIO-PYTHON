num1=int(input("porfavor introduzca un numero"))
num2=int(input("porfavor introduzca un numero"))

if num1==num2:
    resultado= (num1*num2)
    print(f"{resultado}")

elif num1>num2:
    resultado=(num1-num2)
    print(f"{resultado}")

elif num1!=num2:
    resultado=(num1+num2)
    print(f"{resultado}")