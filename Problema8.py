time = input("Ingrese hora, en formato 24 horas: ")
hours, minutes = time.split(":")

if int(hours) == 7 or (int(hours) == 8 and int(minutes) == 0):
    print("Es hora del desayuno")
elif int(hours) == 12 or (int(hours) == 13 and int(minutes) == 0):
    print("Es hora del almuerzo")
elif int(hours) == 18 or (int(hours) == 19 and int(minutes) == 0):
    print("Es hora de la cena")
else:
    print("No es hora de comer")