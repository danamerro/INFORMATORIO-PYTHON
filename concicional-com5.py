A=int(input("porfavor ingrese un numero: \n"))
B= int(input("porfavor ingrese un numero: \n"))
C= int(input("porfavor ingrese un numero: \n"))

if A>=(B+C):
    print("no se trata de un triangulo.")

elif (A**2)==((B**2)+(C**2)):
    print("es un triangulo rectángulo.")

elif (A**2) > ((B**2) + (C**2)):
    print("es un triangulo obtusángulo")

elif (A**2) < ((B**2) + (C**2)):
    print("es un triangulo ocutángulo.")