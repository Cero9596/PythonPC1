edad_cliente = int(input("Ingrese su edad: "))

if edad_cliente < 4:
    precio_entrada = 0
elif edad_cliente <= 18 and edad_cliente >= 4:
    precio_entrada = 5
elif edad_cliente > 18:
    precio_entrada = 10

print(f"El precio a pagar por la entrada es: {precio_entrada}")