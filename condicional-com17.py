estatura=float(input("porfavor ingrese su estatura: \n"))
mujer=1.65
varones=1.72

if estatura>mujer:
    print(f"usted tiene {estatura}, es mayor a la promedio")

elif estatura<mujer:
    print(f"usted tiene {estatura}, es menor a la promedio")
elif estatura==mujer:
    print(f"usted tiene {estatura}, es igual a la promedio")
elif estatura>varones:
    print(f"usted tiene {estatura}, es mayor a la promedio")

elif estatura<varones:
    print(f"usted tiene {estatura}, es menor a la promedio")
elif estatura==varones:
    print(f"usted tiene {estatura}, es igual a la promedio")
else:
    print(f"{estatura}, no coincide con lo pedido, por favor vuelva a intentarlo.")