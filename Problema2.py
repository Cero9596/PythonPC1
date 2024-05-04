consumo = float(input("Ingrese el monto de consumo en el restaurante: "))

porcentaje_propina = int(input("Ingrese el porcentaje de propina que desea dejar al mesero: "))
if porcentaje_propina<15:
    print("Valor incorrecto. Debe ingresar un valor mayor o igual a 15")
    porcentaje_propina = int(input("Ingrese el porcentaje de propina que desea dejar al mesero: "))
    propina = (consumo*porcentaje_propina)/100
else:
    propina = (consumo*porcentaje_propina)/100

print(propina)