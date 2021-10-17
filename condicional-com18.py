ladoA=int(input("escriba un lado del triangulo: \n"))
ladoB=int(input("escriba un lado del triangulo \n"))
ladoC=int(input("escriba un lado del triangulo \n"))

if (ladoA==ladoB) and (ladoA==ladoC):
    print("usted hizo un triangulo equilátero")

elif (ladoA==ladoB)and (ladoA!=ladoC):
    print("usted hizo un triangulo isósceles")

elif (ladoB==ladoA)and (ladoB!=ladoC):
    print("usted hizo un triangulo isósceles")

elif (ladoC==ladoA)and(ladoC!=ladoB):
    print("usted hizo un triangulo isósceles")

elif (ladoA==ladoC)and(ladoA!=ladoB):
    print("usted hizo un triangulo isósceles")

elif (ladoA!=ladoB) and (ladoA!=ladoC):
    print("usted hizo un triangulo escaleno")

elif (ladoB!=ladoA) and (ladoB!=ladoC):
    print("usted hizo un triangulo escaleno")

elif (ladoC!=ladoA) and (ladoC!=ladoB):
    print("usted hizo un triangulo escaleno")