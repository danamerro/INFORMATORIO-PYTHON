print("tamaños:")
print("1_Normal")
print("2_Por debajo de lo normal")
print("3_Un poco por encima de lo normal")
print("Sobredimencionado")

tamaño=str(input("porfavor indique el tamaño del pez:\n"))

if tamaño=="1":
    print("Pez en buenas condiciones")

elif tamaño=="2":
    print("Pez con problemas de nutrición")

elif tamaño=="3":
    print("Pez con síntomas de organismo contaminado")

elif tamaño=="4":
    print("Pez contaminado")

else:
    print(f"{tamaño}, no cohincide con lo requerido")
