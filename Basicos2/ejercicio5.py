# Escribir un algoritmo que decodifique fechas del siglo XXI. El dato es un entero
# comprendido entre 10100 y 311299. El resultado es una secuencia de caracteres:
# número del día dentro del mes, del mes dentro del año y del año dentro del siglo. Por
# ejemplo, para el dato 30485, el resultado es el texto 3-4-2085.

fecha = input("Introduce la fecha: ")
anio = 2000 + int(fecha[len(fecha)-2:])
mes = int(fecha[len(fecha)-4:len(fecha)-2])
dia = int(fecha[:len(fecha)-4])
cadena = '%d-%d-%d' % (dia, mes, anio)

print (cadena)