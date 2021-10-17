horas=int(input("cuantas horas trabajo usted? \n"))
if horas<=40:
    pago= horas*16
    print(f"usted trabajó {horas} horas, su pago es de {pago}, son $16 por hora.")

else:
    pago=40*16
    pagoExtra= (horas-40)*20
    print(f"{pago+pagoExtra}")
