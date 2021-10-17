hectaria=int(input("porfavor introduzca el porcentaje de la hectaria:\n"))
if hectaria >=10:
    print("porcentaje de hectaria aprobada para fertilizar")
elif hectaria<10:
        print("porcentaje de hectaria no aprobada para fertilizar")
print("1-SI")
print("2-NO")
vegetación=int(input("¿Tu vegetación es de tipo MATORRAL?"))


if vegetación==1:
    print("Si se puede fertilizar")
if vegetación==2:
    print("No se puede fertilizar porque presenta MATORRAL EN LA HECTARIA")
