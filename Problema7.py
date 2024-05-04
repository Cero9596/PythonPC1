a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

opcion = int(input("Ingrese la opción del menú a tomar: "))

if opcion == 1:
    print(a+b)
elif opcion == 2:
    print(a-b)
elif opcion == 3:
    print(a*b)
else:
    print("Error. Opción inválida")